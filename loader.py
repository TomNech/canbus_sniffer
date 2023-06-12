class Loader:
    def __init__(self, file_stream):
        self.file = file_stream
        self.data = []

    def __str__(self):
        return f"Soubor TXT má {len(self.data)} řádků\n"

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
