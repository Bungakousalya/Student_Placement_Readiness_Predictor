# 🎓 Student Placement Readiness Predictor

A Machine Learning web application that predicts whether a student is **Placement Ready, Needs Improvement, or At Risk** based on based on student performance metrics.
The project is built using **Flask, Scikit-learn, and deployed on AWS Elastic Beanstalk**.

## 📊 Problem Statement

Students often struggle to understand their placement readiness.  
This project predicts placement readiness using ML based on:

🟦 1. Academic Background Features

These describe the student’s college and academic environment.

branch → Engineering branch (CSE, ECE, etc.)
👉 Shows technical background and specialization.
college_type → Type of college (Tier1 / Tier2 / Tier3)
👉 Represents academic environment quality.
study_mode → Self-study / Coaching / Mixed
👉 Indicates how the student prepares academically.
🟩 2. Academic Performance Features

These measure how well the student is performing in studies.

cgpa → Overall academic score
👉 Core indicator of academic strength.
attendance_percentage → Class attendance rate
👉 Shows discipline and consistency.
mock_test_score → Performance in practice tests
👉 Indicates exam readiness.
core_subjects_confidence → Confidence in core subjects (1–5 scale)
👉 Reflects conceptual understanding.
core_subjects_covered_count → Number of core subjects completed
👉 Shows syllabus completion level.
🟨 3. Coding & Technical Skills

These measure programming and problem-solving ability.

dsa_problems_solved → Number of DSA problems solved
👉 Measures coding practice and problem-solving skill.
projects_count → Number of projects built
👉 Shows practical application skills.
internship → Whether student has internship experience (0/1)
👉 Indicates real-world exposure.
🟧 4. Behavioral & Study Habits

These describe how the student studies and manages time/stress.

study_hours_per_day → Daily study time
👉 Shows dedication and effort.
sleep_hours → Average sleep per day
👉 Impacts focus and performance.
stress_level → Stress rating (1–10)
👉 Indicates mental pressure.
🟥 5. Derived / Engineered Features (IMPORTANT ⭐)

These are created by you (feature engineering) — this is what makes your project stand out.

consistency_score → Balance of study + attendance + practice
👉 Measures regularity.
effort_score → Study effort intensity
👉 Combines consistency and study hours.
stress_sleep_ratio → Stress vs sleep balance
👉 Indicates mental health imbalance.
burnout_score → Risk of burnout
👉 Combines stress + sleep + consistency.
practice_growth_rate → Learning progress rate
👉 Measures coding improvement speed.
prep_index → Final readiness score (very important)
👉 Overall combined indicator of placement readiness.
🟪 6. Target Variable
placement_status → Final output 
Placement Ready ✅
Needs Improvement ⚠️
At Risk ❌


---

## 🧠 Machine Learning Approach

### ✔ Models Used:
- Logistic Regression
- Random Forest Classifier
- Decision Tree

### ✔ Best Model:
- Logistic Regression / Random Forest (based on evaluation)
---
## ⚙️ Tech Stack

- Python
- Flask
- Pandas, NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- HTML (Frontend)
- AWS Elastic Beanstalk (Deployment)

---

## 🏗️ Project Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Encoding & Scaling
5. Handling Imbalanced Data (SMOTE)
6. Model Training
7. Model Evaluation
8. Flask Web App
9. AWS Deployment

---

## ☁️ Deployment

Deployed using **AWS Elastic Beanstalk**

Steps:
- Flask app containerized logically
- Model serialized using pickle
- Deployed using EB CLI
- Hosted as a scalable web service

---

## 📂 Project Structure


Student_Placement_Readiness_Predictor/
│── application.py
│── train.py
│── requirements.txt
│── models/
│── src/
│── templates/
│── static/
│── data/


---

## 📈 Results

- Accuracy: ~86% (Random Forest)
- Balanced dataset using SMOTE
- Improved recall for minority classes

---

## ⚠️ Challenges Faced

- Handling imbalanced dataset
- Preventing data leakage during SMOTE
- Feature engineering for behavioral data
- NaN issues during training
- Deployment configuration on AWS Elastic Beanstalk

---

## 🚀 Future Improvements

- Add deep learning model
- Improve UI design
- Add student recommendation system
- Add explainable AI (SHAP values)

---

## 👩‍💻 Author

**Kousalya Bunga**  
B.Tech CSE | ML & Full Stack Developer 
