from flask import request, Blueprint, jsonify
from ..ai_models.text_to_speech_model import transcribe_audio_to_text
from io import BytesIO

ai_bp = Blueprint('ai_bp', __name__)

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

@ai_bp.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Read file as bytes
        audio_bytes = file.read()
        result = transcribe_audio_to_text(audio_bytes)
        return jsonify({"text": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500