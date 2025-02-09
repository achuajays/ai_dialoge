import streamlit as st
import os
import json
from openai import OpenAI

# Sidebar information
st.sidebar.title("About")
st.sidebar.info(
    "This is an AI powered script assistant app. It uses an llama model to generate scripts for different genres of Asian dramas. "
    "The app takes as input a main character name, number of characters, genre, and number of dialogues and generates a script. "
    "It also allows you to continue generating script after a full stop, exclamation, or question mark."
)

st.sidebar.subheader("Example")
st.sidebar.info(
    "Example:\n\n"
    "Main Character Name: Li ring\n\n"
    "Number of characters: 4\n\n"
    "Genre: Kung Fu\n\n"
    "Number of dialogues: 10"
)

# Main title and inputs
st.title("Asian Drama Script Assistant")

main_character_name = st.text_input("Enter main character name:")
num_of_characters = st.number_input("Enter the number of characters:", value=0, step=1)
genre = st.text_input("Enter genre:")
num_of_dialogues = st.number_input("Enter the number of dialogues:", value=0, step=1)

# When valid inputs have been provided...
if num_of_characters > 0 and num_of_dialogues > 0:
    if st.button("Generate Script"):
        # Initialize OpenAI client (using your GROQ_API_KEY from the environment)
        client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=os.environ.get("GROQ_API_KEY")
        )

        # Build a prompt instructing the model to return a JSON array.
        # Each element will be a JSON object with a key "dialogue_line".
        prompt = (
            f"Generate an Asian drama script based on the following inputs:\n"
            f"1) Main Character Name: {main_character_name}\n"
            f"2) Number of Characters: {num_of_characters}\n"
            f"3) Genre: {genre}\n"
            f"4) Number of Dialogues: {num_of_dialogues}\n\n"
            f"Return your response as a JSON array. Each element in the array should be a JSON object with a single key "
            f"'dialogue_line' representing one dialogue line. Do not include any extra commentary."
            "Please ensure the response is valid JSON. no text or  ```"
            "allways put "" in the dialogue line"
        )

        messages = [
            {"role": "system", "content": "You are an Asian drama script assistant."},
            {"role": "user", "content": prompt}
        ]

        # Call the API to generate the script
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )

        response_text = completion.choices[0].message.content

        # Attempt to parse the returned text as JSON.
        try:
            script_json = json.loads(response_text)
        except Exception as e:
            st.error("Error parsing JSON output. The response might not be in valid JSON format.")
            st.text_area("Raw response:", value=response_text, height=200)
        else:
            st.subheader("Generated Script (JSON)")
            # Show the full JSON response using Streamlit's built-in JSON viewer.
            st.json(script_json)

            # Map the JSON output to a nicer UI—for example, a bullet list of dialogues.
            st.markdown("### Script Dialogues:")
            for dialogue_obj in script_json:
                dialogue_line = dialogue_obj.get("dialogue_line", "No dialogue provided")
                st.markdown(f"- {dialogue_line}")
