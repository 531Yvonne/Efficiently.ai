import streamlit as st
from pages.tools.extract_video import extract_video
from pages.tools.qa_chain import get_response
from pages.tools.moderation import moderate_text

st.title("🎬 Youtube Video Analyzer")
st.caption("🔎 Summarize youtube videos and answer your questions")

# Multiple URLs input using text_area
urls_input = st.text_area("Enter Youtube Video URL(s) (one per line):")

# Convert the newline-separated string to a list of URLs
urls = [url.strip() for url in urls_input.split('\n') if url.strip()]

query = st.text_input("Your question:")
submit = st.button("Submit")

if submit:
    if not urls:
        st.info("Enter url(s) to start your query!")
    else:
        # Add Moderation Layer for Responsible AI purpose
        screening_result = moderate_text(query)
        if screening_result["flag"]:
            st.info(f'''Unable to finish your query. Your query contains:
                    {screening_result['content']} content''')
        else:
            with st.spinner("Watching videos...⏳"):
                try:
                    extracted_result = extract_video(urls)
                except Exception as e:
                    st.error(f"Failed to process videos: {e}")

            response = get_response(extracted_result, query, flag="video")
            if 'Answer' in response:
                st.write('Answer:', response['Answer'])
            else:
                st.info("Failure --- some error occured")
