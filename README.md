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
- Inspected data structure and types

### 2️⃣ Data Cleaning & Preprocessing
- Handled missing values
- Removed duplicates
- Standardized data formats

### 3️⃣ Feature Engineering
- Created new features such as:
  - Duration categories
  - Time-based features (Year, Quarter)
  - Derived metrics

### 4️⃣ Exploratory Data Analysis (EDA)
- Analyzed:
  - Subjects distribution
  - Pricing patterns
  - Subscriber behavior
- Visualized insights using Plotly

### 5️⃣ Time Series Analysis
- Analyzed trends over time for:
  - Profit
  - Subscribers
- Identified growth patterns and seasonality

### 6️⃣ Machine Learning Model
- Built **XGBoost regression model**
- Predicts optimal course price
- Based on features like:
  - Subject
  - Duration
  - Level
  - Number of lectures
  - Time features

### 7️⃣ Recommendation System
- Built content-based recommendation system
- Used:
  - TF-IDF Vectorization
  - Cosine Similarity
- Recommends similar course titles

### 8️⃣ Deployment
- Built interactive web app using Streamlit
- Deployed on Streamlit Cloud

---

## 💡 Key Insights

- Web Development is the most profitable subject  
- Short courses (1–3 hours) perform best  
- Free courses increase user engagement  
- Optimal price range: $25–$50  
- Strong seasonal patterns in course performance  

---

## 🧠 Machine Learning Components

- **Price Prediction Model**
  - Algorithm: XGBoost  
  - Accuracy: ~92%  

- **Recommendation System**
  - TF-IDF + Cosine Similarity  
  - Smart course recommendations  

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
