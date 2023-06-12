import sqlite3
import argparse
import sys
from loader import Loader
from parser import Parser
from counter import MessageCounter
from database import SQLite


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
    parser = Parser()
    dictionary = MessageCounter()
    # database = SQLite(args.database)

    for index in range(len(loader)):
        dictionary.add_to_dict(loader.get_data(index))
        # parser.parse_line(loader.get_data(index))
        # data = parser.id
        # database.insert_data(data)

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

            if can_num_1 >= value and can_num_2 <= value or can_num_1 <= value and can_num_2 >= value:
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
