from common import *
import socket
import threading


class Participant:
    def __init__(self, name, address):
        self.name, self.address = name, address
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, abc):
        """sends messages/commands to auction server"""
        if abc is True:
            abc = messages[True]
        elif abc is False:
            abc = messages[False]
        elif abc is None:
            abc = messages[None]
        else:
            self.socket.send(bytes(abc, FORMAT))

    def listen(self):
        """Starts listening to the auction server"""
        while True:
            message = self.socket.recv(512).decode(FORMAT)
            if process(message) == -1:
                self.send(-1)

    def start(self):
        """Starts the participant to send & receive commands to the auction server"""
        self.socket.connect(self.address)
        print(f"connected to {self.address}")
        # this thread will listen the commands from server
        listen = threading.Thread(target=self.listen)
        listen.start()  # listening starts
        self.socket.send(bytes(self.name, FORMAT))


if __name__ == "__main__":
    p = Participant("Vipul", ("localhost", 60000))
    p.start()
