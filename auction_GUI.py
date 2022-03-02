from actinitm import *
from actn import *
from tkinter import *

thing_name = ""
thing_price = ""

auction_window = Tk()
auction_window.title("AUCTIONS")

# asking for auction item and auction_details
# auction_item_details

HEADING = Label(
    auction_window, text=f"AUCTION",
    anchor=CENTER, font=FONT_HEADING
)
HEADING.pack()

Label(
    auction_window, text="AUCTION", font=FONT
).pack()



auction_thing_name = Entry(auction_window , bd="4p")
auction_thing_price = Entry(auction_window, bd="4p")


def submit():
    global thing_price, thing_name
    thing_name = auction_thing_name.get()
    thing_price = auction_thing_price.get()


Label(
    auction_window,
    text="Item Name",
    font=FONT,
).pack()
auction_thing_name.pack()

Label(
    auction_window,
    text="Item Price",
    font=FONT
).pack()
auction_thing_price.pack()

Button(
    text="SUBMIT",
    command=submit
).pack()

thing = AuctionItem(name=auction_thing_name.get(), price=auction_thing_price.get())

auction_window.geometry("1000x1000")
auction_window.mainloop()

print(f"NAME : {thing_name}")
print(f"PRICE : {thing_price}")
