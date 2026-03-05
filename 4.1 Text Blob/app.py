import streamlit as st
from textblob import TextBlob


st.title("Text Sentiment Analysis")

text = st.text_area("Enter your text:")

if text:
    blob = TextBlob(text)
    st.write("Sentiment Analysis:")
    st.write("-1 represents Negative feedback, 0 means Neutral and +1 represents very Positive Feedback.")
    
    st.write("Sentiment",blob.sentiment.polarity)

    st.write("1 represents immotional impact and 0 represents Rational impactFeedback.")
    st.write("Subjectivity",blob.sentiment.subjectivity)
else:
    st.write("Please enter some text.")
