class TxtReader:

    def __init__(self, file_name):
        self.file_name = file_name

    def write_file(self, new_data):
        with open(self.file_name) as file:
            text = file.write(new_data)
        return text
