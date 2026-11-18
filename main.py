import streamlit as st
import os
from google import genai

client = genai.Client(
    api_key= "AIzaSyA-jMGURQOe63yDDD7p6DRsNm0tDAqsas0"
)

if "history" not in st.session_state:
    st.session_state.history = []

prompt = st.chat_input("Prompt")

if prompt:
    st.session_state.history.append(prompt)

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    res = response.text
    st.session_state.history.append(res)

for msg in st.session_state.history:
    st.write(msg)