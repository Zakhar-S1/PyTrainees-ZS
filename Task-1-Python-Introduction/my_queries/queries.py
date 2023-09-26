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

GET_LIST_OF_ROOMS_AND_STUDENTS = """
SELECT Rooms.name, COUNT(*) AS Count_of_Students
FROM pyIntro.rooms Rooms JOIN pyIntro.students Students 
ON Rooms.id = Students.room
GROUP BY Rooms.name;
"""

AVG_AGE_OF_STUDENTS = """
SELECT Rooms.name, AVG(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), Students.birthday)), '%Y') + 0) AS Avg_age_of_Students
FROM pyIntro.students Students JOIN pyIntro.rooms Rooms 
ON Rooms.id = Students.room
GROUP BY Rooms.name
ORDER BY Avg_age_of_Students
LIMIT 5;
"""

DIFF_OF_AGE = """
SELECT Rooms.name, (MAX(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), Students.birthday)), '%Y') + 0) - MIN(DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), Students.birthday)), '%Y') + 0)) As Diff_of_age
FROM pyIntro.students Students JOIN pyIntro.rooms Rooms 
ON Rooms.id = Students.room
GROUP BY Rooms.name
ORDER BY Diff_of_age DESC
LIMIT 5;
"""

GET_ROOMS_ACCORDING_GENDER = """
SELECT Rooms.name
FROM pyIntro.students Students JOIN pyIntro.rooms Rooms 
ON Rooms.id = Students.room
Where Students.sex = 'M' AND Rooms.name IN (SELECT Rooms.name 
                                            FROM pyIntro.students Students JOIN pyIntro.rooms Rooms 
                                            ON Rooms.id = Students.room
                                            WHERE Students.sex = 'F')
GROUP BY Rooms.name;
"""