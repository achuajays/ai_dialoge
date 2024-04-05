# Asian Drama Script Assistant

This is a Streamlit application for generating scripts for different genres of Asian dramas using OpenAI's GPT-3.5 turbo model. The app allows users to input the main character's name, the number of characters, the genre, and the number of dialogues to generate a script. Additionally, it provides the option to continue generating the script after a full stop, exclamation mark, or question mark.

## About

This script assistant app utilizes OpenAI's GPT-3.5 turbo model to generate scripts for various genres of Asian dramas. Users can input the main character's name, the number of characters, the genre, and the number of dialogues to generate the script. The app also allows for the continuation of script generation after specific punctuation marks.

## Example

Example input:

- Main Character Name: Liu Kang
- Number of characters: 4
- Genre: Kung Fu
- Number of dialogues: 10

## Usage

1. Enter the main character's name, the number of characters, the genre, and the number of dialogues.
2. Click on the "Generate Script" button.
3. The app will display the generated script.
4. If the script ends with a full stop, exclamation mark, or question mark, you can choose to continue the script generation by clicking the "Continue" button.

## Installation

To run the application locally:

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your OpenAI API key and add it to your environment variables.
4. Run the `main.py` script using `streamlit run main.py`.

## Technologies Used

- Python
- Streamlit
- OpenAI GPT-3.5 turbo model