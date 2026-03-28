# 📧 Email Spam Detection System

Email Spam Detection System is a web-based machine learning application designed to classify emails as **Spam** or **Ham (Not Spam)**. It uses Natural Language Processing (NLP) techniques and a trained **Naive Bayes model** to analyze email text and provide accurate predictions.
The system includes both a **Flask web application** and a **Streamlit interface** for easy interaction and testing.

## 🎯 Features

🔒 Simple and user-friendly interface
📧 Email classification (Spam / Ham)
🧠 Machine learning model using Naive Bayes
🔍 Text vectorization using CountVectorizer
🌐 Flask-based web application
⚡ Streamlit-based quick testing interface
📊 Real-time prediction output
💾 Pre-trained model loaded using Pickle

## 🏢 Tech Stack

- ⚙️ Backend : Python (Flask)
- 🎨 Frontend : HTML, CSS
- 🧠 Machine Learning : Scikit-learn (Naive Bayes, CountVectorizer)
- 📊 Data Processing : Pandas, NumPy
- 🟢 Interface : Streamlit

## 🏰 Installation Guide

### 1. Prerequisites

🐍 Python 3.x
📦 Required Python libraries (Flask, Streamlit, sklearn, pandas, numpy)

### 2. Setup Instructions

💽 Download and extract the project files
📁 Ensure all files are in proper folder structure
📊 Place `emails.csv` dataset in project folder
💾 Keep `Naive_model.pkl` in the root directory



## 🎭 How to Use

### 🔑 Flask Web App

📌 Open terminal and run:

```bash
python main.py
```

🌐 Open browser and go to:
http://127.0.0.1:5000/

📧 Enter email text and submit to get prediction



### ⚡ Streamlit App

📌 Run the following command:

```bash
streamlit run ab.py
```

📧 Enter email content
▶️ Click **Predict** to view result



## 📊 Output

✅ Ham Email (Not Spam)
🚫 Spam Email



## 💡 Acknowledgements

* 🌐 Flask – Backend web framework
  https://flask.palletsprojects.com/

* ⚡ Streamlit – Interactive web application framework
  https://streamlit.io/

* 🧠 Scikit-learn – Machine learning library
  https://scikit-learn.org/

* 📊 Pandas – Data analysis and processing
  https://pandas.pydata.org/

* 🔢 NumPy – Numerical computations
  https://numpy.org/

* 🤝 Open-Source Community – Resources, tutorials, and support
  https://github.com/
