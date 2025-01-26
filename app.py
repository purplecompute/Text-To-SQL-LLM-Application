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
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
 ]
 
 # Streamlit App
 
st.set_page_config(page_title="I can retrieve any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question") 

# If submit is clicked
if submit:
    if question is None or question == "":
        st.error("Please enter a question")
        exit()
    else: 
        response = get_gemini_response(question, prompt)
        print(response)
        data = read_sql_query(response, "student.db")
        st.subheader("The response is")
        for row in data:
            print(row)
            st.header(row)

# Add developer information at the bottom
st.markdown("""
    <div style='text-align: center; margin-top: 50px;'>
        <p>
            <img src='https://raw.githubusercontent.com/purplecompute/Media/Multi-Language-Invoice-Data-Extractor-Using-LLM/master/Media/sparkling_ai_icon.png' alt='Sparkling AI logo' width='17' style='vertical-align: middle;' />
            Developed By: Mayur Satao
        </p>
        <p>
            <a href='https://github.com/purplecompute' target='_blank'>
                <img src='https://raw.githubusercontent.com/purplecompute/Media/Multi-Language-Invoice-Data-Extractor-Using-LLM/master/Media/github_icon.png' alt='GitHub logo' width='30' style='vertical-align: middle;' />
            </a>
            <a href='https://www.linkedin.com/in/mayur-satao' target='_blank'>
                <img src='https://raw.githubusercontent.com/purplecompute/Media/Multi-Language-Invoice-Data-Extractor-Using-LLM/master/Media/linkedin_icon.png' alt='LinkedIn logo' width='30' style='vertical-align: middle;' />
            </a>
        </p>
    </div>
""", unsafe_allow_html=True)

