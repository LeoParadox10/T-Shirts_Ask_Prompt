import os
import streamlit as st
from langchain_main import get_few_shots_db_chain

st.title("AtliQ T Shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_few_shots_db_chain()
    answer = chain.invoke(question)['result']
    st.header("Answer")
    st.write(answer)

# Path to the SQL file
sql_file_path = os.path.join(os.path.dirname(
    __file__), 'database', 'db_creation_atliq_t_shirts.sql')

# Read and display the content of the existing SQL file
try:
    with open(sql_file_path, "r") as file:
        sql_file_content = file.read()

    # Display the contents of the SQL file
    st.header("Existing SQL File Content")
    st.text_area("SQL File Content", sql_file_content, height=300)
except FileNotFoundError:
    st.error(
        f"The SQL file 'db_creation_atliq_t_shirts.sql' was not found in the 'database' folder.")
