class Loader:
    def __init__(self, file_stream):
        self.file = file_stream
        self.data = [] #inicializuji prázdný list pro načtení zpráv

    def __str__(self):
        return f"Soubor TXT má {len(self.data)} řádků\n" #vrací délku listu pro informaci kolik má textový soubor řádků

    def __len__(self):
        return len(self.data) #magická metoda pro délku listu

    def load_file(self): #metoda pro načtení souboru

        try:
            with open(self.file) as f: #otevře textový soubor jako 'f'
                for x in f:
                    self.data.append(x.strip()) #přidá všechny řádky do listu z textového souboru, bez bílých znaků
        except FileNotFoundError:
            print("Neplatná cesta k souboru") #pokud není soubor nalezen vyhodí hlášku (argparse)

    def get_data(self, line_number): #metoda, která vrací řádek z listu
        return self.data[line_number]
