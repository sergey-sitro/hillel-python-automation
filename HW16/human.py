import json
from dict2xml import dict2xml
from argparse import ArgumentParser


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        with open("converted_json.json", "w") as json_file:
            json_file.write(json.dumps(self.__dict__))

    def convert_to_xml(self):
        data = self.__dict__
        xml = dict2xml(data)

        with open("converted_xml.xml", "w") as xml_file:
            xml_file.write(xml)


human = Human("John", 27, "male", 1994)

parser = ArgumentParser(description='Choose which file to convert')

default = 'json'
parser.add_argument('--format', help='Format to convert', default=default)
args = parser.parse_args()

if args.format == "json":
    human.convert_to_json()

elif args.format == "xml":
    human.convert_to_xml()
