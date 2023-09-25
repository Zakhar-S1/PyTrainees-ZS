CREATE_SCHEMA = """
CREATE SCHEMA IF NOT EXISTS pyIntro; 
"""

SHOW_DB = """
SHOW DATABASES;
"""

USE_DB = """
USE pyIntro;
"""

SHOW_TBS = """
SHOW TABLES;
"""

CREATE_TB_ROOMS = """
CREATE TABLE IF NOT EXISTS pyIntro.rooms (id int PRIMARY KEY, name VARCHAR(50));
"""

CREATE_TB_STUDENTS = """
CREATE TABLE IF NOT EXISTS pyIntro.students (birthday DATE, id int, name VARCHAR(60), room int, sex CHAR(1), FOREIGN KEY (room) REFERENCES pyIntro.rooms(id) ON DELETE CASCADE);
"""

INSERT_DATA_INTO_TB_ROOMS = """
INSERT INTO pyIntro.rooms(id, name) VALUES(%s,%s);
"""

INSERT_DATA_INTO_TB_STUDENTS = """
INSERT INTO pyIntro.students(birthday, id, name, room, sex) VALUES(%s,%s,%s,%s,%s);
"""




