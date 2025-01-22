from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load gemini models and get a response
def get_response(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text

# Streamlit app
st.set_page_config(page_title="Demo Application", page_icon=":rocket:")
st.header("Gemini Pro Demo Application")

# Input and button
user_input = st.text_input("Input", key="input")
submit = st.button("Ask the question", key="ask")

if submit and user_input:
    try:
        response = get_response(user_input)
        st.subheader("Response:")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.write("Please try again")