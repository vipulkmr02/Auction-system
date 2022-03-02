from bddrs import *
from tkinter import *
from sys import argv
from time import sleep

bidding_window = Tk()
temp_address = tuple(argv[2].split("+"))
address = (temp_address[0], int(temp_address[1]))
details = read_auction(f".\\data\\{argv[1]}")
auction, item, owner = details["auction"], details["item"], details["owner"]

client = Participant(
    name=owner["name"], address=address)

# ITEM
item_frame = LabelFrame(bidding_window, text="Item details")

Label(
    item_frame,
    text=f"Item on Auction is {item['name']}",
    font=FONT_LABELS
).grid(row=0, column=0)

Label(
    item_frame,
    text=f"which is owned by {owner['name'].upper()}",
    font=FONT_LABELS
).grid(row=1, column=0)

# AUCTION DETAILS

auction_details_frame = LabelFrame(
    bidding_window,
    text="Auction",
    font=FONT_HEADING)

# highest bidder label
Label(
    auction_details_frame,
    text=client.auction_data["hb"],
    font=("Engraves MT", 20, 'bold')
).grid(row=0, column=0, padx=20, pady=20)

# current bid
Label(
    auction_details_frame,
    text=client.auction_data["cb"],
    font=("Engraves MT", 16, 'bold')
).grid(row=1, column=0, padx=20, pady=20)

# Bidders

bidders_frame = Frame(bidding_window)
clients_list = Listbox(bidders_frame, font=FONT_LISTBOX)
clients_list.grid(row=0, column=0)

for client, values in client.auction_data['cd']:
    clients_list.insert(
        0,
        f"{client} has placed a bid of {values['bids'][-1]} INR, this is the {numberth(values['last_bid_position'])} bid")

# PARTICIPANT

participant_frame = LabelFrame(bidding_window, text="Participants", font=FONT_HEADING)

Label(participant_frame, font=FONT_LABELS).grid(row=0, column=0)

bid_entry = Entry(participant_frame, font=FONT_LABELS)
bid_entry.grid(row=0, column=1)

bid = bid_entry.get()

place_bid = Button(
    participant_frame,
    text="place Bid",
    command=client.bid(bid))

place_bid.grid(row=0, column=2)

time_left = Label(
    participant_frame,
    text="",
    font=FONT_LABELS
)
time_left.grid(row=0, column=3)

item_frame.pack(anchor=NW, ipadx=10, ipady=10)
participant_frame.pack(anchor=NE, ipadx=10, ipady=10)
auction_details_frame.pack(anchor=SW, ipadx=10, ipady=10)
bidders_frame.pack(anchor=SE, ipadx=10, ipady=10)
bidding_window.minsize(400, 400)


def update_the_info():
    time_left.configure(text=client.auction_data["tl"])
    update_clients_list()


time_left_thread = threading.Thread(target=update_the_info)


def clear_auction_list():
    for index in range(len(client['cd'])):
        clients_list.delete(0)


def create_auction_list():
    for key in client['cd']:
        clients_list.insert(
            0,
            f"{client['cd'][key]['name']} | {client['cd']['price']}")


def update_clients_list():
    while True:
        clear_auction_list()
        create_auction_list()
        sleep(10)


bidding_window.mainloop()
