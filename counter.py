from collections import Counter
class MessageCounter:
    def __init__(self): # inicializuji prázdný slovník (counter())
        # self.count = 1
        # self.inventory = {}
        self.c = Counter()
    def add_to_dict(self, can_messages):
        self.can_messages = can_messages
        self.c.update([can_messages]) #přidání zprávy do slovníku self.c (pokud se stejná zpráva vyskytuje tak inkrementuje value)

    @property
    def get_counter_list(self): #metoda, která vrací slovník (key:'CAN zpráva' , value: 'počet výskytů zprávy')
        return self.c
