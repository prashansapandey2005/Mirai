import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Create client
client = genai.Client(api_key=api_key)

# Personas dictionary
personas = {
    
    "Shree Krishna": "Respond with wisdom from the Bhagavad Gita, playful charm, and divine guidance.",
    "Radha Ji": "Respond with love, devotion, compassion, and gentle spiritual wisdom.",
    "Tom Riddle": "Respond with dark, cunning, and manipulative tone, full of ambition and mystery.",
    "Fred Weasley": "Respond with playful humor, pranks, and witty banter.",
    "George Weasley": "Respond with mischievous jokes, lighthearted sarcasm, and twin-style fun."
}

# Streamlit UI
st.title("🌌 The Multiverse of Chatbots (Upgraded)")
st.write("Choose your chatbot persona and start chatting!")

persona_choice = st.selectbox("Select Persona:", list(personas.keys()))
user_input = st.text_input("Your Message:")

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Send"):
    if user_input:
        # Use a valid model from your list (e.g., gemini-2.5-flash)
        response = client.models.generate_content(
            model="models/gemini-3.1-flash-lite",
            contents=f"{personas[persona_choice]} User said: {user_input}"
        )

        st.session_state.history.append(("You", user_input))
        st.session_state.history.append((persona_choice, response.text))

# Display chat history
for speaker, message in st.session_state.history:
    st.markdown(f"**{speaker}:** {message}")
