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


class Auction:
    def __init__(self, thing, port, bid_increment=10, dur=60):
        self.bids = 0
        self.duration = dur
        self.auction_done = False
        self.item = thing
        self.item_name = thing.name
        self.base_price = thing.price
        self.clients = {}  # contains all the client's data
        self.bid_increment = bid_increment
        self.address = ('localhost', port)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.address)

    def increase_bid(self, bid=None):
        self.bids += 1
        self.item.price += (self.bid_increment / 100) * self.item.price if bid is None else bid

    def timeout(self):
        for seconds in range(self.duration):
            sleep(1)

        self.auction_done = True

    def listen_bidders(self):
        """starts listening to the bidders"""
        self.server.listen()  # server starts to listen for connections

        while self.auction_done is False:  # the value of auction_done is True when the time's out for the program.
            client, address = self.server.accept()
            self.clients[address] = [client]
            client_thread = threading.Thread(target=handle_client, args=(client,))
            client_thread.start()

    def send(self, message, address="*"):
        if address == "*":
            for data in self.clients:
                client = data[0]
                client.send(bytes(message, FORMAT))
        else:
            if (type(message) == bool) or (type(message) is None):
                self.clients[address][0].send(bytes(messages[message], FORMAT))
            else:
                self.clients[address][0].send(bytes(message, FORMAT))

    def start(self):
        timeout = threading.Thread(target=self.timeout)
        timeout.start()

        while self.auction_done is False:
            self.listen_bidders()

        timeout.join()


if __name__ == "__main__":
    item = AuctionItem(name="WATCH", price=86)
    print("item created")
    action = Auction(item, 60000, 2, 60)
    print("auction created")
    action.start()
