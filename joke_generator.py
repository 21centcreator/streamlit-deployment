import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()


st.title("AI Joke Generator")

topic = st.text_input("Enter a topic for the joke:")

if st.button("Generate Joke"):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("OPENAI_API_KEY not found in .env file.")
    elif not topic:
        st.error("Please enter a topic.")
    else:
        try:
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a funny comedian."},
                    {"role": "user", "content": f"Tell me a short joke about {topic}."}
                ],
                max_tokens=60,
                temperature=0.8
            )
            joke = response["choices"][0]["message"]["content"].strip()
            st.success(joke)
        except Exception as e:
            st.error(f"Error: {e}")