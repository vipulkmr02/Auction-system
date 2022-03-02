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
        return number + "st"
    elif str(number)[-1] == '2':
        return number + "nd"
    elif str(number)[-1] == '3':
        return number + "rd"
    else:
        return number + "th"


def read_auction(file_path):
    from json import loads
    content = open(file_path).read()
    return loads(content)


def fetch_auctions(mode='~', auction_info=None):
    from json import loads, dumps
    file = open(".\\auctions.json", "r").read()
    if file == "":
        file = "{}"
    auctions = loads(file)

    if mode == '~':
        return auctions

    elif mode == '+':
        identifier = "Auction_%s" % auction_info['name']
        file = open("auctions.json", "w")
        auctions[identifier] = auction_info
        file.write(dumps(auctions))

    elif mode == '-':
        identifier = "Auction_%s" % auction_info['name']
        file = open("auctions.json", "w")
        auctions.pop(identifier)
        file.write(dumps(auctions))


messages = {
    None: 0,
    True: 1,
    False: 3,
    "+": 10
}


def handle_client(s):
    message = s.recv(512).decode()
    return message
