import streamlit as st
from dotenv import load_dotenv
import os
import sqlite3
import google.generativeai as genai
import pandas as pd

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
genai.GenerationConfig(temperature = 1)

model = genai.GenerativeModel("gemini-pro")
def get_response(prompt, question):
    response = model.generate_content([prompt, question])
    return response.text

def run_sql_query(query, db):
    connection = sqlite3.connect(db)
    df = pd.read_sql_query(query, connection)
    return df
    # cur = connection.cursor()
    # cur.execute(query)
    # rows = cur.fetchall()
    # for row in rows:
    #     print(row)
    # connection.commit()
    # connection.close()
    # return rows

def main():
    prompt = """
            INSTRUCTIONS:
            1. You are an expert in converting English questions to SQL queries. 
            2. The SQL database has two tables: student and department.
            3. The table student has columns: name, id, department_id, total_marks.
            4. The table department has columns: department_id, name, department_head.
            5. The table student has a foreign key to the table department, namely the column department_id.
            6. Provide suitable queries for the given questions based on the examples given.
            7. Also, the SQL code MUST NOT HAVE ``` or sql in the beginning or end in the output.

            EXAMPLES:
            1. Question: How many students are present?
               Query: SELECT * FROM student;
            2. Question: How many students are present in Aman's department?
               Query: SELECT COUNT(*) FROM student s JOIN department d ON s.department_id = d.department_id WHERE d.department_head = 'Minato';
            3. Question: Names of students who have scored less than 60 marks.
               Query: SELECT name FROM student WHERE total_marks < 60;
            4. Question: Tell me the name of students who are enrolled in the department headed by Madara and have less than 90 and greater than 80 marks
               Query: SELECT student.name FROM student JOIN department ON student.department_id = department.department_id WHERE department.department_head = 'Madara' AND student.total_marks < 90 AND student.total_marks > 80;
            """
    
    st.set_page_config(page_title="English To SQL")
    st.header("English to SQL to Result")
    st.info("Enter your English query and get a correct and ready to execute SQL query. Also get the results after executing that generated query")
    st.divider()
    st.subheader("Question")
    question = st.text_area("Question", help="Enter your question", placeholder="Enter the question", label_visibility="hidden")
    st.text("")
    submit = st.button("Convert", type="primary", use_container_width=True)
    st.divider()
    if question and submit:
        query = get_response(prompt, question)
        if query.startswith('Query:'):
            query = query.split(":")[1]
        st.subheader("Query")
        st.success(query)
        output = run_sql_query(query, "student.db")
        st.divider()
        st.subheader("Result")
        # for row in output:
        #     print(row)
        st.table(output)

    else:
        st.error("Write a suitable question") 

if __name__ == "__main__":
    main()
