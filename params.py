from dotenv import load_dotenv
from os import getenv as ge
load_dotenv()  # take environment variables from .env.
API_TOKEN = ge('API_TOKEN')
WORKSPACE_ID=ge("WORKSPACE_ID")
USER_ID=ge("USER_ID")