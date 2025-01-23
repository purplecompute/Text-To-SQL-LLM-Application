from dotenv import load_dotenv
load_dotenv()    # Load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
# Configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the google gemini model and provide sql query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    combined_input = f"{prompt}\n{question}"
    response = model.generate_content(combined_input)
    return response.text

# Function to retieve query from sql databse
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# Define your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query! The SQL database has the name STUDENT and table named STUDENTS and has the following columns - Name, Class, Section and Marks. \n\n For example, \n Example 1 - How many entries of records are present ? The SQL command will be something like this SELECT COUNT(*) FROM STUDENTS;, \n Example 2 - Tell me all the students studying in Data Science class?, the SQL command will be something like this SELECT * FROM STUDENTS WHERE Class="Data Science";
    also the SQL code should not have ｀｀｀ in beginning or end and SQL word in the output
    """
 ]
 
 # Streamlit App
 
st.set_page_config(page_title="I can retrieve any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question") 

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "student.db")
    st.subheader("The response is")
    for row in data:
        print(row)
        st.header(row)



