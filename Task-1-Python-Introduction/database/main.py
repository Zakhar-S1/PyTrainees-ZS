from database import MySQLManager
from my_queries.queries import QUERIES
from settings import my_host, my_user, my_password


def main():
    mydb = MySQLManager(host=my_host, user=my_user, password=my_password)

    # for i, item in enumerate(QUERIES):
    #     data_from_db = mydb.get_data(item)
    #     print(data_from_db)

    data_from_db = mydb.get_data(QUERIES)

    for i, item in enumerate(data_from_db):
        print(item)



    mydb.close_connection()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
