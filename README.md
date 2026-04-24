# 🎓 Student Placement Readiness Predictor

A robust Machine Learning web application designed to evaluate and predict student employability. By analyzing academic performance, technical expertise, and behavioral habits, the system categorizes students into three readiness levels: **Placement Ready**, **Needs Improvement**, or **At Risk**.

---

## 📊 Project Overview

### Problem Statement
Many students lack a clear understanding of where they stand in the competitive job market. This project bridges that gap by using predictive analytics to provide data-driven insights into a student's placement status, helping them identify areas for growth before the actual recruitment season begins.

### Tech Stack
* **Language:** Python
* **Web Framework:** Flask
* **Libraries:** Pandas, NumPy, Scikit-learn, Imbalanced-learn (SMOTE)
* **Frontend:** HTML5, CSS3
* **Deployment:** AWS Elastic Beanstalk

---

## ⚙️ Features & Data Points

The model evaluates students based on a multi-dimensional feature set:

| Category | Features |
| :--- | :--- |
| **Academic Background** | Branch (CSE, ECE, etc.), College Tier (1, 2, or 3), Study Mode |
| **Academic Performance** | CGPA, Attendance %, Mock Test Scores, Core Subject Confidence |
| **Technical Skills** | DSA Problems Solved, Projects Count, Internship Experience |
| **Behavioral Habits** | Study Hours, Sleep Duration, Stress Levels (1–10) |
| **Engineered Features ⭐** | Consistency Score, Effort Intensity, Burnout Risk, Prep Index |

---

## 🧠 Machine Learning Workflow

### 1. Data Processing
* **Feature Engineering:** Created advanced metrics like `stress_sleep_ratio` and `practice_growth_rate` to capture non-linear student behavior.
* **Handling Imbalance:** Applied **SMOTE** (Synthetic Minority Over-sampling Technique) to ensure the model identifies "At Risk" students as accurately as "Ready" ones.
* **Scaling & Encoding:** Standardized numerical data and encoded categorical variables for optimal model performance.

### 2. Model Selection
We evaluated multiple algorithms to find the most reliable predictor:
* Logistic Regression
* Decision Tree Classifier
* **Random Forest Classifier (Best Performer)**

### 3. Performance Metrics
* **Accuracy:** ~86% (Random Forest)
* **Optimization:** Improved recall for minority classes to minimize false negatives in the "At Risk" category.

---

## ☁️ Deployment

The application is fully containerized and deployed on **AWS Elastic Beanstalk**, ensuring scalability and high availability.

**Deployment Steps:**
1. Model serialization using `Pickle`.
2. Flask application environment configuration.
3. Deployment via **EB CLI**.
4. Hosted as a scalable cloud web service.

---

## 📁 Project Structure

```text
Student_Placement_Readiness_Predictor/
│── application.py          # Flask Entry Point
│── train.py                # Model Training Script
│── requirements.txt        # Dependencies
│── models/                 # Saved Pickle files
│── src/                    # Data Processing Scripts
│── templates/              # HTML Web Pages
│── static/                 # CSS & Images
└── data/                   # Dataset Files
```

---

## 🚀 Future Enhancements
* **Deep Learning:** Implementing Neural Networks for higher predictive precision.
* **Explainable AI (XAI):** Integrating **SHAP** or **LIME** to tell students *why* they received a specific score.
* **Recommendation System:** Providing personalized study roadmaps based on the prediction results.

---

## 👩‍💻 Author
**Kousalya Bunga**
*B.Tech in Computer Science & Engineering*
*Specializing in Machine Learning & Full Stack Development*
