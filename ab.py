import streamlit as st
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
data = pd.read_csv("emails.csv")

# Data preprocessing
data.drop_duplicates(inplace=True)
X = data['text'].values
y = data['spam'].values

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Vectorizer and model training
cv = CountVectorizer()
x_train = cv.fit_transform(X_train)
x_test = cv.transform(X_test)

nb = MultinomialNB()
nb.fit(x_train, y_train)

# Streamlit application
st.title('Email Spam Detection')

st.write("""
    This application predicts whether an email is spam or not.
    Enter the email text below and click on 'Predict' to see the result.
""")

email_text = st.text_area("Email Text", "")

if st.button('Predict'):
    if email_text:
        # Transform input text and make prediction
        clean_email = cv.transform([email_text])
        prediction = nb.predict(clean_email)[0]

        if prediction == 0:
            st.write("This is a Ham Email!")
        else:
            st.write("This is a Spam Email!")
    else:
        st.write("Please enter an email text to make a prediction.")