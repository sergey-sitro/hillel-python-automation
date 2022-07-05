from HW18.proxy_pattern.abstract_reader import Reader
from HW18.proxy_pattern.txt_reader import TxtReader
from HW18.proxy_pattern.txt_writer import TxtWriter


class TxtProxyReader(Reader):
    def __init__(self, txt_reader: TxtReader, txt_writer: TxtWriter):
        self.__result = ''
        self.__is_actual = False
        self.__reader = txt_reader
        self.__writer = txt_writer

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read_file()
            self.__is_actual = True
            return self.__result

    def write_file(self, new_data):
        self.__result = self.__writer.write_file(new_data)
        self.__is_actual = False
        self.__result = self.__reader.read_file()
        return self.__result

    def update_actual_status(self, status):
        self.__is_actual = status
