from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DBNAME = os.getenv("DBNAME")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
