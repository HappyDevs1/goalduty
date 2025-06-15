from flask import Blueprint
from ..controllers.future_goals_controller import (
    get_all_future_goals,
    get_future_goal_by_id,
    create_future_goal,
    update_future_goal,
    get_future_goals_by_user_id
)

future_goals_bp = Blueprint('future_goals_bp', __name__)

future_goals_bp.route('/future_goals', methods=['GET'])(get_all_future_goals)
future_goals_bp.route('/future_goals/<int:future_goals_id>', methods=['GET'])(get_future_goal_by_id)
future_goals_bp.route('/future_goals', methods=['POST'])(create_future_goal)
future_goals_bp.route('/future_goals/<int:future_goals_id>', methods=['PUT'])(update_future_goal)
future_goals_bp.route('/future_goals/user/<int:user_id>', methods=['GET'])(get_future_goals_by_user_id)