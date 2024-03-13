from dotenv import load_dotenv
import os

load_dotenv()

ENTRENAMIENTOS_URL = os.environ.get("ENTRENAMIENTOS_URL")
DATABASE_URL = os.environ.get("DATABASE_URL")
QUEUE_URL = os.environ.get("QUEUE_URL")
FLASK_PORT = os.environ.get("FLASK_PORT")
FLASK_DEBUG = os.environ.get("FLASK_DEBUG") == "True" or os.environ.get("FLASK_DEBUG") == "true"
