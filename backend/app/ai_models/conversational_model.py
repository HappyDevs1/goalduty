import os
from flask import request, jsonify
from openai import OpenAI
from ..db import db
from ..models.user_model import User
from ..models.ai_messages_model import AIMessages
from ..models.user_messages_model import UserMessages

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
    user_id = data.get("user_id")
    if not user_input:
        return jsonify({"error": "Missing 'message' field in JSON body"}), 400
    
    if not user_id:
        return jsonify({"error": "Missing 'user_id' field in JSON body"}), 400
    
    # Check if user_id exists in the database
    user = db.session.query(User).filter_by(id=user_id).first()

    if not user:
        return jsonify({"error": "User not found"}), 404
    
    # Check if user_id is valid
    if not isinstance(user_id, int):
        return jsonify({"error": "Invalid user_id"}), 400

    try:
        followup_question = chat(user_input)

        # Save the user message
        user_in_messages = UserMessages.query.filter_by(user_id=user_id).all()

        if user_in_messages:
            user_in_messages.messages = []
            user_in_messages.messages.append(user_input)
        else:
            user_in_messages = UserMessages(user_id=user_id, messages=user_input)
            db.session.add(user_in_messages)

        # Save the AI message
        ai_message = AIMessages.query.filter_by(user_id=user_id).all()

        if ai_message:
            ai_message.messages = []
            ai_message.messages.append(followup_question)
        else:
            ai_message = AIMessages(user_id=user_id, messages=followup_question)
            db.session.add(ai_message)

        db.session.commit()
            
        return jsonify({"response": followup_question})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
