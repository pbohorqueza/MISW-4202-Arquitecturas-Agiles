from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
FLASK_PORT = os.environ.get("FLASK_PORT")
FLASK_DEBUG = os.environ.get("FLASK_DEBUG") == "True" or os.environ.get("FLASK_DEBUG") == "true"
AIM_URL = os.environ.get("AIM_URL")
