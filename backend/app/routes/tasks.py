from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..extensions import db
from ..models.task import Task
from ..schemas.task import TaskSchema

bp = Blueprint('tasks', __name__, url_prefix='/tasks')
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@bp.get('/')
@jwt_required()
def list_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    return tasks_schema.jsonify(tasks)

@bp.post('/')
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()
    task = Task(**data, user_id=user_id)
    db.session.add(task)
    db.session.commit()
    return task_schema.jsonify(task), 201

@bp.put('/<int:task_id>')
@jwt_required()
def update_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first_or_404()
    data = request.get_json()
    for field in ['title', 'description', 'status', 'due_date']:
        if field in data:
            setattr(task, field, data[field])
    db.session.commit()
    return task_schema.jsonify(task)

@bp.delete('/<int:task_id>')
@jwt_required()
def delete_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'})
