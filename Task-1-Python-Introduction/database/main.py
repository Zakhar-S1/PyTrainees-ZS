import database
from settings import my_host, my_user, my_password


def main():
    mydb = database.MySQLManager(host=my_host, user=my_user, password=my_password)
    #mydb.create_db()
    mydb.show_db()
    mydb.close_connection()


# port="3306", db_name="testdb"

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
