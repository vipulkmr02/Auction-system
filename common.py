FORMAT = "utf-8"


def process(message):
    if message.startswith("?"):
        return input(message[1:-1])
    elif message.startswith("!"):
        print(message[1:-1])
    else:
        return -1


def handle_client(s):
    message = s.recv(512).decode()
    process(message)
