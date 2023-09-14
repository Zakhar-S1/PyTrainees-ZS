import mysql.connector
import json


class MySQLManager:

    def __init__(self, host, user, password):
        self.conn = None
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )


    def create_db(self):
        my_cursor = self.conn.cursor()
        my_cursor.execute("CREATE DATABASE testdb;")

    def create_schema(self):
        my_cursor = self.conn.cursor()
        my_cursor.execute("CREATE SCHEMA IF NOT EXISTS pyIntro;")

    def create_tables(self):
        my_cursor = self.conn.cursor()
        my_cursor.execute("USE pyIntro;")
        my_cursor.execute("CREATE TABLE IF NOT EXISTS pyIntro.rooms (id int PRIMARY KEY, name VARCHAR(50));")
        my_cursor.execute(
            "CREATE TABLE IF NOT EXISTS pyIntro.students (birthday DATE, id int, name VARCHAR(60), room int, sex CHAR(1), FOREIGN KEY (room) REFERENCES pyIntro.rooms(id) ON DELETE CASCADE);")

    def insert_data_into_rooms_tb(self):
        my_cursor = self.conn.cursor()

        with open('/Users/zakhar/PyTrainees-ZS/Task-1-Python-Introduction/data/input/rooms.json', 'r') as f:
            data = json.load(f)

        for item in data:
            val = (item['id'], item['name'])
            sql = "INSERT INTO pyIntro.rooms(id, name) VALUES(%s,%s)"
            my_cursor.execute(sql, val)
            self.conn.commit()

    def insert_data_into_students_tb(self):
        my_cursor = self.conn.cursor()

        with open('/Users/zakhar/PyTrainees-ZS/Task-1-Python-Introduction/data/input/students.json', 'r') as f:
            data = json.load(f)

        for item in data:
            val = (item['birthday'], item['id'], item['name'], item['room'], item['sex'])
            sql = "INSERT INTO pyIntro.rooms(birthday, id, name, room, sex) VALUES(%s,%s)"
            my_cursor.execute(sql, val)
            self.conn.commit()

    def show_tables(self):
        my_cursor = self.conn.cursor()
        my_cursor.execute("USE pyIntro;")
        my_cursor.execute("SHOW TABLES")

        for tbs in my_cursor:
            print(tbs)

    def show_db(self):
        my_cursor = self.conn.cursor()
        my_cursor.execute("SHOW DATABASES")

        for db in my_cursor:
            print(db)

    def close_connection(self):
        self.conn.close()
