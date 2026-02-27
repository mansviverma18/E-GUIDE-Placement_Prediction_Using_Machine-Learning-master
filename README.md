# E-GUIDE: Placement Prediction using Machine Learning

E-GUIDE is an interactive E-portal designed to guide engineering students through their placement journey. By leveraging data-driven insights and machine learning, the platform predicts placement probability and estimates potential salaries while providing actionable feedback to help students enhance their employability.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Data Preprocessing](#data-preprocessing)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

Campus recruitment is a high-stakes period for engineering students. E-GUIDE empowers students by using Random Forest models to forecast placement status (Placed/Not Placed) and provide personalized advice based on academic and skill metrics. It also offers institutional insights to help colleges refine their career readiness programs.

## Key Features

- Dual-Model Prediction: Utilizes distinct Random Forest models for placement classification and salary regression.
- Strict Confidence Threshold: Employs a high confidence threshold (90%) for placement determination to ensure realistic and high-precision guidance.
- Skill Gap Analysis: Integrated chatbot functionality to suggest programming languages and technologies for improvement.
- Personalized Action Plan: Analyzes individual "Feature Importance" (e.g., impact of CGPA vs. Internships) to deliver tailored feedback.

## Dataset

- The project utilizes a comprehensive dataset featuring:
- Academic Performance: CGPA, 10th & 12th Percentages, and Backlogs.
- Skill Development: Number of Major/Mini projects, Workshops/Certifications, and Skills count.
- Professional Exposure: Internship and Hackathon participation.
- Soft Skills: Communication Skill Rating. Other relevant features

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   git clone https://github.com/mansviverma18/E-GUIDE-Placement_Prediction_Using_Machine-Learning-master.git
   
2. Install the required packages:
   pip install -r requirements.txt

## Project Structure

- `static/`: Contains images and css files
- `templates/`: Contains HTML files
- `app.py`: Main Flask App
- `model.pkl`: Pickle file of predicting placement model
- `model1.pkl`: Pickle file of Salary Prediction model [download through - (https://drive.google.com/file/d/1DKbetU7Wg9-71PdZnoVERJwTHFuW6uED/view?usp=drive_link)]
- `Placement_prediction_data.csv`: Placement Prediction data
- `Placement_prediction.py`: Model for Placement Prediction
- `preprocessing.ipynb`: Jupyter Notebook for Data preprocessing
- `requirements.txt`: List of required Python packages
- `salary_prediction_data.csv`: Salary prediction data
- `salary_prediction.py`: Model for salary prediction
- `README.md`: Project documentation

## Data Preprocessing

Key steps taken during preprocessing include:
1. Cleaning: Removing unnecessary columns (e.g., StudentId, Unnamed indices).
2. Missing Values: Filling null entries with zero to ensure model stability.
3. Encoding: Label encoding categorical features like 'Internship' and 'Hackathon'.
4. Renaming: Improving column readability for internal processing (e.g., 'communi_rating').

## Model Training

Two Random Forest classifiers are trained:
1. Placement Prediction Model: A RandomForestClassifier (Entropy criterion) trained on a 70/30 data split.
2. Salary Prediction Model: A RandomForestRegressor used to estimate annual packages for placed candidates.

The training process involves:
1. Splitting the data into training and testing sets
2. Initializing the Random Forest classifiers
3. Training the models on the training set
4. Fine-tuning hyperparameters using techniques like Grid Search or Random Search

## Evaluation

The models' performance is evaluated using various metrics, including:
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Roc_Auc_Score

## Results

### Placement Prediction Model
- Accuracy: ~92% (based on test set reports).
- Precision/Recall: Strong performance across both placed and not-placed classes (F1-score ~0.90-0.93).

## Flask App

The application allows users to input their profile details via a web form. The backend processes the input, converts skills into numerical formats, and returns immediate placement probability and estimated salary.

## Team

Team Path Guiders (Krishna Institute of Engineering & Technology):

- Mansvi Verma

- Arnav Sharma

- Lakshay Tyagi

- Hardik Garg


Project Guide: Mr. Shivansh Prasad

## License

This project is licensed under the MIT License.
