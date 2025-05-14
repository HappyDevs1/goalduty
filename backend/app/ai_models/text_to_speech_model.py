from huggingface_hub import InferenceClient
import os

hf_api_key = os.getenv("HUGGINGFACE_TOKEN")

os.environ['CURL_CA_BUNDLE'] = ''
os.environ['REQUESTS_CA_BUNDLE'] = ''

from dotenv import load_dotenv
load_dotenv()

test_audio = "C:/Users/i7 dell/Downloads/videoplayback.m4a"

def transcribe_audio_to_text(test_audio):
  client = InferenceClient(
    provider="fal-ai",
    api_key=hf_api_key,
  )

  output = client.automatic_speech_recognition(test_audio, model="openai/whisper-large-v3")

  return(output)