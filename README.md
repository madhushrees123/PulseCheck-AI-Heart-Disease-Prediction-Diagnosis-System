# ❤️ CardioSense AI – Smart Heart Disease Detection System

## 📌 Project Overview

CardioSense AI is a machine learning-based web application designed to predict the risk of heart disease using patient health parameters. The system analyzes clinical data such as age, blood pressure, cholesterol levels, and ECG results to classify whether a person is at high risk or low risk of heart disease.

---

## 🎯 Objective

The main objective of this project is to build an intelligent system that can assist in early detection of heart disease using machine learning techniques, improving decision-making in healthcare.

---

## 🧠 Machine Learning Model

* Algorithm Used: **Random Forest Classifier**
* Problem Type: **Binary Classification**
* Output:

  * 0 → Low Risk (No Heart Disease)
  * 1 → High Risk (Heart Disease)

### 🔹 Why Random Forest?

* Handles complex patterns effectively
* Provides higher accuracy compared to basic models
* Reduces overfitting using multiple decision trees

---

## 📊 Dataset

* Source: UCI / Kaggle Heart Disease Dataset

* Features:

  * Age
  * Gender
  * Chest Pain Type
  * Blood Pressure
  * Cholesterol
  * Fasting Blood Sugar
  * ECG Results
  * Maximum Heart Rate
  * Exercise Induced Angina
  * ST Depression
  * Slope
  * Number of Major Vessels
  * Thalassemia

* Target Variable:

  * `heart_disease` (0 or 1)

---

## ⚙️ Technologies Used

### 🔹 Frontend

* Streamlit

### 🔹 Backend

* Flask (REST API)

### 🔹 Machine Learning

* Scikit-learn
* Pandas
* NumPy

### 🔹 Database

* SQLite

---

## 🔄 System Workflow

1. User enters patient details through the web interface
2. Data is sent to the Flask backend API
3. Input data is scaled using StandardScaler
4. Processed data is passed to the trained ML model
5. Model predicts risk level (High / Low)
6. Result is displayed on the UI
7. Prediction is stored in the database

---

## 🚀 Features

* Real-time heart disease prediction
* User-friendly interface with medical inputs
* Backend API integration
* Data storage using SQLite
* Improved model accuracy using Random Forest
* Clean and professional UI design

---

## 📈 Model Performance

* Accuracy: ~85%–90% (depends on dataset)
* Evaluation Metrics:

  * Accuracy
  * Precision
  * Recall
  * F1 Score

---

## 🛠️ How to Run the Project

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Train Model

```bash
cd backend
python train_model.py
```

### Step 3: Run Backend

```bash
python app.py
```

### Step 4: Run Frontend

```bash
cd frontend
streamlit run app.py
```

---

## 📷 Application Preview

* Input form for patient data
* Prediction result (High Risk / Low Risk)
* Clean UI with dropdown selections

---

## 🔮 Future Enhancements

* Use advanced models like XGBoost
* Add confidence score visualization
* Deploy application on cloud
* Add user authentication system
* Improve UI with animations and charts

---

## 👩‍💻 Team

* ------ – Documentation & Frontend
* (Add your team members here)

---

## 📌 Conclusion

CardioSense AI demonstrates how machine learning can be effectively used in healthcare for early detection of heart disease. The project combines data analysis, model building, and web development to create a complete end-to-end solution.

---

## 📚 References

* Scikit-learn Documentation
* UCI Machine Learning Repository
* Streamlit Documentation
* Flask Documentation

---
