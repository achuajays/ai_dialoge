import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("api_key")

# Sidebar
st.sidebar.title("About")
st.sidebar.info(
    "This is an AI powered script assistant app. It uses OpenAI's GPT-3.5 turbo model to generate script for different genres of Asian dramas. The app takes input of main character name, number of characters, genre and number of dialogues and generates script. The app generates script for different genres of Asian dramas. The app takes input of main character name, number of characters, genre and number of dialogues and generates script. It also allows user to continue generating script after full stop, exclamation or question mark. "
)

st.sidebar.subheader("Example")
st.sidebar.info(
    "Example:\n\n"
    "Main Character Name: Liu Kang\n\n"
    "Number of characters: 4\n\n"
    "Genre: Kung Fu\n\n"
    "Number of dialogues: 10"
)




st.title("Asian Drama Script Assistant")

main_character_name = st.text_input("Enter main character name:")
num_of_characters = st.number_input("Enter the number of characters:", value=0, step=1)
genre = st.text_input("Enter genre:")
num_of_dialogues = st.number_input("Enter the number of dialogues:", value=0, step=1)

if num_of_characters > 0 and num_of_dialogues > 0:
    if st.button("Generate Script"):
        client = OpenAI(api_key=api_key)

        messages = [
            {"role": "system", "content": "You are an Asian drama assistant, skilled in creating script with 4 points. 1) Main character name 2) Number of characters 3) Genre 4) Number of dialogues"},
            {"role": "user", "content": f"1) {main_character_name} 2) {num_of_characters} 3) {genre} 4) {num_of_dialogues}"}
        ]

        script = ""
        for _ in range(num_of_dialogues):
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages + [{"role": "user", "content": script}]
            )

            new_script = completion.choices[0].message.content
            script += f"\n{new_script}"
            st.success("Continuation Generated!")
            st.code(new_script)

            if '.' in new_script or '!' in new_script or '?' in new_script:
                if st.button("Continue"):
                    messages.append({"role": "user", "content": script})
                else:
                    break

