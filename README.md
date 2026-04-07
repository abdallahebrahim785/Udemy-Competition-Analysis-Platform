# 📊 Udemy Competition Analysis Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://udemy-competition-analysis-platform.streamlit.app/)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🚀 Live Demo

👉 https://udemy-competition-analysis-platform.streamlit.app/

---

## 🎯 Project Overview

This project is a **Data Science and Machine Learning-powered analytics platform** designed to analyze Udemy course data and simulate real-world business decision-making.

It answers key questions such as:
- What makes a course successful?
- How should courses be priced?
- Which subjects are the most profitable?
- How do subscribers and profits evolve over time?
- How can we recommend similar courses?

This project demonstrates a complete **end-to-end Data Science lifecycle** from raw data to deployment.

---

## 🔄 Data Science Lifecycle

### 1️⃣ Data Collection & Import
- Loaded dataset using Pandas  
- Explored data structure and features  

### 2️⃣ Data Cleaning & Preprocessing
- Handled missing values  
- Removed duplicates  
- Standardized formats  

### 3️⃣ Feature Engineering
- Created new features such as:
  - Duration categories  
  - Time-based features (Year, Quarter)  
  - Derived business metrics  

### 4️⃣ Exploratory Data Analysis (EDA)
- Analyzed:
  - Subject distribution  
  - Pricing patterns  
  - Subscriber behavior  
- Visualized insights using Plotly  

### 5️⃣ Time Series Analysis
- Analyzed trends for:
  - Profit  
  - Subscribers  
- Identified growth trends and seasonality  

### 6️⃣ Machine Learning Model
- Built **XGBoost regression model (Best Model)**  
- Predicts optimal course price  
- Uses features like:
  - Subject  
  - Duration  
  - Number of lectures  
  - Difficulty level  
  - Time features  

- Evaluation Metrics:
  - **RMSE (Root Mean Squared Error)**  
  - **MAE (Mean Absolute Error)**  

### 7️⃣ Recommendation System
- Built content-based recommendation system  
- Techniques used:
  - TF-IDF Vectorization  
  - Cosine Similarity  
- Recommends similar course titles based on content  

### 8️⃣ Deployment
- Developed interactive web app using Streamlit  
- Deployed on Streamlit Cloud  

---

## 💡 Key Insights

- Web Development is the most profitable subject  
- Short courses (1–3 hours) perform best  
- Free courses attract more users  
- Optimal price range: $25–$50  
- Strong seasonal trends in course performance  

---

## 🧠 Machine Learning Components

- **Price Prediction Model**
  - Algorithm: XGBoost  
  - Evaluation Metrics: RMSE and MAE  
  - Predicts optimal course pricing based on input features  

- **Recommendation System**
  - TF-IDF + Cosine Similarity  
  - Suggests similar courses based on titles and content  

---

## 🛠️ Tech Stack

- Streamlit  
- Python  
- Pandas, NumPy  
- Plotly  
- Scikit-learn  
- XGBoost  

---

## 📊 Dataset

- 2,782 courses  
- 4 subjects  
- Data from 2012–2017  
- 2.46M+ subscribers  

---

## 🚀 Run Locally

```bash
git clone https://github.com/abdallahebrahim785/udemy-competition-analysis.git
cd udemy-competition-analysis

pip install -r requirements.txt

streamlit run app.py
