from collections import Counter
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
