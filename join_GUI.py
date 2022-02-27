from tkinter import *
from common import *

def connect_auction():
    pass


auctions = fetch_auctions(mode="~")
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

# Auctions list
auction_list = Listbox(
    list_frame,
    font=FONT_LISTBOX
)
auction_list.pack(padx=10, pady=10)


def create_auction_list():
    for id, details in auctions:
        auction_list.insert(END, f"{details['name']} | {details['price']}")


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
main_window.mainloop()
