🎓 Student Placement Readiness Predictor

A Machine Learning web application that predicts whether a student is Placement Ready, Needs Improvement, or At Risk, based on student performance metrics.

The project is built using Flask, Scikit-learn, and deployed on AWS Elastic Beanstalk.

📊 Problem Statement

Students often struggle to understand their placement readiness.
This project uses machine learning to evaluate students based on academic performance, coding skills, and behavioral patterns to predict their placement status.

📌 Features Used
🟦 Academic Background
branch → Engineering branch (CSE, ECE, etc.)
college_type → Tier of college (Tier1 / Tier2 / Tier3)
study_mode → Learning method (Self / Coaching / Mixed)
🟩 Academic Performance
cgpa → Overall academic score
attendance_percentage → Attendance level
mock_test_score → Mock test performance
core_subjects_confidence → Confidence in core subjects (1–5)
core_subjects_covered_count → Number of core subjects completed
🟨 Coding & Technical Skills
dsa_problems_solved → Number of DSA problems solved
projects_count → Number of projects built
internship → Internship experience (0/1)
🟧 Behavioral & Study Habits
study_hours_per_day → Daily study hours
sleep_hours → Average sleep duration
stress_level → Stress level (1–10)
🟥 Engineered Features (Feature Engineering ⭐)
consistency_score → Study consistency level
effort_score → Overall effort intensity
stress_sleep_ratio → Balance between stress and sleep
burnout_score → Burnout risk indicator
practice_growth_rate → Learning improvement rate
prep_index → Final readiness score
🎯 Target Variable
placement_status
Placement Ready ✅
Needs Improvement ⚠️
At Risk ❌
🧠 Machine Learning Approach
✔ Models Used
Logistic Regression
Random Forest Classifier
Decision Tree
✔ Best Model
Logistic Regression / Random Forest (based on evaluation)
⚙️ Tech Stack
Python
Flask
Pandas, NumPy
Scikit-learn
Imbalanced-learn (SMOTE)
HTML/CSS (Frontend)
AWS Elastic Beanstalk (Deployment)
🏗️ Project Workflow
Data Collection
Data Preprocessing
Feature Engineering
Encoding & Scaling
Handling Imbalanced Data (SMOTE)
Model Training
Model Evaluation
Flask Web Application
AWS Deployment
☁️ Deployment

The application is deployed on AWS Elastic Beanstalk.

Steps:
Trained ML model serialized using Pickle
Flask application configured for production
Deployed using EB CLI
Hosted as a scalable cloud web service
📁 Project Structure
Student_Placement_Readiness_Predictor/
│── application.py
│── train.py
│── requirements.txt
│── models/
│── src/
│── templates/
│── static/
│── data/
📈 Results
Accuracy: ~86% (Random Forest)
SMOTE applied to handle class imbalance
Improved recall for minority classes
⚠️ Challenges Faced
Handling imbalanced dataset
Avoiding data leakage during SMOTE
Feature engineering for behavioral patterns
Missing value (NaN) handling issues
AWS deployment configuration
🚀 Future Improvements
Add deep learning models
Improve UI design
Add explainable AI (SHAP/LIME)
Build student recommendation system
👩‍💻 Author

Kousalya Bunga
B.Tech CSE | Machine Learning & Full Stack Developer
