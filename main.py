import argparse
import sys
from loader import Loader
from parser import Parser
from counter import MessageCounter

if __name__ == '__main__': #spuštění hlavní funkce

    parser = argparse.ArgumentParser(
        prog='CAN_MONITOR',
        description='MONITOR_CAN_MESSAGE',
        epilog='')

    parser.add_argument('-f', '--filename', help="Zadej název souboru")
    # parser.add_argument('-db', '--database', help="Zadej název souboru") zatím nepoužito pro databázy SQlite
    args = parser.parse_args()
    loader = Loader(args.filename) #vytvoření instance třídy Loader (posíláme textový soubor)
    loader.load_file() #instance pro nahrání souboru pomocí třídy Loader
    parser = Parser() #vytvoření instance třídy Parser (argparse)
    dictionary = MessageCounter() #vytvoření instance třídy MessageCounter
    # database = SQLite(args.database) # zatím nepoužito pro databázy SQlite

    for index in range(len(loader)): #projetí listu v délce instance
        dictionary.add_to_dict(loader.get_data(index)) #přidání instance loader do instance dictionary pomocí metody add_to_dict
        # parser.parse_line(loader.get_data(index))
        # data = parser.id
        # database.insert_data(data)

    def all_msg(): #funkce pro vypsání všech nalezených zpráv ve slovníku

        num = 0 #proměnná num

        print(f"Zjištěné CAN_BUS zprávy: {loader}")

        # print(dictionary.get_counter_list.items())

        for key, value in dictionary.get_counter_list.items():
            num += 1 #inkrementuje proměnnou num
            print(f" {num}.\t CAN zpráva: {key} --> POČET: {value}")
        print()


    def filter_key_msg(): #funkce pro vypsání všech zpráv podle ID CAN zprávy (první tři znaky zprávy)

        filter_msg = {} #pomocný slovník na 'vyfiltrované' zprávy
        num = 0 #proměnná num
        can_id = str(input("Zadejte ID CAN zprávy: \n")) #načtení ID CAN zprávy od uživatele

        for key, value in dictionary.get_counter_list.items():
            if key.startswith(can_id): #vyhledání ID pomocí metody startswith ve slovníku v KEY
                filter_msg.update({key: value}) #přidání CAN zprávy (KEY a VALUE) do pomocného slovníku

        for key, value in (sorted(filter_msg.items(), key=lambda item: item[1])): #lambda funkce pro seřazení CAN zpráv podle počtu výskytu (VALUE)
            num += 1 #inkrementuje proměnnou num
            print(f"{num}.\t CAN zpráva: {key} \t POČET: {value}") #vypíše v terminálu vyfiltrované zprávy ze slovníku
        print()

    def filter_value_msg(): #funkce pro vypsání všech zpráv podle počtu výskytů CAN zprávy
        filter_msg = {} #pomocný slovník pro 'vyfiltrované' zprávy
        num = 0 #proměnná num
        can_num = int(input("Zadejte počet výskytů CAN zprávy: ")) #načtení čísla počtu výskytů CAN zprávy od uživatele

        for key, value in dictionary.get_counter_list.items():
            if value == can_num: #vyhledání stejného čísla ve slovníku (VALUE)
                filter_msg.update({key: value}) #přidání CAN zprávy (KEY a VALUE) do pomocného slovníku

        for key, value in sorted(filter_msg.items()): #seřazený slovník
            num += 1 #inkrementuje proměnnou num
            print(f"{num}.\t CAN zpráva: {key} \t POČET: {value}") #vypíše v terminálu vyfiltrované zprávy ze slovníku
        print()


    def filter_range_value(): #funkce pro vypsání všech zpráv podle počtu výskytů CAN zprávy v rozsahu
        filter_msg = {} #pomocný slovník pro 'vyfiltrované' zprávy
        num = 0 #proměnná num

        can_num_1 = int(input("Zadejte první číslo: ")) #načtení prvního čísla počtu výskytů CAN zprávy od uživatele
        can_num_2 = int(input("Zadejte druhé číslo: ")) #načtení druhého čísla počtu výskytů CAN zprávy od uživatele

        for key, value in dictionary.get_counter_list.items():

            if can_num_1 >= value and can_num_2 <= value or can_num_1 <= value and can_num_2 >= value:
                filter_msg.update({key: value})

        for key, value in filter_msg.items():
            num += 1
            print(f"{num}.\t CAN zpráva: {key} \t POČET: {value}") #vypíše v terminálu vyfiltrované zprávy ze slovníku
        print()

    def end(): #funkce pro ukončení programu
        sys.exit("Program ukončen")


    while True:

        print(loader) #vypíše magickou metodu instance loader
        print("1 - Zobrazit všechny nalezené zprávy") #Vypsání volby pro vypsání všech CAN zpráv
        print("2 - Zobrazit seznam podle vybraného ID CAN zprávy") #Vypsání volby pro vypsání všech CAN zpráv podle ID
        print("3 - Zobrazit seznam podle počtu výskytů CAN zprávy") #Vypsání volby pro vypsání všech CAN zpráv podle počtu výskytů
        print("4 - Zobrazit seznam podle rozsahu výskytů CAN zprávy") #Vypsání volby pro vypsání všech CAN zpráv podle počtu výskytů v rozsahu
        print("5 - Ukončit program") #Vypsání volby pro ukončení programu
        print("--------------------------------------------------")

        choice = int(input("Zadejte volbu: ")) #načtení čísla pro zvolenou volbu

        if choice == 1:
            all_msg() #volání funkce all_msg

        elif choice == 2:
            filter_key_msg() #volání funkce filter_key_msg

        elif choice == 3:
            filter_value_msg() #volání funkce filter_value_msg

        elif choice == 4:
            filter_range_value() #volání funkce filter_range_value

        elif choice == 5:
            end() #volání funkce end

        else:
            print("Volba neexistuje\n")


