import configparser
import os

abs_path = os.path.abspath(fr"/Users/sergeymatkobozhyk/Desktop/Hillel/Hillel Project/Homework/hillel-python-automation/HW22/configurations/configuration.ini")
config = configparser.RawConfigParser()
config.read(abs_path)


def get_db_name():
    return config.get('db_info', 'db_name')
