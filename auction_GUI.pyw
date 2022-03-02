from actinitm import *
from actn import *
from time import sleep
from tkinter import *
from sys import argv
from socket import gethostname, gethostbyname
from threading import Thread
from random import randint

auction_window = Tk()
details = read_auction(argv[1])
auction, item, owner = details["auction"], details["item"], details["owner"]

thing = AuctionItem(
    name=item["name"],
    price=item["price"],
    dimensions=item["dimensions"],
    desc=item["desc"],
    details=item["details"],
    owner=owner["name"])


def check_participants():
    global participants
    length = len(action.clients)
    print("length")
    while 1:
        if length != len(action.clients):
            sleep(1)
            length = len(action.clients)
            for name, data in action.clients:
                print("yes I am!")
                participants.insert(
                    END,
                    f"NAME: {name} | NUMBER OF BIDS: {data['number_of_bids']}"
                )


def time_count():
    while True:
        time_left.configure(text=str(action.time_left))


PORT = randint(60000, 65000)

TIME_thread = Thread(target=time_count)

action = Auction(
    item=thing,
    addr=(gethostbyname(gethostname()), PORT),
    duration=int(auction["duration"])
)

if auction["type"] == "PUBLIC":
    auction_info = {
        "name": item['name'],
        "desc": item['desc'],
        "price": item['price'],
        "address": action.address
    }

# ITEM
item_frame = LabelFrame(
    auction_window,
    font=FONT_LABELS,
    text="Item details")

Label(
    item_frame,
    text=f"Item on Auction is {item['name']}",
    font=FONT_LABELS
).grid(row=0, column=0)

Label(
    item_frame,
    text=f"which is owned by {owner['name'].upper()}",
    font=FONT_LABELS,
).grid(row=1, column=0)

# AUCTION DETAILS

auction_details_frame = Frame(auction_window, bd=0)

time_left = Label(
    auction_details_frame,
    font=FONT_LABELS,
)
time_left.grid(row=0, column=1, columnspan=3)

high = Label(
    auction_details_frame,
    text=action.highest_bidder,
    font=("Engraves MT", 20, 'bold')
)
high.grid(row=1, column=2)

bid = Label(
    auction_details_frame,
    text=action.current_bid,
    font=("Engraves MT", 16, 'bold')
)
bid.grid(row=2,column=2)

# Bidders

bidders_frame = Frame(auction_window, bd=0)
clients_list = Listbox(bidders_frame, font=FONT_LISTBOX)
clients_list.grid(row=0, column=0)

for client, values in action.clients:
    clients_list.insert(
        END,
        f"{client} has placed a bid of {values['bids'][-1]} INR, this is the {numberth(values['last_bid_position'])} bid")

Button_frame = LabelFrame(
    bidders_frame,
    text='Options',
    bd=0,
    font=FONT_HEADING)
Button_frame.grid(row=1, column=0)

Button(
    Button_frame,
    text="REMOVE",
    font=FONT_BUTTON
).grid(row=1, column=2)

# PARTICIPANTS

participant_frame = LabelFrame(auction_window, text="Participants", font=FONT_LABELS)

participants = Listbox(participant_frame, font=FONT_LISTBOX)

item_frame.grid(row=0, column=0, padx=10, pady=10)
auction_details_frame.grid(row=0, column=1, padx=10, pady=10)
participants.grid(row=1, column=0, padx=10, pady=10)
bidders_frame.grid(row=1, column=1, padx=10, pady=10)

auction_window.minsize(400, 400)


def start_auction():
    action.start()
    fetch_auctions('+', auction_info)
    Thread(target=time_count).start()
    Thread(target=check_participants).start()


def stop_auction():
    action.evaluate_result()
    high.configure(text=action.highest_bidder)
    bid.configure(text=action.current_bid)
    fetch_auctions('-', auction_info)
    action.stop()


start_button = Button(
    auction_window,
    text="start",
    command=start_auction
)
start_button.grid(row=2, column=0)

stop_button = Button(
    auction_window,
    text="stop",
    command=stop_auction
)
stop_button.grid(row=2, column=1)

# auction_window.configure(background="red")
# auction_window.wm_attributes("-fullscreen", 'True')

auction_window.resizable(False, False)
auction_window.mainloop()
