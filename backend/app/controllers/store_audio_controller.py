from flask import request, jsonify
from supabase import create_client
import os

from dotenv import load_dotenv
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SERVICE_SUPABASE_KEY = os.getenv("SERVICE_SUPABASE_KEY")

superbase = create_client(SUPABASE_URL, SERVICE_SUPABASE_KEY)

# Production ready function to upload audio files to Supabase storage
def upload_to_storage(file_obj, filename):
  bucket = superbase.storage.from_("goalduty-audio")
  bucket.upload(filename, file_obj)
  public_url = f"{SUPABASE_URL}/storage/v1/object/public/audio_uploads/{filename}"
  return public_url

# def store_audio():
#   if 'file' not in request.files:
#     return jsonify({'message': 'No file part'}), 400

#   file = request.files['file']

#   if file.filename == '':
#     return jsonify({'message': 'No selected file'}), 400

#   filename = file.filename
#   public_url = upload_to_storage(file, filename)

#   return jsonify({
#     'message': 'File uploaded successfully',
#     'url': public_url
#   }), 200

# Test function to upload audio files to Supabase storage
def store_audio():
  file_path = "C:/Users/i7 dell/Downloads/audio_to_test.mp3"
  filename = "test_audio.mp3"

  with open(file_path, "rb") as f:
    public_url = upload_to_storage(f, filename)
  return jsonify({
    'message': 'File uploaded successfully',
    'url': public_url
  }), 200