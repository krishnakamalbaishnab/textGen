from dotenv import load_dotenv

load_dotenv()

#import the required libraries

import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#function to load gemini models and get response

model = genai.GenerativeModel('gemini-pro')

def get_response(question):
    response = model.generate_content(question)
    return response.text


#streamlit app

st.set_page_config(page_title="Demo Application", page_icon=":rocket:")
st.header("Gemini Pro Demo Application")

input=st.text_input("Input", key="input")
submit=st.button("Ask the question", key="ask")