import datetime
import socket
import threading
from time import sleep
from common import *


class Auction:
    def __init__(self,
                 item,
                 currency="INR",
                 addr=("localhost", 60000),
                 bid_increment=10,
                 duration=200
                 ):
        """
        parameters
                 item,
                 currency="INR",
                 addr=("localhost", 60000),
                 bid_increment=10,
                 duration=200
        """
        self.winner = ""

        # item variables
        self.item = item
        self.item_name = item.name
        self.base_price = item.price

        # auction variables
        self.type = type
        self.time_left = 0
        self.bids = 0
        self.hammer_price = self.base_price
        self.highest_bidder = ""
        self.clients = {}  # contains all the client's data
        self.current_bid = self.base_price
        self.bid_increment = bid_increment
        self.auction_done = False
        self.duration = duration
        self.auction_start_time = datetime.datetime.now()
        self.currency = currency

        # server
        self.address = addr
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.address)

        # threads
        self.listen_bidders = threading.Thread(target=self.listen_bidders)
        self.timeout_thread = threading.Thread(target=self.timeout)


    def increase_bid(self, bid=""):
        self.bids += 1

        if bid == "":
            self.current_bid += (self.bid_increment / 100) * self.base_price
        else:
            self.current_bid = int(bid)

    def timeout(self):
        print("the auction will stop on TIME")
        for seconds in range(self.duration):
            sleep(1)
            self.time_left = self.duration - seconds

        self.auction_done = True

    def evaluate_result(self):
        """evaluates the result auction"""
        if self.auction_done is True:
            self.winner = self.highest_bidder
            self.hammer_price = self.current_bid

        self.item.sold(self.winner, self.hammer_price)

    def stop(self):
        """stops the auction server"""
        self.timeout_thread.join()
        ending_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        ending_socket.connect(self.address)
        self.send(DISCONNECT_MESSAGE)

    def listen_client(self, address):
        print("()\n")
        client_socket, client_name = self.clients[address]["socket"], ""
        self.clients.pop(address)

        while True:
            message = client_socket.recv(512).decode(FORMAT)

            # this "if block" will be run very first because the Participant will be first sending its name
            if message.startswith("|"):
                client_name = message[1:]
                self.clients[client_name] = {
                    "address": address,
                    "socket": client_socket,
                    "number_of_bids": 0,
                    "last_bid_position": 0,
                    "bids": []
                }

            elif message.startswith("+"):
                # if bid is none then by default 10% of the base price will be added to the current bid
                bid = message[1:]
                self.increase_bid(bid=bid)
                self.clients[client_name]["number_of_bids"] += 1
                self.clients[client_name]["latest_bid_number"] = self.bids
                self.clients[client_name]["bids"].append(bid + self.currency)

            elif message.startswith("<"):
                index = message.find(">")
                self.clients[client_name][message[1:index]] = message[index + 1:]

            elif message is DISCONNECT_MESSAGE:
                client_socket.close()
                self.clients.pop(client_name)

    def listen_bidders(self):
        """starts listening to the bidders"""
        print("listening to bidders")
        self.server.listen()  # server starts to listen for connections

        while self.auction_done is False:  # the value of auction_done is True when the time's out for the program.
            client, address = self.server.accept()
            self.clients[address] = {
                "socket": client}  # will be popped out when listen_client will be run for the specific address
            client_thread = threading.Thread(target=self.listen_client, args=(address,))
            client_thread.start()

    def send(self, message, address="*"):
        """
        by default, the message will be sent, until you specify any address
        """
        if address == "*":
            for client in self.clients:
                client_socket = client["socket"]
                client_socket.send(bytes(message, FORMAT))

        else:
            if (type(message) == bool) or (type(message) is None):
                self.clients[address][0].send(bytes(messages[message], FORMAT))
            else:
                self.clients[address][0].send(bytes(message, FORMAT))

    def start(self):
        """starts the auction"""
        # the timeout thread will stop the auction after the given duration by the user
        # by default the timeout of an auction is 200 seconds
        self.listen_bidders.start()
        self.timeout_thread.start()
