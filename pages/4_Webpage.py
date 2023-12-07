import streamlit as st
from pages.tools.process_web import fetch_webcontent, analyze_content

st.title("🛜 Web Browsing")
st.caption("🔎 What's on the webpage?")

url = st.text_input("Enter the website URL:")
summarize = st.button("Summarize!")

if url and summarize:
    st.write(f"You entered: {url}")

    with st.spinner("Scanning webpage...⏳"):
        try:
            content = fetch_webcontent(url)
            if content:
                result = analyze_content(content)
                st.subheader("Summary:")
                st.write(result)
            else:
                st.error("Unable to access this webpage")
        except Exception as e:
            st.error(f"Failed to process this request: {e}")
