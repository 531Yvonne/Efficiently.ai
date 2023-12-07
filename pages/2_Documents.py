import streamlit as st
import tempfile
from pages.tools.extract_file import extract_file
from pages.tools.qa_chain import get_response
from pages.tools.moderation import moderate_text

st.title("🗂️ Documents Analyzer")
st.caption("🔎 Summary and Q&A powered by unstructured.io")

uploads = st.file_uploader(label='Upload documents',
                           type=['docx', 'doc', 'odt', 'pptx', 'ppt',
                                 'xlsx', 'csv', 'tsv', 'eml', 'msg',
                                 'rtf', 'epub', 'html', 'xml', 'pdf',
                                 'png', 'jpg', 'txt'],
                           accept_multiple_files=True)

extracted_result = ""
if uploads:
    for f in uploads:
        file_name, extension = f.name, f.name.split('.')[-1]
        # Save the uploaded file to temp file in order to run unstructured.io
        with tempfile.NamedTemporaryFile(delete=False,
                                         suffix=f".{extension}")as temp_file:
            temp_file.write(f.read())
        with st.spinner("Extracting documents...⏳"):
            try:
                texts = extract_file(temp_file.name)
                extracted_result += texts
            except Exception as e:
                st.error(f"Failed to process documents: {e}")
    with st.expander("See Extracted Text"):
        st.write(extracted_result)

query = st.text_input("Your question:")
submit = st.button("Submit")

if submit:
    if not uploads:
        st.info("Upload file(s) to start your query!")
    else:
        # Add Moderation Layer for Responsible AI purpose
        screening_result = moderate_text(query)
        if screening_result["flag"]:
            st.info(f'''Unable to finish your query. Your query contains:
                    {screening_result['content']} content''')
        else:
            response = get_response(extracted_result, query, flag="document")
            if 'Answer' in response:
                st.write('Answer:', response['Answer'])
            else:
                st.info("Failure --- some error occured")
