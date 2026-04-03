from dotenv import load_dotenv
import os

# Read values from .env once.
load_dotenv()

class Settings:
    # Store all database settings in one place.
    def __init__(self):
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_name = os.getenv("DB_NAME")

# Create one settings object that other files can import.
settings = Settings()