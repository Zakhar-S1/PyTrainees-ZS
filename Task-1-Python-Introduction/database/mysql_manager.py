import mysql.connector


class MySQLManager:

    def __init__(self, host, user, password):
        self.conn = None
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

    # self.conn = mysql.connector.connect(host="localhost", user="root", password="1230321!", database="testdb")

    def create_db(self):
        my_cursor = self.conn.cursor()
        my_cursor.execute("CREATE DATABASE testdb")

    def create_table(self):
        pass

    def input_data_into_db(self):
        pass





    def show_db(self):
        my_cursor = self.conn.cursor()
        my_cursor.execute("SHOW DATABASES")

        for db in my_cursor:
            print(db)

    def close_connection(self):
        self.conn.close()
