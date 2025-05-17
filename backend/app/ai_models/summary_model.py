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