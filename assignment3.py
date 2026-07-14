import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

# --- Load .env ---
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# --- Configure API ---
genai.configure(api_key=api_key)
# --- Initialize model ---
model = genai.GenerativeModel("gemini-3.1-flash-lite")

# --- Memory Vault ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Render chat history ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Chat input ---
if user_message := st.chat_input("Say something..."):
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_message})
    with st.chat_message("user"):
        st.markdown(user_message)

    # --- Generate response ---
    response = model.generate_content(user_message)

    # Access the text safely
    assistant_reply = response.text

    # Save assistant reply
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
