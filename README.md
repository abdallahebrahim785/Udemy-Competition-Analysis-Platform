# 📊 Udemy Competition Analysis Platform

> A full-stack data science platform that gives e-learning startups the competitive intelligence they need before entering the market — powered by XGBoost, TF-IDF, and Streamlit.

<div align="center">

[![Streamlit App](https://img.shields.io/badge/🚀%20Live%20App-Streamlit-FF4B4B?style=for-the-badge)](https://udemy-competition-analysis-platform.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/abdallahebrahim785/Udemy-Competition-Analysis-Platform)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)

</div>

---

## 🎯 Business Scenario

Imagine you're a startup founder about to launch a new e-learning platform. Before writing a single line of code or recording a single lesson — you need to understand your competition deeply:

- Which subjects dominate the market?
- How do profit & subscribers evolve over time?
- How should you price your courses to stay competitive?
- Who exactly are you competing against?

This platform answers all of those questions using **2,782 real Udemy courses** spanning **2012–2017**, delivering actionable competitive intelligence through an interactive dashboard built for decision-makers.

---

## 🖼️ Dashboard Preview

| Tab | Description |
|-----|-------------|
| 📚 Subject Analysis | Market share, profit, and subscriber breakdowns by subject |
| 💰 Profit & Subscribers | Time-series trends by subject and course level |
| 🤖 Price Prediction | ML-powered optimal pricing for any new course |
| 🎯 Recommendation System | Find your closest existing Udemy competitors |

---

## 🔄 Project Lifecycle

### 1️⃣ Data Understanding & EDA
Analyzed 2,782 Udemy courses across 4 subjects over 5 years. Key explorations included:
- Pricing patterns across subjects and course levels
- Subscriber growth trends over time
- Content duration impact on engagement
- Paid vs. free course performance comparison

### 2️⃣ Feature Engineering
Crafted domain-specific signals to improve model accuracy:

| Feature | Description |
|---------|-------------|
| `lectures_per_hour` | Ratio of lecture count to content duration |
| `is_long_course` | Binary flag for courses exceeding 10 hours |
| `year` / `quarter` | Temporal seasonality features |
| One-hot encodings | Subject and level categorical variables |

### 3️⃣ Price Prediction Model
Built a regression pipeline using **XGBoost** (with Gradient Boosting fallback) to predict the optimal price for any new course.

- **Target:** Course price (paid courses only)
- **Scaling:** MinMaxScaler on both features and target
- **Validation:** 80/20 train-test split
- **Metrics:** R², MAE, RMSE
- **Key finding:** Subject is the single most influential pricing factor

### 4️⃣ Recommendation System
A **content-based filtering engine** using TF-IDF vectorization and cosine similarity to surface the closest Udemy competitors for any course a startup plans to launch.

- Course title is weighted **3×** for stronger semantic matching
- Subject is weighted **2×** to preserve category relevance
- Bigram TF-IDF captures multi-word topic phrases
- Filterable by subject, level, price, and course type

### 5️⃣ Interactive Dashboard
Wrapped the entire analysis into a **Streamlit** multi-tab dashboard with:
- Global sidebar filters (subject, level, course type, year range)
- Fully interactive **Plotly** charts
- KPI cards with live metrics
- Resettable filters with one click

---

## 💡 Key Findings

- 🥇 **Web Development** dominates with **$69M** in total profit and the highest subscriber count
- ⏱️ **1–3 hour courses** targeting **All Levels** consistently attract the most subscribers
- 🆓 **Free courses** drive massive reach — a freemium launch strategy is strongly supported by the data
- 📈 **2015–2017** shows explosive growth across all subjects and metrics
- 💲 **Subject** is the #1 determinant of course price — Web Dev commands a ~34% premium over Musical Instruments

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Dashboard | Streamlit |
| Visualization | Plotly Express & Graph Objects |
| ML Model | XGBoost / Gradient Boosting (Scikit-learn) |
| Recommender | TF-IDF + Cosine Similarity (Scikit-learn) |
| Data Processing | Pandas, NumPy |
| Scaling | MinMaxScaler |
| Language | Python 3.9+ |

---

## 📁 Project Structure

```
Udemy-Competition-Analysis-Platform/
│
├── app.py                        # Main Streamlit application
├── udemy_courses_cleaned.csv     # Cleaned dataset (2,782 courses)
├── udemy_logo.jpg                # Sidebar logo asset
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/abdallahebrahim785/Udemy-Competition-Analysis-Platform.git
cd Udemy-Competition-Analysis-Platform

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## 📦 Requirements

```
streamlit
pandas
numpy
plotly
scikit-learn
xgboost
```

---

## 📊 Dataset Overview

| Property | Value |
|----------|-------|
| Total Courses | 2,782 |
| Subjects | Web Development, Business Finance, Graphic Design, Musical Instruments |
| Time Period | 2012 – 2017 |
| Total Profit | ~$163M |
| Total Subscribers | ~2.46M |
| Features | Price, subscribers, reviews, lectures, duration, level, subject |

---

## 🔗 Links

- 🌐 **Live App:** [udemy-competition-analysis-platform.streamlit.app](https://udemy-competition-analysis-platform.streamlit.app/)
- 💻 **GitHub:** [github.com/abdallahebrahim785/Udemy-Competition-Analysis-Platform](https://github.com/abdallahebrahim785/Udemy-Competition-Analysis-Platform)

---

## 👤 Author

**Abdallah Ebrahim**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/abdallahebrahim785)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github)](https://github.com/abdallahebrahim785)

---

## ⭐ Support

If you found this project useful, please consider giving it a **star** on GitHub — it helps others discover it!

[![Star on GitHub](https://img.shields.io/github/stars/abdallahebrahim785/Udemy-Competition-Analysis-Platform?style=social)](https://github.com/abdallahebrahim785/Udemy-Competition-Analysis-Platform)

---

<div align="center">
  <sub>Built with ❤️ using Python · Streamlit · XGBoost · Scikit-learn · Plotly</sub>
</div>
