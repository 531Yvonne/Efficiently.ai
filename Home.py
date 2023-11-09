import streamlit as st

st.set_page_config(page_title="Efficiently.ai", page_icon="🌠")

st.title("Welcome to Efficiently.ai\n where find efficiency to the next level!")

if "openai_api_key" not in st.session_state:
    st.session_state["openai_api_key"] = ""

openai_api_key = st.text_input(
    "Input your OpenAI API Key to start!", st.session_state["openai_api_key"])
submit = st.button("Submit")
if submit:
    st.session_state["openai_api_key"] = openai_api_key
    st.write("You have entered your key")
