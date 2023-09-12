from dotenv import load_dotenv
import os

load_dotenv()

my_host = os.getenv("DB_HOST")
my_user = os.getenv("DB_USER")
my_password = os.getenv("DB_PASSWORD")
my_port = os.getenv("DB_PORT")
my_db_name = os.getenv("DB_NAME")


def myEnvironment() -> None:
    load_dotenv()


if __name__ == "__main__":
    myEnvironment()
