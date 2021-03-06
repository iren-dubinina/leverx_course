import time
import pandas as pd
from task1.task1 import JsonReader, JSWriter, XMLWriter
from db import Database
import argparse
from queries import *


def main():
    parser = argparse.ArgumentParser(description='Files of rooms and students')
    parser.add_argument('--in_dir_rooms', type=str, default="rooms.json", help='Input path for file with rooms')
    parser.add_argument('--in_dir_students', type=str, default="students.json",
                        help='Input path for file with students')
    parser.add_argument('--extension', type=str, default="json", help='Input extension for output file')
    parser.add_argument('--db_user', type=str, default="root", help='Input user for db')
    parser.add_argument('--db_password', type=str, default="", help='Input password for db')
    parser.add_argument('--db_name', type=str, default="task4", help='Input database name')
    args = parser.parse_args()

    db = Database(args.db_user, args.db_password)

    # Create db if not exists
    db.execute(create_db_query(args.db_name))
    db.select_database(args.db_name)

    # Create tables if not exist
    db.execute(create_table_room_query())
    db.execute(create_table_students_query())

    # Parse files
    rooms_reader = JsonReader(args.in_dir_rooms)
    rooms_list = rooms_reader.read()

    students_reader = JsonReader(args.in_dir_students)
    students_list = students_reader.read()

    # Insert values into tables
    db.executemany(insert_rooms_query(), rooms_list)
    db.executemany(insert_students_query(), students_list)

    # Create writer to save results
    writer = JSWriter()
    if args.extension == 'xml':
        writer = XMLWriter()

    timing_results = {
        "name": select_queries.keys(),
        "w/o": [],
        "w": []
    }

    for query_name in select_queries:
        start_time = time.time()
        result = db.query(select_queries[query_name]())
        end_time = time.time()
        writer.write_in_file(query_name, result)
        timing_results["w/o"].append(end_time - start_time)

    # Create index1 for Students table
    # result = db.query(add_index1_query())

    # Create index2 for Students table
    result = db.query(add_index2_query())

    for query_name in select_queries:
        start_time = time.time()
        result = db.query(select_queries[query_name]())
        end_time = time.time()
        writer.write_in_file(query_name, result)
        timing_results["w"].append(end_time - start_time)

    # Close connection
    db.close()

    # Print time results
    print(pd.DataFrame(timing_results))


if __name__ == '__main__':
    main()
