from flask import request, Blueprint
from ..ai_models.text_to_speech_model import transcribe_audio_to_text

ai_bp = Blueprint('ai_bp', __name__)

ai_bp.route('/transcribe', methods=['POST'])(transcribe_audio_to_text)