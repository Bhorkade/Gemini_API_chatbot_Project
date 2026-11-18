# AI Chatbot using Streamlit & Gemini

## About the Project
This project is a simple AI chatbot built using Python, Streamlit, and Google's Gemini API. It allows users to enter prompts and receive AI-generated responses in an interactive chat interface.

## Features
- Interactive chat interface using Streamlit
- Google Gemini API integration
- Maintains chat history using `st.session_state`
- Accepts user prompts through `st.chat_input()`
- Displays user prompts and AI responses
- Simple and lightweight application

## Technologies Used
- Python
- Streamlit
- Google Gemini API (`google-genai`)
- Session State

## Project Workflow
1. User enters a prompt in the chat input.
2. The prompt is stored in the session history.
3. The prompt is sent to the Gemini model.
4. Gemini generates a response.
5. The response is stored in the session history.
6. Streamlit displays the conversation.

## Installation

### 1. Clone the repository
```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

### 2. Install dependencies
```bash
pip install streamlit google-genai
```

### 3. Set up your Gemini API key
Create a Google Gemini API key from Google AI Studio and configure it in your project.

### 4. Run the application
```bash
streamlit run main.py
```

## How It Works
The application uses Streamlit for the UI and Google's Gemini API to generate answers. The `st.session_state` variable stores the conversation history during the session, allowing previous prompts and responses to remain displayed.

## Future Improvements
- Add a clear chat option
- Display user and AI messages separately using chat message components
- Add secure API key management using environment variables
- Improve UI design
- Add error handling

## Author
Shrikar Bhorkade
