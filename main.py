import streamlit as st
from openai import OpenAI

# Page config
st.set_page_config(page_title="ChatGPT with Streamlit", page_icon="💬")

# App title and description
st.title("ChatGPT by projectbaby")
st.write("This is a simple chat application using OpenAI's GPT-4o model.")


# Initialize the OpenAI client
@st.cache_resource
def get_openai_client():
    return OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


client = get_openai_client()

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a sarcastic genZ but helpful assistant."}
    ]

# Display chat history
for message in st.session_state.messages:
    if message["role"] != "system":  # Don't display system messages
        with st.chat_message(message["role"]):
            st.write(message["content"])


# Function to generate response
def generate_response(prompt):
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
        )

        # Extract the response text
        response_text = response.choices[0].message.content

        # Add assistant response to chat history
        st.session_state.messages.append(
            {"role": "assistant", "content": response_text}
        )

        return response_text
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return "Sorry, I encountered an error. Please try again."


# User input
user_input = st.chat_input("Say something...")

# Process user input
if user_input:
    with st.spinner("Thinking..."):
        response = generate_response(user_input)
        with st.chat_message("assistant"):
            st.write(response)
