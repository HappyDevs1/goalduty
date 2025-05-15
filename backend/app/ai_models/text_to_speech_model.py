from flask import request, jsonify
import io
import whisper
import torchaudio
import torch

model = whisper.load_model("base")

def transcribe_audio_to_text(audio_bytes):
    audio_file = io.BytesIO(audio_bytes)

    # Load audio with torchaudio
    waveform, sample_rate = torchaudio.load(audio_file)

    # Resample if needed
    if sample_rate != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        waveform = resampler(waveform)
        sample_rate = 16000

    # Convert to mono if stereo
    if waveform.shape[0] > 1:
        waveform = torch.mean(waveform, dim=0, keepdim=True)

    # Convert waveform to numpy array for Whisper
    audio = waveform.squeeze().numpy()

    result = model.transcribe(audio)
    return result["text"]

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


# import whisper

# Production ready function to transcribe audio

# def transcribe_audio_to_text(audio_file):
#     model = whisper.load_model("base")
#     result = model.transcribe(audio_file)
#     return result["text"]