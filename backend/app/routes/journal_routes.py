from flask import Blueprint
from ..controllers.journal_controller import (
    get_all_journals,
    get_journal_by_id,
    create_journal,
    update_journal,
    delete_journal,
    get_journals_by_user_id,
)

journal_bp = Blueprint('journal_bp', __name__)

journal_bp.route('/journals', methods=['GET'])(get_all_journals)
journal_bp.route('/journals/<int:journal_id>', methods=['GET'])(get_journal_by_id)
journal_bp.route('/journals', methods=['POST'])(create_journal)
journal_bp.route('/journals/<int:journal_id>', methods=['PUT'])(update_journal)
journal_bp.route('/journals/<int:journal_id>', methods=['DELETE'])(delete_journal)
journal_bp.route('/journals/user/<int:user_id>', methods=['GET'])(get_journals_by_user_id)