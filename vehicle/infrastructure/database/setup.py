"""
This module contains the database setup for the vehicle application.
"""
import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

def is_running_with_alembic():
    """
    Check if the current process is running with Alembic.
    """
    return 'alembic' in sys.modules

# Load environment variables if running with Alembic
if is_running_with_alembic():
    load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """
    This function returns a session to the database.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
