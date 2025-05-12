from flask import Blueprint
from ..controllers.daily_tasks_controller import (
    get_all_daily_tasks,
    get_daily_task_by_id,
    create_daily_task,
    update_daily_task,
    get_daily_tasks_by_user
)

daily_tasks_bp = Blueprint('daily_tasks_bp', __name__)

daily_tasks_bp.route('/daily_tasks', methods=['GET'])(get_all_daily_tasks)
daily_tasks_bp.route('/daily_tasks/<int:daily_task_id>', methods=['GET'])(get_daily_task_by_id)
daily_tasks_bp.route('/daily_tasks', methods=['POST'])(create_daily_task)
daily_tasks_bp.route('/daily_tasks/<int:daily_task_id>', methods=['PUT'])(update_daily_task)
daily_tasks_bp.route('/daily_tasks/user/<int:user_id>', methods=['GET'])(get_daily_tasks_by_user)