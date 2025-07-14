from .auth import bp as auth_bp
from .tasks import bp as tasks_bp

__all__ = [
    'auth_bp',
    'tasks_bp',
]
