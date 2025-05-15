from flask import request, Blueprint, jsonify
from ..ai_models.text_to_speech_model import (transcribe)
from io import BytesIO

ai_bp = Blueprint('ai_bp', __name__)

ai_bp.route('/transcribe', methods=['POST'])(transcribe)

# Production ready flask function

# @ai_bp.route('/transcribe', methods=['POST'])
# def transcribe():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file provided'}), 400

#     file = request.files['file']

#     try:
#         audio_bytes = BytesIO(file.read())
#         result = transcribe_audio_to_text(audio_bytes)
#         return jsonify({'text': result}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500