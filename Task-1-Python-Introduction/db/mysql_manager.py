import mysql.connector
import json

from my_queries import *


class MySQLManager:

    def __init__(self, host, user, password, namedb, path_for_rooms_file, path_for_students_file, port=3306):
        self.conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=namedb
        )
        self.my_cursor = self.conn.cursor()
        self.path_for_rooms_file = path_for_rooms_file
        self.path_for_students_file = path_for_students_file

    def create_schema(self):
        self.my_cursor.execute(USE_DB)
        self.my_cursor.execute(CREATE_SCHEMA)

    def create_tables(self):
        self.my_cursor.execute(CREATE_TB_ROOMS)
        self.my_cursor.execute(CREATE_TB_STUDENTS)

    def show_tables(self):
        self.my_cursor.execute(USE_DB)
        self.my_cursor.execute(SHOW_TBS)

        for tbs in self.my_cursor:
            print(tbs)

    def get_data_from_file(self, path):
        with open(path, 'r') as f:
            data = json.load(f)
        return data

    def insert_data_into_rooms_tb(self):
        data = self.get_data_from_file(self.path_for_rooms_file)
        data_for_insert = []
        for item in data:
            val = (item['id'], item['name'])
            data_for_insert.append(val)

        sql = INSERT_DATA_INTO_TB_ROOMS
        self.my_cursor.executemany(sql, data_for_insert)
        self.conn.commit()

    def insert_data_into_students_tb(self):
        data = self.get_data_from_file(self.path_for_students_file)
        data_for_insert = []
        for item in data:
            val = (item['birthday'], item['id'], item['name'], item['room'], item['sex'])
            data_for_insert.append(val)

        sql = INSERT_DATA_INTO_TB_STUDENTS
        self.my_cursor.executemany(sql, data_for_insert)
        self.conn.commit()

    def execute_select_query(self, query):

        result = []
        for i, item in enumerate(query):
            self.my_cursor.execute(item)
            result.append(self.my_cursor.fetchall())

        return result

        # self.my_cursor.execute(query, **kwargs)
        # return self.my_cursor.fetchall()

    def close_connection(self):
        self.conn.close()
