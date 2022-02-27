from sys import platform

OPERATING_SYSTEM = platform
# server
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!@disconnect@!"

# tkinter GUI
FONT_HEADING = ("Noto Sans", 12)
FONT = ("Open Sans", 10)
FONT_LABELS = ("Open Sans", 10, "bold")
FONT_BUTTON = ("Segoe UI", 10)
FONT_LISTBOX = ("Consolas", 10)


def numberth(number):
    if str(number)[-1] == '1':
        return number+"st"
    elif str(number)[-1] == '2':
        return number+"nd"
    elif str(number)[-1] == '3':
        return number+"rd"
    else:
        return number+"th"


def read_auction(file_path):
    from json import loads
    content = open(file_path).read()
    return loads(content)


def fetch_ongoing_auctions(a='r', b=None):
    from json import loads, dumps

    if a == 'r':
        file = open("ongoing_auctions.json", "r")
        result = loads(file.read())
        return result

    if a == 's':
        file = open("ongoing_auctions.json", "a")
        file.write(dumps(b))


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
