import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    # Database configuration
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_SERVER = os.getenv('DB_SERVER')
    DB_NAME = os.getenv('DB_NAME')
    SQLALCHEMY_DATABASE_URI = (
        ff'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False