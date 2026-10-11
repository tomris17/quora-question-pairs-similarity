# ❓ Quora Question Pairs Similarity

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Library-Scikit_Learn-orange.svg)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Library-Pandas-yellow.svg)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/App-Streamlit-red.svg)](https://streamlit.io/)

This repository contains a Natural Language Processing (NLP) solution for identifying whether two questions asked on Quora share the same intent and meaning.

---

## 📊 Project Overview
* **Objective:** Build a classification model that predicts whether a pair of questions are duplicates (log-loss evaluation metric).
* **Key Steps:**
  * Exploratory Data Analysis (EDA) on question frequency, distribution, and word overlap.
  * Feature Engineering (extracting token-based features, length-based features, and fuzzy string matching scores).
  * Text Vectorization and Model Training using machine learning algorithms (Logistic Regression, Random Forest, or XGBoost).
  * Interactive web dashboard deployment via **Streamlit** for real-time question similarity checking.

---

## 🛠️ Tech Stack & Libraries
* **Python**
* **Pandas & NumPy** (Data Processing)
* **Scikit-Learn** (Classification & Vectorization)
* **FuzzyWuzzy** (String Similarity Metrics)
* **Matplotlib & Seaborn** (Data Visualization)
* **Streamlit** (Interactive Dashboard)

---

## 🚀 Getting Started & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tomris17/quora-question-pairs-similarity.git](https://github.com/tomris17/quora-question-pairs-similarity.git)
   cd quora-question-pairs-similarity
