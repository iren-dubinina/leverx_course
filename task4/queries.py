# Queries for Task4

def create_db_query(db_name):
    # Created db
    return f"create database if not exists {db_name}"


def create_table_room_query():
    # Created rooms table
    return """create table if not exists rooms(
                 id integer,
                 name varchar(10), 
                 primary key (id))
            """


def create_table_students_query():
    # Created students table
    return """create table if not exists students(
              id integer,
              name varchar(50) Not Null, 
              birthday datetime,
              room_id integer Not Null,
              sex varchar(1),
              primary key (id),
              foreign key (room_id) references Rooms(id))
            """


def insert_rooms_query():
    return "INSERT INTO rooms(id, name) VALUE (%(id)s, %(name)s)"


def insert_students_query():
    return "INSERT INTO students(id, name, birthday, room_id, sex) VALUE (%(id)s, %(name)s, %(birthday)s,%(room)s, %(sex)s)"


def rooms_count_students_query():
    return '''SELECT rooms.id, count(students.id)
              FROM rooms left join students
              ON rooms.id = students.room_id
              GROUP BY rooms.id'''


def min_avg_age_query():
    return '''SELECT rooms.id, avg(datediff(CURDATE(), students.birthday)) as Age
              FROM rooms join students
              ON rooms.id = students.room_id 
              GROUP BY rooms.id
              ORDER by Age ASC
              LIMIT 5'''


def max_diff_age_query():
    return '''SELECT rooms.id, datediff(max(students.birthday), min(students.birthday)) as Different 
              FROM rooms join students
              ON rooms.id = students.room_id 
              GROUP BY rooms.id
              ORDER by Different DESC
              LIMIT 5'''


def diff_sex_query():
    return '''SELECT rooms.id, count(DISTINCT students.sex) AS SexCount
              FROM rooms join students
              ON rooms.id = students.room_id
              GROUP BY rooms.id
              HAVING SexCount > 1'''


def add_index1_query():
    return '''CREATE index ByRoomID on students (room_id)'''


def add_index2_query():
    return '''CREATE index ByBirthday on students (room_id, birthday)'''