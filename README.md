# SQL LLM Project

This project is a Streamlit application that uses Google Generative AI to convert natural language questions into SQL queries and retrieve data from a SQLite database. The application allows users to input a question and get a response based on the content of the database.

## Features

- Load environment variables from a `.env` file
- Use Streamlit for the web interface
- Convert natural language questions to SQL queries using Google Generative AI
- Retrieve and display data from a SQLite database

## Video Demo

<img align="centre" alt="GIF" src="https://raw.githubusercontent.com/purplecompute/Multi-Language-Invoice-Data-Extractor-Using-LLM/master/Media/Invoice_Data_Extractor_Project_Demo.gif?raw=true" width="1200" height="550" />

## Requirements

- Python 3.x
- Streamlit
- Google Generative AI
- Python Dotenv

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/sql-llm-project.git
    cd sql-llm-project
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a [.env](http://_vscodecontentref_/1) file in the root directory and add your Google API key:
    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter a question in the input field and click the "Ask the question" button to get the SQL query response and data from the database.

## Project Structure

- [app.py](http://_vscodecontentref_/2): The main application file that contains the Streamlit app and the logic for interacting with Google Generative AI and the SQLite database.
- [sql.py](http://_vscodecontentref_/3): A script to set up the SQLite database and insert initial records.
- [requirements.txt](http://_vscodecontentref_/4): A list of Python packages required for the project.
- [.env](http://_vscodecontentref_/5): A file to store environment variables (not included in the repository).
- [.gitignore](http://_vscodecontentref_/6): A file specifying which files and directories to ignore in the repository.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.