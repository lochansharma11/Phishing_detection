import streamlit as st
import pandas as pd
import numpy as np
from sklearn.externals # Replace with 'import joblib' if you're using Python 3.8+
import matplotlib.pyplot as plt
import seaborn as sns

# Load pre-trained model
model = joblib.load("phishprotector_model.pkl")  # Replace with your trained model path

# Function to make predictions
def predict_url(url):
    # Here, implement feature extraction for the URL (stub example)
    features = extract_features(url)  # Replace with your feature extraction function
    prediction = model.predict([features])
    return "Phishing" if prediction == 1 else "Legitimate"

# Main app
st.set_page_config(
    page_title="PhishProtector",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🛡️ PhishProtector - Stay Safe Online")
st.write("A cutting-edge tool to detect phishing websites and protect your digital presence.")

# Sidebar
st.sidebar.title("Navigation")
pages = st.sidebar.radio("Go to", ["Home", "Detect Phishing", "About"])

# Home Page
if pages == "Home":
    st.image("security_image.jpg", use_column_width=True)  # Add an attractive image
    st.markdown(
        """
        ## Why Choose PhishProtector?
        - 🔍 **Accurate Detection:** Powered by advanced AI and machine learning.
        - 🛡️ **Comprehensive Protection:** Analyze multiple features of a website.
        - 🌐 **Easy to Use:** Just enter a URL and let the tool do the work.
        
        ## Features
        - Real-time analysis of URLs
        - Detailed reports for suspicious websites
        - Secure and reliable
        """
    )

# Detect Phishing Page
elif pages == "Detect Phishing":
    st.header("🔗 Detect Phishing Websites")
    st.write("Enter a website URL to check if it is legitimate or a phishing attempt.")
    
    url_input = st.text_input("Enter Website URL", placeholder="e.g., http://example.com")
    
    if st.button("Check Now"):
        if url_input:
            with st.spinner("Analyzing..."):
                result = predict_url(url_input)
            st.success(f"The website is classified as: **{result}**")
            if result == "Phishing":
                st.warning("⚠️ This website may pose a threat to your security.")
            else:
                st.info("✅ The website appears to be legitimate.")
        else:
            st.error("Please enter a URL to analyze.")
    
    st.markdown("### Example Reports")
    st.image("example_report.jpg", caption="Sample Analysis Report", use_column_width=True)

# About Page
elif pages == "About":
    st.header("About PhishProtector")
    st.write(
        """
        **PhishProtector** is a project aimed at reducing online threats by identifying phishing websites using machine learning.
        - Designed for users of all technical levels
        - Based on research and real-world datasets
        - Built with Python, Streamlit, and AI algorithms
        """
    )
    st.markdown(
        """
        ### Technologies Used:
        - Python 🐍
        - Scikit-learn 🤖
        - Streamlit 🌟
        - Matplotlib & Seaborn 📊
        """
    )

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Developed by **Your Name**. © 2024 PhishProtector")
