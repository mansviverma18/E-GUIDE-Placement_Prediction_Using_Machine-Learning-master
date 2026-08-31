import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import os
import numpy as np
import pickle
import requests
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()  # reads GROQ_API_KEY from your local .env file

app = Flask(__name__, template_folder="templates")

model = pickle.load(open('model.pkl', 'rb'))
model1 = pickle.load(open('model1.pkl', 'rb'))

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "openai/gpt-oss-120b"

@app.route('/')
def h():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict():
    cgpa = request.args.get('cgpa', '0')
    projects = request.args.get('projects', '0')
    workshops = request.args.get('workshops', '0')
    mini_projects = request.args.get('mini_projects', '0')
    skills = request.args.get('skills', '')
    communication_skills = request.args.get('communication_skills', '0')
    internship = request.args.get('internship', '0')
    hackathon = request.args.get('hackathon', '0')
    tw_percentage = request.args.get('tw_percentage', '0')
    te_percentage = request.args.get('te_percentage', '0')
    backlogs = request.args.get('backlogs', '0')
    name = request.args.get('name', 'Student')

    s = skills.count(',') + 1 if skills else 1

    arr = np.array([cgpa, projects, workshops, mini_projects, s,
                    communication_skills, internship, hackathon,
                    tw_percentage, te_percentage, backlogs], dtype=float)

    output = model.predict([arr])[0]

    p = 1 if output == 'Placed' or output == 1 else 0

    arr1 = np.append(arr, p)
    salary = model1.predict([arr1])[0]

    k = f"{int(salary):,}"

    if p == 1:
        out = f"Congratulations {name}! You have high chances of getting placed!"
        out2 = f"Your expected salary will be INR {k} per annum."
    else:
        out = f"Sorry {name}, you have low chances of getting placed. All the best!"
        out2 = "Improve your skills and try again."

    return render_template('out.html', output=out, output2=out2)


@app.route('/chat', methods=['POST'])
def chat():
    """Server-side proxy for the Jeet chatbot. Keeps the Groq API key
    out of the browser/client-side JS entirely."""
    if not GROQ_API_KEY:
        return jsonify({"error": "Server is not configured with a GROQ_API_KEY."}), 500

    data = request.get_json(silent=True) or {}
    messages = data.get("messages")

    if not messages or not isinstance(messages, list):
        return jsonify({"error": "Request must include a 'messages' list."}), 400

    try:
        response = requests.post(
            GROQ_API_URL,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {GROQ_API_KEY}",
            },
            json={
                "model": GROQ_MODEL,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 500,
            },
            timeout=30,
        )
        response.raise_for_status()
        result = response.json()
        reply = result["choices"][0]["message"]["content"].strip()
        return jsonify({"reply": reply})

    except requests.exceptions.HTTPError as e:
        # Bubble up Groq's own error message so it's easy to debug
        try:
            detail = response.json().get("error", {}).get("message", str(e))
        except Exception:
            detail = str(e)
        return jsonify({"error": detail}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Network error contacting Groq: {e}"}), 502


if __name__ == "__main__":
    app.run(debug=True)