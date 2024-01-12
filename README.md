# English-To-SQL-To-Result
This is a streamlit app that generates SQL queries based on the user's input. The system needs to be given the database configuration and it generates the SQL query and the result both.

The app is based on Google's Gemini pro LLM. 

First, an SQLite database needs to be created using the createDB.py file. You can change the DB configuration, table details, data, etc. However, these details would be used in the prompt later on.
Next, in the file main.py, a prompt having the instructions, db configuration as well as examples is sent to Gemini pro. Gemini Pro generates a query and then that query is executed over the database to get the desired results.

The system is capable of generating queries for the most difficult of use cases provided the correct examples and db configuration are used.

It is also an example of few-shot learning.
