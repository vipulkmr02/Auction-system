from bddrs import *
import socket
from time import sleep
import threading

item_counter = 0


class AuctionItem:
    def __init__(self, price, name=None):
        print("ITEM CREATED!")
        self.name, self.price = name, price

        if self.name is None:
            global item_counter
            self.name = f"ITEM_{item_counter}"
            item_counter += 1
