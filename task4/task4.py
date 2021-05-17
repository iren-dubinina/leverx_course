from task1.task1 import JsonReader, JSWriter
from db import Database
import argparse
from queries import *


def main():
    db = Database()

    # Create db if not exists
    db.execute(create_db_query())
    db.select_database("task4")

    # Create tables if not exist
    db.execute(create_table_room_query())
    db.execute(create_table_students_query())

    # Parse tables
    parser = argparse.ArgumentParser(description='Files of rooms and students')
    parser.add_argument('--in_dir_rooms', type=str, default="rooms.json", help='Input path for file with rooms')
    parser.add_argument('--in_dir_students', type=str, default="students.json",
                        help='Input path for file with students')
    parser.add_argument('--extension', type=str, default="json", help='Input extension for output file')
    args = parser.parse_args()

    # Parse files
    rooms_reader = JsonReader(args.in_dir_rooms)
    rooms_list = rooms_reader.read()

    students_reader = JsonReader(args.in_dir_students)
    students_list = students_reader.read()

    # Insert values into tables
    for room in rooms_list:
        db.execute(insert_rooms_query(), room)

    db.commit()

    for student in students_list:
        db.execute(insert_students_query(), student)

    db.commit()

    # Create json writer to save results
    json_writer = JSWriter()

    # Query1 Select rooms with count of students
    result = db.query(rooms_count_students_query())
    json_writer.write_in_file("query1", result)

    # Query2 Select 5 rooms with min average ages
    result = db.query(min_avg_age_query())
    json_writer.write_in_file("query2", result)

    # Query3 Select 5 rooms with max difference of ages
    result = db.query(max_diff_age_query())
    json_writer.write_in_file("query3", result)

    # Query5 Select rooms with difference sex of students
    result = db.query(diff_sex_query())
    json_writer.write_in_file("query4", result)

    # Create index1 for Students table
    result = db.query(add_index1_query())

    # Create index2 for Students table
    result = db.query(add_index2_query())

    # Close connection
    db.close()


if __name__ == '__main__':
    main()
