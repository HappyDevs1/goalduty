from flask import Blueprint
from ..controllers.daily_report_controller import (
    get_all_daily_reports,
    get_daily_report_by_id,
    create_daily_report,
    update_daily_report
)

daily_report_bp = Blueprint('daily_report_bp', __name__)

daily_report_bp.route('/daily_report', methods=['GET'])(get_all_daily_reports)
daily_report_bp.route('/daily_report/<int:daily_report_id>', methods=['GET'])(get_daily_report_by_id)
daily_report_bp.route('/daily_report', methods=['POST'])(create_daily_report)
daily_report_bp.route('/daily_report/<int:daily_report_id>', methods=['PUT'])(update_daily_report)