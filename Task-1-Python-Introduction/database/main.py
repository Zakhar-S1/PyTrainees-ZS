from database import MySQLManager
from settings import my_host, my_user, my_password


def main():
    mydb = MySQLManager(host=my_host, user=my_user, password=my_password)
    mydb.close_connection()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
