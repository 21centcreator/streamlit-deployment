import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up Streamlit UI
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
            # Initialize OpenAI client
            client = OpenAI(api_key=api_key)

            # Make chat completion request
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a funny comedian."},
                    {"role": "user", "content": f"Tell me a short joke about {topic}."}
                ],
                max_tokens=60,
                temperature=0.8
            )

            # Extract and display joke
            joke = response.choices[0].message.content.strip()
            st.success(joke)

        except Exception as e:
            st.error(f"Error: {e}")
