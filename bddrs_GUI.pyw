from bddrs import *
from tkinter import *
from sys import argv


bidding_window = Tk()
temp_address = tuple(argv[2].split("+"))
address = (temp_address[0], int(temp_address[1]))
details = read_auction(argv[1])
auction, item, owner = details["auction"], details["item"], details["owner"]


# ITEM
item_frame = Frame(bidding_window, bd=0, width="200")

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

auction_details_frame = Frame(bidding_window, bd=0)

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
    text="action.highest_bid",
    font=("Engraves MT", 16, 'bold')
).pack(anchor=CENTER, padx=20, pady=20, ipadx=10, ipady=10)

# Bidders

bidders_frame = Frame(bidding_window, bd=0)
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

participant_frame = LabelFrame(bidding_window, text="Participants", font=FONT_LABELS)

participants = Listbox(participant_frame, font=FONT_LISTBOX)

participants.pack(padx=10, pady=10)

item_frame.pack(anchor=NW, ipadx=10, ipady=10)
auction_details_frame.pack(anchor=NE, ipadx=10, ipady=10)
bidders_frame.pack(anchor=SE, ipadx=10, ipady=10)

bidding_window.minsize(800, 400)
