import os
from flask import request, jsonify
from openai import OpenAI
from ..db import db
from ..models.future_goals_model import FutureGoal

token = os.environ["OPENAI_API_KEY"]
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4.1"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def summarize(user_prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant that cleans up, summarizes, and titles long user-submitted text. "
                    "When the user gives you a message, do the following:\n\n"
                    "1. Provide a clean and concise summary of the content.\n"
                    "2. Generate a short and relevant title for the text.\n\n"
                    "Respond in this format:\n"
                    "Title: <generated title>\n"
                    "Summary: <cleaned-up and concise summary>"
                ),
            },
            {
                "role": "user",
                "content": user_prompt,
            }
        ],
        model=model_name
    )

    # Extract the text from the response
    content = response.choices[0].message.content.strip()

    # Simple parsing logic assuming the format is consistent
    lines = content.split("\n")
    title = ""
    summary = ""
    for line in lines:
        if line.lower().startswith("title:"):
            title = line.split(":", 1)[1].strip()
        elif line.lower().startswith("summary:"):
            summary = line.split(":", 1)[1].strip()

    return {"title": title, "summary": summary}

def summarize_daily_tasks(user_task):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant that cleans up, summarizes one like of long sentence into few words of daily tasks"
                    "When the user gives you a message, do the following:\n\n"
                    "1. Provide a clean and concise umbrella word to name the long description of a task into fewer words lesser than 3 words.\n"
                    "2. Make sure the word that represent the task is accurate to what the user must do in the task.\n"
                    "Respond in this format:\n"
                    "Task 1: <generated task word>\n"
                    "Task 2: <generated task word>\n"
                    "Task 3: <generated task word>\n"
                ),
            },
            {
                "role": "user",
                "content": user_task,
            }
        ],
        model=model_name
    )

    # Extract the text from the response
    content = response.choices[0].message.content.strip()

    # Simple parsing logic assuming the format is consistent
    lines = content.split("\n")
    task1 = ""
    task2 = ""
    task3 = ""
    for line in lines:
        if line.lower().startswith("Task 1:"):
            task1 = line.split(":", 1)[1].strip()
        elif line.lower().startswith("Task 2:"):
            task2 = line.split(":", 1)[1].strip()
        elif line.lower().startswith("Task 3:"):
            task3 = line.split(":", 1)[1].strip()

    return {"Task 1": task1, "Task 2": task2, "Task 3": task3}

def get_summary():
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "Missing 'message' field in JSON body"}), 400

    try:
        result = summarize(user_input)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def get_summarized_daily_tasks():
    data = request.get_json()
    user_id = data.get("user_id")

    if not user_id:
        return jsonify({"error": "Missing 'user_id' field in JSON body"}), 400
    try:
        user_tasks = FutureGoal.query.filter_by(user_id=user_id).first()

        result = summarize_daily_tasks(user_tasks.name)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500