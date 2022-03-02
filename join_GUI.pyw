from tkinter import *
from threading import Thread
from time import sleep
from common import *
from os import system

auctions = fetch_auctions()


def connect_auction():
    global auctions, auction_list
    auctions = fetch_auctions()
    key = f"Auction_{auction_list.get(ANCHOR).split('|')[0]}"
    command = f".\\bddrs_GUI.pyw {auctions[key]['name']} {auctions[key]['address'][0]}+{auctions[key]['address'][1]})"

    system(command)


main_window = Tk()

user_details_frame = LabelFrame(
    main_window,
    text="Your Details",
    padx=10,
    pady=10
)

# USER's details
Label(
    user_details_frame,
    text="NAME",
    font=FONT_LABELS
).pack(anchor=NW)
NAME = Entry(user_details_frame, font=FONT_LABELS)
NAME.pack(anchor=NE)

Label(
    user_details_frame,
    text="Mobile no.",
    font=FONT_LABELS
).pack(anchor=SW)
mobile_no = Entry(user_details_frame, font=FONT_LABELS)
mobile_no.pack(anchor=SE)

list_frame = LabelFrame(
    main_window,
    text="AUCTIONS",
    padx=10,
    pady=10)

auction_list = Listbox(
    list_frame,
    font=FONT_LISTBOX
)
# Auctions list
auction_list.pack(padx=10, pady=10)


def clear_auction_list():
    for index in range(len(auctions)):
        auction_list.delete(0)


def create_auction_list():
    global auctions
    auctions = fetch_auctions()
    for key in auctions:
        auction_list.insert(0, f"{auctions[key]['name']} | {auctions[key]['price']}")


def update_auction_list():
    while True:
        clear_auction_list()
        create_auction_list()
        sleep(10)


options = LabelFrame(main_window, text="Commands")

Button(
    options,
    text='Connect',
    font=FONT_BUTTON,
    command=connect_auction
).pack(padx=10, pady=7, side="left")

Button(
    options,
    text='Details',
    font=FONT_BUTTON
).pack(padx=10, pady=7, side="right")

user_details_frame.pack(pady=10, padx=10)
list_frame.pack(pady=10, padx=10)
options.pack(pady=10, padx=10)

create_auction_list()
update = Thread(target=update_auction_list)
update.start()
main_window.mainloop()
update.join()

# TODO: not showing all auctions in the "auction_list" list box
