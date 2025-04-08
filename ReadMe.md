# ChatGPT with Streamlit 💬

This is a simple chat application built using [Streamlit](https://streamlit.io/) and OpenAI's GPT-4o model. The app allows users to interact with a chatbot that provides responses in a sarcastic yet helpful tone.

## Features
- Interactive chat interface powered by Streamlit.
- Uses OpenAI's GPT-4o model for generating responses.
- Maintains chat history during the session.
- Customizable assistant personality.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/python-chatbot.git
   cd python-chatbot

2. Install the required dependencies

    pip install -r requirements.txt

3. Add your own OpenAi Api key to

    dir: ".streamlit/secrets.toml"

    OPENAI_API_KEY = "your_openai_api_key"

## Usage

Run the Streamlit app:

Open the app in your browser at http://localhost:8501.

Start chatting with the assistant by typing in the input box.

## File structure

.
├── [main.py](http://_vscodecontentref_/1)               # Main application code
├── [ReadMe.md](http://_vscodecontentref_/2)             # Project documentation
└── .streamlit/
    └── [secrets.toml](http://_vscodecontentref_/3)      # Contains OpenAI API key

## Customization

- Modify the assistant's personality by editing the system message in main.py:

{"role": "system", "content": "You are a sarcastic genZ but helpful assistant."}

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Streamlit
OpenAI