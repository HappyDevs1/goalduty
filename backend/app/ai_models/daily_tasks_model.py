import os
from flask import request, jsonify
from openai import OpenAI
from sqlalchemy.orm.attributes import flag_modified
from ..db import db
from ..models.user_model import User
from ..models.ai_messages_model import AIMessages
from ..models.user_messages_model import UserMessages

# Set up OpenAI client
token = os.environ["OPENAI_API_KEY"]
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4.1"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def generate_openai_response(system_msgs, user_msgs):
    """
    Generates a list of daily tasks based on the user's conversation history.
    """
    system_text = "\n".join(system_msgs)
    user_text = "\n".join(user_msgs)

    prompt = (
        "You are a helpful assistant. Your job is to analyze all the user's messages and the assistant's previous clarifying questions "
        "to understand the user's ultimate goal and context.\n\n"
        "Do not ask follow-up questions. Do not ask for clarification. Just provide at least 2-3 specific daily tasks the user can do "
        "consistently to reach their goal.\n\n"
        f"These are the assistant's previous follow-up questions:\n{system_text}\n\n"
        f"These are the user's previous responses:\n{user_text}"
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": "Based on everything so far, what are some daily tasks I can do to reach my goal?",
            }
        ],
        model=model_name
    )
    return response.choices[0].message.content.strip()

def generate_daily_tasks():
    """
    Flask route handler to generate daily tasks for a user based on past messages.
    """
    data = request.get_json()
    user_id = data.get("user_id")

    if not user_id:
        return jsonify({"error": "Missing 'user_id' field in JSON body"}), 400

    try:
        # Fetch messages from DB
        user_message_record = UserMessages.query.filter_by(user_id=user_id).first()
        ai_message_record = AIMessages.query.filter_by(user_id=user_id).first()

        if not user_message_record or not ai_message_record:
            return jsonify({"error": "No conversation history found for this user."}), 404

        # Ensure messages are lists
        user_msgs = user_message_record.messages if isinstance(user_message_record.messages, list) else [user_message_record.messages]
        ai_msgs = ai_message_record.messages if isinstance(ai_message_record.messages, list) else [ai_message_record.messages]

        result = generate_openai_response(ai_msgs, user_msgs)
        return jsonify({"daily_tasks": result}), 200

    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500
