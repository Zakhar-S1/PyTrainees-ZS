import mysql.connector
import json

from settings import PATH_TO_ROOMS_FILE, PATH_TO_STUDENTS_FILE
from my_queries import *


def get_data_from_file(path):
    with open(path, 'r') as f:
        data = json.load(f)
        print(data)
    return data


class MySQLManager:

    def __init__(self, host, user, password):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.my_cursor = self.conn.cursor()

    # def select(self, query, **kwargs):
    #     return self.my_cursor.execute(query, **kwargs)

    def create_schema(self):
        self.my_cursor.execute(CREATE_SCHEMA)
        self.my_cursor.execute(USE_DB)

    def create_tables(self):
        self.my_cursor.execute(CREATE_TB_ROOMS)
        self.my_cursor.execute(CREATE_TB_STUDENTS)

    def show_tables(self):
        self.my_cursor.execute(USE_DB)
        self.my_cursor.execute(SHOW_TBS)

        for tbs in self.my_cursor:
            print(tbs)

    def insert_data_into_rooms_tb(self):
        data = get_data_from_file(PATH_TO_ROOMS_FILE)
        data_for_insert = []
        for item in data:
            val = (item['id'], item['name'])
            data_for_insert.append(val)

        sql = INSERT_DATA_INTO_TB_ROOMS
        self.my_cursor.executemany(sql, data_for_insert)
        self.conn.commit()

    def insert_data_into_students_tb(self):
        data = get_data_from_file(PATH_TO_STUDENTS_FILE)
        data_for_insert = []
        for item in data:
            val = (item['birthday'], item['id'], item['name'], item['room'], item['sex'])
            data_for_insert.append(val)

        sql = INSERT_DATA_INTO_TB_STUDENTS
        self.my_cursor.executemany(sql, data_for_insert)
        self.conn.commit()

    def execute_select_query(self, query, **kwargs):

        result = []
        for i, item in enumerate(query):
            self.my_cursor.execute(item, **kwargs)
            result.append(self.my_cursor.fetchall())

        return result

        # self.my_cursor.execute(query, **kwargs)
        # return self.my_cursor.fetchall()

    def close_connection(self):
        self.conn.close()
