from database import MySQLManager
from settings import my_host, my_user, my_password


class Application:

    def run_app(self) -> None:
        mydb = MySQLManager(host=my_host, user=my_user, password=my_password)
        mydb.close_connection()


