import sqlite3
from collections import Counter
import argparse
import sys

# pip install pdoc (python doc)
# pdoc ./my_project.py (spustíme pro daný soubor)

class Loader:
    def __init__(self, file_stream):
        self.file = file_stream
        self.data = []

    def __str__(self):
        return f"Soubor .txt má {len(self.data)} řádků (zpráv)\n"

    def __len__(self):
        return len(self.data)

    def load_file(self):

        try:
            with open(self.file) as f:
                for x in f:
                    self.data.append(x.strip())
        except FileNotFoundError:
            print("Neplatná cesta k souboru")

    def get_data(self, line_number):
        return self.data[line_number]


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


class MessageCounter:
    def __init__(self):
        # self.count = 1
        # self.inventory = {}
        self.c = Counter()

    def add_to_dict(self, can_messages):
        self.can_messages = can_messages
        self.c.update([can_messages])

    @property
    def get_counter_list(self):
        return self.c


class SQLite:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.create_table()

    def create_table(self):
        self.sql = '''
        CREATE TABLE IF NOT EXISTS CAN_messages (
            id INTEGER,
            data_length INTEGER,
            data TEXT
        )
        '''
        self.conn.execute(self.sql)
        self.conn.commit()

    def insert_message(self, id, data_len, data):
        pass
        self.sql = '''
        INSERT INTO messages (id, data_length, data)
        VALUES (?, ?, ?)
        '''
        self.conn.execute()
        self.conn.commit()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog='Moje krásná aplikace',
        description='Umím parsovat CAN zprávy',
        epilog='Celé jsem to napsal sám')

    parser.add_argument('-f', '--filename', help="Zadej název souboru")
    parser.add_argument('-db', '--database', help="Zadej název souboru")
    args = parser.parse_args()
    loader = Loader(args.filename)
    loader.load_file()
    # parser = Parser()
    dictionary = MessageCounter()

    for index in range(len(loader)):
        dictionary.add_to_dict(loader.get_data(index))

    def all_msg():

        num = 0
        # for a in range(13):
        #     parser.parse_line(loader.get_data(a))
        #     parser.data

        print(f"Zjištěné CAN_BUS zprávy: {loader}")

        # print(dictionary.get_counter_list.items())

        for key, value in dictionary.get_counter_list.items():
            num += 1
            print(f" {num}.\t CAN zpráva: {key} --> POČET: {value}")
        print()


    def filter_key_msg():

        filter_msg = {}
        num = 0
        can_id = str(input("Zadejte ID CAN zprávy: \n"))

        for key, value in dictionary.get_counter_list.items():
            if key.startswith(can_id):
                filter_msg.update({key: value})

        for key, value in filter_msg.items():
            num += 1
            print(f"{num}.\t CAN zpráva: {key} \t POČET: {value}")
        print()
        # database = SQLite(args.database)
        # database.create_table()


    def filter_value_msg():
        filter_msg = {}
        num = 0
        can_num = int(input("Zadejte počet výskytů CAN zprávy: "))

        # print(dictionary.get_counter_list.items())

        for key, value in dictionary.get_counter_list.items():
            if value == can_num:
                filter_msg.update({key: value})

        for key, value in filter_msg.items():
            num += 1
            print(f"{num}.\t CAN zpráva: {key} \t POČET: {value}")
        print()


    def filter_range_value():
        filter_msg = {}
        num = 0

        can_num_1 = int(input("Zadejte první číslo: "))
        can_num_2 = int(input("Zadejte druhé číslo: "))

        for key, value in dictionary.get_counter_list.items():

            if can_num_1 <= value <= can_num_2 or value <= can_num_1 and value >= can_num_2:
                filter_msg.update({key: value})

        for key, value in filter_msg.items():
            num += 1
            print(f"{num}.\t CAN zpráva: {key} \t POČET: {value}")
        print()

    def end():
        sys.exit("Program ukončen")


    while True:
        try:
            print(loader)
            print("1 - Zobrazit všechny nalezené zprávy")
            print("2 - Zobrazit seznam podle vybraného ID CAN zprávy")
            print("3 - Zobrazit seznam podle počtu výskytů CAN zprávy")
            print("4 - Zobrazit seznam podle rozsahu výskytů CAN zprávy")
            print("5 - Ukončit program")
            print("--------------------------------------------------")

            choice = int(input("Zadejte volbu: "))

            if choice == 1:
                all_msg()

            elif choice == 2:
                filter_key_msg()

            elif choice == 3:
                filter_value_msg()

            elif choice == 4:
                filter_range_value()

            elif choice == 5:
                end()

            else:
                print("Volba neexistuje\n")

        except:
            print("Chyba! Zadejte volbu.")
