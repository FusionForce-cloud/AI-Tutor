!pip install streamlit google-generativeai pyngrok
import streamlit as st
import google.generativeai as genai

# Configure API key
API_KEY = "AIzaSyCCvaPOXeNVp72lsvCRMHmFysqlj5sfCG0"
genai.configure(api_key=API_KEY)

sys_prompt = """You are a helpful AI Tutor for Data Science.
Students will ask you doubts related to various topics in data science. You are expected to reply in as much detail as possible.
Make sure to take examples while explaining a concept.
In case if a student asks any question outside the data science scope, politely decline and tell
them to ask the question from the data science domain."""

model = genai.GenerativeModel(model_name="model/gemini-1.5-flash",
                              system_instruction=sys_prompt)

st.title("Data Science Tutor Application")

user_prompt = st.text_area("Enter your query:", placeholder="Type your query here.....")

btn_click = st.button("Generate Answer")

if btn_click:
    response = model.generate_content(user_prompt)
    st.write(response)
