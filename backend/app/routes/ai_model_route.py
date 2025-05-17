from flask import request, Blueprint, jsonify
from ..ai_models.text_to_speech_model import transcribe
from ..ai_models.conversational_model import get_followup
from ..ai_models.summary_model import get_summary

ai_bp = Blueprint('ai_bp', __name__)

ai_bp.route('/transcribe', methods=['POST'])(transcribe)
ai_bp.route('/chat', methods=['POST'])(get_followup)
ai_bp.route('/summarize', methods=['POST'])(get_summary)