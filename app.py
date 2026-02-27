import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")

model = pickle.load(open('model.pkl', 'rb'))
model1 = pickle.load(open('model1.pkl', 'rb'))

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

if __name__ == "__main__":
    app.run(debug=True)