from os import system as sys

# server
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!@disconnect@!"

# tkinter GUI
FONT_HEADING = "Arial 20"
FONT = "Calibri 12"

messages = {
    None: 0,
    True: 1,
    False: 3,
    "+": 10
}


def process(message):
    if message.startswith("?"):
        return input(message[1:-1])
    elif message.startswith("!"):
        print(message[1:-1])

    else:
        return -1


def handle_client(s):
    message = s.recv(512).decode()
    return message
