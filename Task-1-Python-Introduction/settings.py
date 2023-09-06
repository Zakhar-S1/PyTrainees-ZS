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
    print(f'My id is: {my_host}.')
    print(f'My secret key is: {my_user}.')
    print(f'My secret key is: {my_password}.')
    print(f'My secret key is: {my_port}.')
    print(f'My secret key is: {my_db_name}.')


if __name__ == "__main__":
    myEnvironment()
