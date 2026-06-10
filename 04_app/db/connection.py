import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import streamlit as st

load_dotenv()

# get cloud credentials
try:
    get_user = st.secrets["DB_USER"]
    get_password = st.secrets["DB_PASSWORD"]
    get_host = st.secrets["DB_HOST"]
    get_port = st.secrets["DB_PORT"]
    get_db = st.secrets["DB_NAME"]
except Exception:
    get_user = os.getenv('DB_USER')
    get_password = os.getenv('DB_PASSWORD')
    get_host = os.getenv('DB_HOST')
    get_port = os.getenv('DB_PORT')
    get_db = os.getenv('DB_NAME')

# dynamically construct the database URL
database_url = f"mysql+pymysql://{get_user}:{get_password}@{get_host}:{get_port}/{get_db}"

# Database connection
try:
    engine = create_engine(
        database_url, 
        connect_args={"ssl": {}}, 
        echo=True
    )
    print('successful connection to the database')

except Exception as e:
    print(f'ERROR: {e}')
