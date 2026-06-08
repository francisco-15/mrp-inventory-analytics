from sqlalchemy import create_engine
import os
from dotenv import load_dotenv



# database URL 
load_dotenv()
get_user = os.getenv('user')
get_password = os.getenv('db_password')
database_url = f"mysql+pymysql://{get_user}:{get_password}@localhost:3306/mrp_movements"


# connection database
try:
    engine = create_engine(database_url, echo=True)
    print('successful connection to the database')

except Exception as e:
    print(f'ERROR: {e}') 
