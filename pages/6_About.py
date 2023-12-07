import streamlit as st
from pages.tools.generate_quote import write_quote

st.title("ℹ️ About")

"🔋 Powered by [OpenAI API](https://platform.openai.com/docs/introduction), [OpenAIWhisper](https://openai.com/research/whisper), [unstructured.io](https://unstructured.io), [LangChain](https://www.langchain.com), [Streamlit](https://streamlit.io)"
"📚 Knowledge and Techniques from Generative AI class at the University of Chicago"
"🧑‍💻 Designed and Implemented by [Yves Yang](https://www.yvesyang.com)"

with st.spinner("Loading...⏳"):
    st.write("📝", write_quote())
