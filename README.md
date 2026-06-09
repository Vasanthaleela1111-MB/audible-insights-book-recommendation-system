# 📚 Audible Insights: Intelligent Book Recommendation System

## 📖 Overview

Audible Insights is an AI-powered Book Recommendation System designed to help users discover books that match their interests and reading preferences. The system leverages Natural Language Processing (NLP), Machine Learning, and Recommendation Techniques to provide personalized book suggestions based on book content, genres, authors, and user preferences.

The project includes data preprocessing, exploratory data analysis, NLP-based feature extraction, clustering techniques, and recommendation models, all integrated into an interactive Streamlit application.

---

## 🎯 Objectives

* Build an intelligent recommendation engine for books.
* Analyze book metadata, ratings, reviews, and genres.
* Extract meaningful text features using NLP techniques.
* Group similar books using clustering algorithms.
* Generate personalized recommendations using multiple recommendation approaches.
* Deploy the system through an interactive Streamlit dashboard.

---

## 📂 Datasets

### Dataset 1: Audible Catalog

Contains detailed book information:

* Book Name
* Author
* Genre
* Rating
* Number of Reviews
* Price
* Description
* Listening Time

### Dataset 2: Audible Catalog Advanced Features

Contains additional metadata:

* Book Name
* Author
* Rating
* Number of Reviews
* Price

The datasets are merged and cleaned before model development.

---

## ⚙️ Project Workflow

### 1. Data Collection

* Audible Catalog Dataset
* Advanced Features Dataset

### 2. Data Cleaning

* Missing value handling
* Duplicate removal
* Data standardization
* Data consistency checks

### 3. Exploratory Data Analysis (EDA)

* Genre distribution analysis
* Rating distribution analysis
* Author performance analysis
* Review trends analysis

### 4. NLP Processing

* Text preprocessing
* TF-IDF Vectorization
* Feature extraction from book descriptions

### 5. Recommendation System Development

* Content-Based Filtering
* Clustering-Based Recommendation
* Hybrid Recommendation Model

### 6. Deployment

* Streamlit Dashboard
* Interactive Recommendation Interface
* Analytics Visualization

---

## 🧠 Machine Learning & NLP Techniques

### NLP

* Text Cleaning
* Tokenization
* TF-IDF Vectorization
* Cosine Similarity

### Machine Learning

* Content-Based Filtering
* K-Means Clustering
* Hybrid Recommendation System

---

## 📊 Analytics Dashboard

The dashboard provides insights such as:

* Most Popular Genres
* Highest Rated Authors
* Rating Distribution Analysis
* Ratings vs Reviews Analysis
* Genre Trends and Patterns

Visualizations are implemented using Matplotlib.

---

## 🚀 Features

* Personalized Book Recommendations
* Author-Based Book Exploration
* NLP-Powered Similarity Matching
* Interactive Analytics Dashboard
* Streamlit Web Interface
* Clean and User-Friendly Design

---

## 🛠️ Technology Stack

### Programming & Data Analysis

* Python
* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* Recommendation Systems
* Clustering

### Natural Language Processing

* TF-IDF Vectorization
* Cosine Similarity
* Text Feature Engineering

### Visualization

* Matplotlib
* Seaborn

### Deployment

* Streamlit
* Pickle

---

## 📁 Project Structure

```text
Audible-Insights/
│
├── datasets/
│   ├── Audible_Catalog.csv
│   └── Audible_Catalog_Advanced_Features.csv
│
├── notebooks/
│   └── Book_Recommendation.ipynb
│
├── models/
│   └── model.pkl
│
├── recommendation.py
├── requirements.txt
└── README.md
```

---

## ▶️ Running the Application

### Run Streamlit

```bash
streamlit run recommendation.py
```

---

## 🎓 Author

**Vasantha Leela M**

B.E Computer Science and Engineering
Karpagam Academy of Higher Education

---

## 📌 Future Enhancements

* Collaborative Filtering
* Deep Learning-Based Recommendations
* User Authentication
* Personalized Reading Profiles
* Real-Time Recommendation Updates

---
