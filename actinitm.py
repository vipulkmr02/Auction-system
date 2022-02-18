import random as rand


class AuctionItem:
    def __init__(self, file_path, name=None):
        print("ITEM CREATED!")
        self.name, self.file_path = name, file_path

        if self.name is None:
            self.name = f"ITEM_{rand.random() * 100}"
