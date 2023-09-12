import json
import mysql_manager
import mysql.connector


def show_json_file():
    with open('/Users/zakhar/PyTrainees-ZS/Task-1-Python-Introduction/data/input/rooms.json', 'r') as f:
        data = json.load(f)

    print(data)


def insert_data_into_rooms_tb(data, con):
    cur = con.cursor()

    for item in data:
        sql = "INSERT INTO "


if __name__ == '__main__':
    show_json_file()
