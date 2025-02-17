
import streamlit as st
import google.generativeai as genai

# Configure API key
API_KEY = "AIzaSyCCvaPOXeNVp72lsvCRMHmFysqlj5sfCG0"
genai.configure(api_key=API_KEY)

sys_prompt = """You are an AI Code Reviewer. Users will submit Python code, and you should analyze it for potential bugs, 
errors, or areas of improvement. Provide detailed feedback and suggest a fixed version of the code."""

model = genai.GenerativeModel(model_name="model/gemini-1.5-flash",
                              system_instruction=sys_prompt)

st.title("Data Science Tutor Application")

user_prompt = st.text_area("Enter your query:", placeholder="Type your query here.....")

btn_click = st.button("Generate Answer")

if btn_click:
    response = model.generate_content(user_prompt)
    st.write(response)
