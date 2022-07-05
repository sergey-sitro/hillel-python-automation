from patterns_lesson.proxy_pattern.reader import Reader


class TxtReader(Reader):

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name) as file:
            text = file.read()
        return text
