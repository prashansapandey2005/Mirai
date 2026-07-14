import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# --- Load API key ---
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# --- Configure Gemini client ---
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-3.1-flash-lite")

# --- Personas dictionary ---
personas = {
    "Shree Krishna": "Respond with wisdom from the Bhagavad Gita, playful charm, and divine guidance.",
    "Radha Ji": "Respond with love, devotion, compassion, and gentle spiritual wisdom.",
    "Tom Riddle": "Respond with dark, cunning, and manipulative tone, full of ambition and mystery.",
    "Fred Weasley": "Respond with playful humor, pranks, and witty banter.",
    "George Weasley": "Respond with mischievous jokes, lighthearted sarcasm, and twin-style fun."
}

# --- Streamlit UI ---
st.title("🌌 The Multiverse of Chatbots")
st.write("Choose your chatbot persona and start chatting!")

persona_choice = st.selectbox("Select Persona:", list(personas.keys()))

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
    response = model.generate_content(
        f"{personas[persona_choice]} User said: {user_message}"
    )
    assistant_reply = response.text

    # Save assistant reply
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    with st.chat_message("assistant"):
        st.markdown(f"**{persona_choice}:** {assistant_reply}")
