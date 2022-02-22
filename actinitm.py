from bddrs import *
from random import randint
import socket
from time import sleep
import threading

item_counter = 0


class AuctionItem:
    def __init__(self, price, name=None):
        print("ITEM CREATED!")
        self.name, self.base_price = name, price

        if self.name is None:
            global item_counter
            self.name = f"ITEM_{item_counter}"
            item_counter += 1


class Auction:
    def __init__(self, thing, bid_increment=10, time=60):
        self.bids = 0
        self.time = time
        self.auction_done = False
        self.item_name = thing.name
        self.base_price = thing.price
        self.bid_increment = bid_increment
        self.address = ('localhost', randint(60000, 65000))
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.address)

    def increase_bid(self, bid=None):
        self.bids += 1
        self.item.price += (self.bid_increment / 100) * self.bid if bid is None else bid

    def timeout(self):
        sleep(self.time)
        self.auction_done = True

    def listen_bidders(self):
        """starts listening to the bidders"""
        self.server.listen()  # server starts to listen for connections

        while self.auction_done is False:  # the value of auction_done is True when the time's out for the program.
            client, address = self.server.accept()
            client_thread = threading.Thread(target=handle_client, args=(client,))
            name = client.recv(1024).decode(FORMAT)

    def start(self):
        timeout = threading.Thread(target=self.timeout)
        timeout.start()

        while True:
            if self.auction_done:
                break
            else:
                (threading.Thread(target=self.listen_bidders)).start()


if __name__ == "__main__":
    item = AuctionItem(name="WATCH", base_price=86)
    print("item created")
    action = Auction(item, 2, 10)
    print("auction created")
    action.start()
