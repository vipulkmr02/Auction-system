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
    while 1:
        if length != len(action.clients):
            sleep(1)
            length = len(action.clients)
            for name, data in action.clients:
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
item_frame = Frame(auction_window, bd=0, width="200")

Label(
    item_frame,
    text=f"Item on Auction is {item['name']}",
    font=FONT_LABELS
).pack(anchor=NW, ipadx=5, ipady=5)

Label(
    item_frame,
    text=f"which is owned by {owner['name'].upper()}",
    font=FONT_LABELS
).pack(anchor=SW, ipadx=5, ipady=5)

# AUCTION DETAILS

auction_details_frame = Frame(auction_window, bd=0)

time_left = Label(
    auction_details_frame,
    bd=3,
    font=FONT_LABELS,
)
time_left.pack(anchor=NE, padx=10, pady=10)

Label(
    auction_details_frame,
    text=action.highest_bidder,
    font=("Engraves MT", 20, 'bold')
).pack(anchor=CENTER, padx=20, pady=20, ipadx=10, ipady=10)

Label(
    auction_details_frame,
    text=action.current_bid,
    font=("Engraves MT", 16, 'bold')
).pack(anchor=CENTER, padx=20, pady=20, ipadx=10, ipady=10)

# Bidders

bidders_frame = Frame(auction_window, bd=0)
clients_list = Listbox(bidders_frame, font=FONT_LISTBOX)
clients_list.pack(anchor=CENTER)

for client, values in action.clients:
    clients_list.insert(
        END,
        f"{client} has placed a bid of {values['bids'][-1]} {action.currency}, this is the {numberth(values['last_bid_position'])} bid")

Button_frame = LabelFrame(
    bidders_frame,
    height=50,
    bd=0, text='Options',
    font=FONT_HEADING)
Button_frame.pack(side="bottom")

Button(
    Button_frame,
    text="REMOVE",
    font=FONT_BUTTON
).pack(anchor=CENTER)

# PARTICIPANTS

participant_frame = LabelFrame(auction_window, text="Participants", font=FONT_LABELS)

participants = Listbox(participant_frame, font=FONT_LISTBOX)

participants.pack(padx=10, pady=10)

item_frame.pack(anchor=NW, ipadx=10, ipady=10)
auction_details_frame.pack(anchor=NE, ipadx=10, ipady=10)
bidders_frame.pack(anchor=SE, ipadx=10, ipady=10)

auction_window.minsize(800, 400)


def start_auction():
    print("auction started")
    action.start()
    fetch_auctions('+', auction_info)


def stop_auction():
    print("auction stopped")
    action.evaluate_result()
    action.stop()
    fetch_auctions('-', auction_info)

action.send("")

Button(auction_window, text="start", command=start_auction).pack(anchor=S)
Button(auction_window, text="stop", command=stop_auction).pack(anchor=S)
Thread(target=time_count).start()
Thread(target=check_participants).start()
# auction_window.configure(background="red")
# auction_window.wm_attributes("-fullscreen", 'True')
auction_window.mainloop()
