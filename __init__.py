from dotenv import load_dotenv, find_dotenv
from os import getenv
load_dotenv('.env.local', '.env')

DB_TYPE = getenv('DB_TYPE')
DB_PATH = getenv('DB_PATH')+getenv('DB_NAME')
