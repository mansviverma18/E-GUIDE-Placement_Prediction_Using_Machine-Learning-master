E-GUIDE: Placement Prediction using Machine Learning
E-GUIDE is an interactive E-portal designed to guide engineering students through their placement journey. By leveraging data-driven insights and machine learning, the platform predicts placement probability and estimates potential salaries while providing actionable feedback to help students enhance their employability.

Final Result
<img src="static/images/pl1.png" alt="Alt text" width=100%>
<img src="static/images/pl2.png" alt="Alt text" width=100%>
<img src="static/images/pl3.png" alt="Alt text" width=100%>

Table of Contents
Overview

Key Features

Dataset

Installation

Project Structure

Data Preprocessing

Model Training

Results

Deployment

Team

Overview
Campus recruitment is a high-stakes period for engineering students. E-GUIDE empowers students by using Random Forest models to forecast placement status (Placed/Not Placed) and provide personalized advice based on academic and skill metrics. It also offers institutional insights to help colleges refine their career readiness programs.
+2

Key Features

Dual-Model Prediction: Utilizes distinct Random Forest models for placement classification and salary regression.


Strict Confidence Threshold: Employs a high confidence threshold (90%) for placement determination to ensure realistic and high-precision guidance.


Skill Gap Analysis: Integrated chatbot functionality to suggest programming languages and technologies for improvement.


Personalized Action Plan: Analyzes individual "Feature Importance" (e.g., impact of CGPA vs. Internships) to deliver tailored feedback.

Dataset
The project utilizes a comprehensive dataset featuring:


Academic Performance: CGPA, 10th & 12th Percentages, and Backlogs.
+1


Skill Development: Number of Major/Mini projects, Workshops/Certifications, and Skills count.
+1


Professional Exposure: Internship and Hackathon participation.
+1


Soft Skills: Communication Skill Rating.

Installation
Clone the repository:

Bash
git clone https://github.com/mansviverma18/E-GUIDE-Placement_Prediction_Using_Machine-Learning-master.git
Install dependencies:

Bash
pip install -r requirements.txt
Project Structure
app.py: Flask backend managing prediction logic and web routing.

Placement_Prediction.py: Script for training the Random Forest classification model.

preprocessing.ipynb: Jupyter Notebook detailing data cleaning, renaming, and handling missing values.

model.pkl & model1.pkl: Serialized pickle files for the Placement and Salary models.

static/ & templates/: UI components (HTML/CSS/Images).

Data Preprocessing
Key steps taken during preprocessing include:

Cleaning: Removing unnecessary columns (e.g., StudentId, Unnamed indices).

Missing Values: Filling null entries with zero to ensure model stability.

Encoding: Label encoding categorical features like 'Internship' and 'Hackathon'.


Renaming: Improving column readability for internal processing (e.g., 'communi_rating').

Model Training
The system uses Random Forest algorithms for high reliability:

Placement Model: A RandomForestClassifier (Entropy criterion) trained on a 70/30 data split.


Salary Model: A RandomForestRegressor used to estimate annual packages for placed candidates.

Results
Placement Prediction Model
Accuracy: ~92% (based on test set reports).

Precision/Recall: Strong performance across both placed and not-placed classes (F1-score ~0.90-0.93).

Flask App
The application allows users to input their profile details via a web form. The backend processes the input, converts skills into numerical formats, and returns immediate placement probability and estimated salary.

Team
Team Path Guiders (Krishna Institute of Engineering & Technology):

Mansvi Verma

Arnav Sharma

Lakshay Tyagi

Hardik Garg


Project Guide: Mr. Shivansh Prasad 
+1

License
This project is licensed under the MIT License.

