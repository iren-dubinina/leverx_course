import json
from typing import List, Any
from dict2xml import dict2xml
from decimal import Decimal
import argparse


class JsonReader:
    """
        This class is used to read json files
    """
    def __init__(self, filename) -> object:
        self.filename = filename

    def read(self):
        with open(self.filename) as json_file:
            data = json.load(json_file)
        return data


class JSWriter:
    def write_in_file(self, filename, data):
        with open(f"{filename}.json", 'w') as outfile:
            json.dump(data, outfile, ensure_ascii=False, default=str)


class XMLWriter:
    def write_in_file(self, filename, data):
        xml = dict2xml(data)
        with open(f"{filename}.xml", 'w') as outfile:
            outfile.write(xml)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Files to combine and save')
    parser.add_argument('--in_dir_rooms', type=str, default="rooms.json", help='Input path for file with rooms')
    parser.add_argument('--in_dir_students', type=str, default="students.json",
                        help='Input path for file with students')
    parser.add_argument('--extension', type=str, default="json", help='Input extension for output file')
    parser.add_argument('--out_file', type=str, default="outfile", help='Input name for output file')
    args = parser.parse_args()
    print(args)

    rooms_reader = JsonReader(args.in_dir_rooms)
    rooms_list = rooms_reader.read()

    students_reader = JsonReader(args.in_dir_students)
    students_list = students_reader.read()

    students_by_room = {}
    for student in students_list:
        room = student['room']
        if room not in students_by_room:
            students_by_room[room] = []
        students_by_room[room].append(student)

    for room in rooms_list:
        room['students'] = students_by_room[room['id']]

    if args.extension == "json":
        data_writer = JSWriter()
    elif args.extension == "xml":
        data_writer = XMLWriter()
    else:
        print('Such extension not supported')

    try:
        data_writer.write_in_file(args.out_file, rooms_list)
    except IOError as io:
        print('Error writing to file')
    else:
        print("Result saved in {}.{}".format(args.out_file, args.extension))
