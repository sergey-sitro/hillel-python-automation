from HW18.proxy_pattern.abstract_writer import Writer


class TxtWriter(Writer):

    def __init__(self, file_name, new_data):
        self.file_name = file_name
        self.new_data = new_data

    def write_file(self, new_data):
        with open(self.file_name, "w") as file:
            text = file.write(new_data)
        return text
