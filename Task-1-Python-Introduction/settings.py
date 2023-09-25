from dotenv import load_dotenv
import os

PATH_TO_ROOMS_FILE = "/Users/zakhar/PyTrainees-ZS/Task-1-Python-Introduction/data/input/rooms.json"
PATH_TO_STUDENTS_FILE = "/Users/zakhar/PyTrainees-ZS/Task-1-Python-Introduction/data/input/students.json"

load_dotenv()

my_host = os.getenv("DB_HOST")
my_user = os.getenv("DB_USER")
my_password = os.getenv("DB_PASSWORD")
my_port = os.getenv("DB_PORT")
my_db_name = os.getenv("DB_NAME")
