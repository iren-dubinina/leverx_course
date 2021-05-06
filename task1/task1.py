import json
from dict2xml import dict2xml


class JsonReader:
    """
        This class is used to read json files
    """

    def __init__(self, name):
        self.name = name

    def read(self):
        filename = input("Input path for input file {}: ".format(self.name))
        with open(filename) as json_file:
            data = json.load(json_file)
        return data
    



class Writer:
    """
        This class is used to write in files
    """
    def __init__(self):
        extension = input("Input extension for output file: ")
        self.extension = extension.strip()

    @staticmethod
    def write_json(self, data, file_name):
        with open(file_name, 'w') as outfile:
            json.dump(data, outfile)

    @staticmethod
    def write_xml(self, data, file_name):
        xml = dict2xml(result_list)
        with open(file_name, 'w') as outfile:
            outfile.write(xml)

    def write(self, data):
        try:
            output_file = "output.{}".format(self.extension)
            if self.extension == "json":
                self.write_json(self, data, output_file)
            elif self.extension == "xml":
                self.write_xml(self, data, output_file)
            else:
                raise TypeError("Invalid extension")
            print("Result saved in {}".format(output_file))
        except TypeError as t:
            print(t)
        except IOError as io:
            print(io)

            


if __name__ == "__main__":
    rooms_reader = JsonReader("rooms")
    rooms_list = rooms_reader.read()

    students_reader = JsonReader("students")
    students_list = students_reader.read()

    result_list = []
    for room in rooms_list:
        room_with_students = room
        students_in_room = [student for student in students_list if student['room'] == room['id']]

        #         for student in students_list:
        #             if student['room'] == room['id']:
        #                 students_in_room.append(student)
        # ?               del(students_list[student])

        room_with_students['students'] = students_in_room
        result_list.append(room_with_students)

    data_writer = Writer()
    data_writer.write(result_list)
