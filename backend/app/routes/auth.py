from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError

from ..extensions import db
from ..models.user import User
from ..schemas.user import UserSchema

bp = Blueprint('auth', __name__)
user_schema = UserSchema()

@bp.post('/register')
def register():
    data = request.get_json()
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Username or email already registered'}), 400
    return user_schema.jsonify(user), 201

@bp.post('/login')
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()
    if not user or not user.check_password(data.get('password')):
        return jsonify({'message': 'Bad credentials'}), 401
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200

@bp.get('/me')
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return user_schema.jsonify(user)
