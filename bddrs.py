from common import *
import socket
import threading


class Participant:
    def __init__(self, name, address):
        self.name, self.address = name, address
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_server = True

    def send(self, abc):
        """sends messages/commands to auction server"""

        self.socket.send(bytes(abc, FORMAT))

    def listen(self):
        """Starts listening to the auction server"""
        while self.listen_server:
            message = self.socket.recv(512).decode(FORMAT)

            if message == 1:
                message = True
            elif message == 3:
                message = False
            elif message == 0:
                message = None
            if message == DISCONNECT_MESSAGE:
                self.listen_server = False

    def start(self):
        """Starts the participant to send & receive commands to the auction server"""
        self.socket.connect(self.address)
        print(f"connected to {self.address}")
        # this thread will listen the commands from server
        listen = threading.Thread(target=self.listen)
        listen.start()  # listening starts
        self.socket.send(bytes(f"|{self.name}", FORMAT))


if __name__ == "__main__":
    p = Participant("Vipul", ("localhost", 60000))
    p.start()
