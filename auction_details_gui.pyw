# from bddrs import *
from tkinter import *
from tkinter import filedialog
from common import *

def json_button():
    file = filedialog.askopenfilename(filetypes=(("JSON", "*.json"),))
    return file


ITEM, AUCTION = {}, {}
AUCTION_DURATION = 0
var = IntVar()  # 1 for PUBLIC 2 for PRIVATE
main_window = Tk()
main_window.title("Create an AUCTION")
main_window.geometry("500x500")

auction_details_frame = LabelFrame(
    main_window,
    font=FONT_HEADING,
    text="Auction Settings"
)

Label(
    auction_details_frame,
    text="Duration (in seconds)",
    font=FONT
).grid(row=1, column=0)
duration_box = Entry(auction_details_frame, font=FONT)
duration_box.grid(row=1, column=1, columnspan=2)

Label(auction_details_frame, text="Server Type", font=FONT).grid(row=2, column=0)
Radiobutton(
    auction_details_frame,
    text="Public",
    variable=var,
    value=1
).grid(row=2, column=1)

Radiobutton(
    auction_details_frame,
    text="Private",
    variable=var,
    value=2
).grid(row=2, column=2)

auction_details_frame.pack(padx=20, pady=20)

item_details_frame = LabelFrame(main_window, font=FONT_HEADING, text="Item Details")

Label(
    item_details_frame,
    text="Name",
    font=FONT
).grid(row=0, column=0)
Item_name = Entry(item_details_frame, font=FONT)
Item_name.grid(row=0, column=1)

Label(item_details_frame, text="Description", font=FONT).grid(row=1, column=0)
Item_desc = Entry(item_details_frame, font=FONT)
Item_desc.grid(row=1, column=1)

Label(item_details_frame, text="Dimensions", font=FONT).grid(row=2, column=0)
Item_dimension = Entry(item_details_frame, font=FONT)
Item_dimension.grid(row=2, column=1)

Label(item_details_frame, text="Price", font=FONT).grid(row=3, column=0)
Item_price = Entry(item_details_frame, font=FONT)
Item_price.grid(row=3, column=1)


def collect():
    ITEM["name"] = Item_name.get()
    ITEM["dimensions"] = Item_dimension.get()
    ITEM["price"] = Item_price.get()
    ITEM["desc"] = Item_desc.get()
    AUCTION["duration"] = duration_box.get()
    AUCTION["type"] = var.get()
    print(AUCTION)


# submit button
Button(
    item_details_frame,
    text="SUBMIT",
    font=FONT,
    command=collect
).grid(row=7, column=0, columnspan=3)

# item json upload button
# Button(item_details_frame,
#        text="ITEM's file", relief=GROOVE,
#        bd=3, command=json_button,
#        font=FONT, activebackground="black",
#        activeforeground="white"
#        ).grid(row=1, column=0)

item_details_frame.pack(padx=15, pady=15)

main_window.mainloop()
