import os
from flask import request, jsonify
from openai import OpenAI

token = os.environ["OPENAI_API_KEY"]
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4.1"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def chat(user_prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. Your job is to only ask one follow-up "
                    "question to better understand the user's ultimate goal. "
                    "Do not answer the user. Do not give suggestions. Just ask a clarifying question."
                ),
            },
            {
                "role": "user",
                "content": user_prompt,
            }
        ],
        model=model_name
    )
    return response.choices[0].message.content.strip()

def get_followup():
    data = request.get_json()

    user_input = data.get("message")
    if not user_input:
        return jsonify({"error": "Missing 'message' field in JSON body"}), 400

    try:
        followup_question = chat(user_input)
        return jsonify({"response": followup_question})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
