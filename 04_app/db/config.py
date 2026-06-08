from sqlalchemy.orm import sessionmaker
from .connection import engine

# setup session
session_local = sessionmaker(autoflush=False, bind=engine)