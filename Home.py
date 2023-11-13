import streamlit as st

st.set_page_config(page_title="Efficiently.ai", page_icon="🌠")

st.title("Welcome to Efficiently.ai")
st.caption("🌠 Boost your efficiency to the next level!")
"💬 Customized Chatbot: easy export and language settings"
"🗂️ Summarize complex files and answer your questions"
"🎬 Summarize videos and answer your questions"
"🛜 What's on the webpage?"
"📊 Generate easy charts based on given data"


if "openai_api_key" not in st.session_state:
    st.session_state["openai_api_key"] = ""

openai_api_key = st.text_input(
    "Input your OpenAI API Key to start!", st.session_state["openai_api_key"])
submit = st.button("Submit")
if submit:
    st.session_state["openai_api_key"] = openai_api_key
    st.write("You have entered your key")
    with open('.env', 'w') as env_file:
        env_file.write(f'OPENAI_API_KEY={openai_api_key}\n')
