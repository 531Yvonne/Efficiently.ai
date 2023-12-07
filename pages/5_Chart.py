import streamlit as st
import pandas as pd
import json
from pages.tools.process_csv import create_agent, get_response


st.title("📊 Chart Generator")
st.caption("🔎 Obtain insights and charts from csv datasets.")

file = st.file_uploader("Upload a CSV", type=["csv"])
query = st.text_input("Enter your request")
submit = st.button("Submit Query", type="primary")

if submit:
    agent = create_agent(file)
    response = get_response(agent, query)
    # Convert string response to actual dictionary
    dict_result = json.loads(response)

    # Response is a simple answer.
    if "answer" in dict_result:
        st.write(dict_result["answer"])

    # Response is a bar chart.
    if "bar" in dict_result:
        data = dict_result["bar"]
        df = pd.DataFrame(data)
        df.set_index("columns", inplace=True)
        st.bar_chart(df)

    # Response is a line chart.
    if "line" in dict_result:
        data = dict_result["line"]
        df = pd.DataFrame(data)
        df.set_index("columns", inplace=True)
        st.line_chart(data=df)

    # Response is a table.
    if "table" in dict_result:
        data = dict_result["table"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        st.table(df)
