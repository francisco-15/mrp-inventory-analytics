import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import streamlit as st

load_dotenv()

# get cloud credentials
get_user = st.secrets.get("DB_USER", os.getenv("DB_USER"))
get_password = st.secrets.get("DB_PASSWORD", os.getenv("DB_PASSWORD"))
get_host = st.secrets.get("DB_HOST", os.getenv("DB_HOST"))
get_port = st.secrets.get("DB_PORT", os.getenv("DB_PORT"))
get_db = st.secrets.get("DB_NAME", os.getenv("DB_NAME"))

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
