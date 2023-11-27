FROM python:3.9-slim

COPY . /python-super-introduction

WORKDIR /python-super-introduction

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "./main.py", "--path_for_rooms_file", "./data/input/rooms.json", "--path_for_students_file", "./data/input/students.json", "--format_of_export_file", "xml"]
