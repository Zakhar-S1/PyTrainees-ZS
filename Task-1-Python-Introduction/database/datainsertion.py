import json


def show_json_file():
    with open('/Users/zakhar/PyTrainees-ZS/Task-1-Python-Introduction/data/input/rooms.json', 'r') as f:
        data = json.load(f)

    print(data)


if __name__ == '__main__':
    show_json_file()
