
class Parser:
    def __init__(self):
        self.id = 0
        self.data_length = 0
        self.data = ""

    def parse_line(self, line):
        temporary = line.split()
        self.id = str(temporary[0])
        self.data_length = int(temporary[1])
        self.data = temporary[2:]

    @property
    def get_id(self):
        return self.id

    @property
    def get_data_length(self):
        return self.data_length

    @property
    def get_data(self):
        return self.data

    def __str__(self):
        return f"ID: {self.get_id}, DATA LEN: {self.get_data_length}, DATA: {self.get_data}"
