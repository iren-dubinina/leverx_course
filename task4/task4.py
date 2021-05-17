import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Sparina',
    charset='utf8mb4',
)


def db_create():
    # создание БД
    with connection.cursor() as cursor:
        query = "create database if not exists task4"

        # создание таблиц
        query = """create table if not exists task4.Rooms(
                     id integer,
                     name varchar(10), 
                     primary key (id))
                """
        cursor.execute(query)

        query = """create table if not exists task4.Students(
                     id integer,
                     name varchar(50) Not Null, 
                     birthday date,
                     room integer,
                     sex varchar(1),
                     primary key (id),
                     foreign key (id) references Rooms(id))
                """
        cursor.execute(query)


def main():
    db_create()
    connection.close()


if __name__ == '__main__':
    main()

#     #connection.commit()
#     #connection.fetchall
