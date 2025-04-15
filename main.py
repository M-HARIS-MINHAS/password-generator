import streamlit as st
import random
import string
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env for secret key
load_dotenv()

# Gemini AI Assistant
def ai_assistant(prompt):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "❌ API key not found. Please check your .env file."
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI Error: {str(e)}"

# Password Generator Logic
def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# -------------------- Custom CSS --------------------
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }

    .main-title {
        color: #10b981;
        font-size: 42px;
        font-weight: bold;
    }

    .stButton>button {
        background-color: #10b981;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #059669;
        transform: scale(1.05);
    }

    .copy-container {
        margin-top: 15px;
        padding: 14px 20px;
        background-color: #dcfce7;
        border: 2px dashed #10b981;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
        color: #065f46;
        word-break: break-word;
    }

    .ai-response {
        background-color: #e0f7fa;
        color: #004d40;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
        font-size: 16px;
    }

    .stSlider > div {
        color: #10b981;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- UI --------------------
st.markdown("<div class='main-title'>🔐 Password Generator</div>", unsafe_allow_html=True)
st.write("Customize your password below:")

length = st.slider("Password Length", min_value=8, max_value=32, value=12)
use_uppercase = st.checkbox("Include Uppercase Letters")
use_numbers = st.checkbox("Include Numbers")
use_special_chars = st.checkbox("Include Special Characters")

password = ""
if st.button("Generate Password"):
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    st.success("✅ Password generated!")

if password:
    st.markdown(f"<div class='copy-container'>🔑 {password}</div>", unsafe_allow_html=True)

# ------------------ AI Assistant ------------------
st.markdown("## 🤖 Ask Gemini AI")
user_query = st.text_input("Ask anything:")
if st.button("Ask AI") and user_query.strip():
    response = ai_assistant(user_query)
    st.markdown(f"<div class='ai-response'>{response}</div>", unsafe_allow_html=True)

# ------------------ Sidebar ------------------
st.sidebar.title("📘 About")
st.sidebar.write("This app helps you create **secure passwords** and ask questions using **Gemini AI**.")

st.sidebar.title("🔗 Resources")
st.sidebar.markdown("""
- [Password Strength Checker](https://www.passwordmeter.com/)
- [Strong Password Tips](https://www.nist.gov/itl/applied-cybersecurity/nist-cybersecurity-center-excellence/strong-passwords)
""")

st.sidebar.title("📩 Contact")
st.sidebar.write("Created by **M Haris** 💻 | Powered by **Streamlit + Gemini AI** 🚀")

