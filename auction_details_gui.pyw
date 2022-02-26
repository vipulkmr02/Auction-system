from datetime import datetime
# from bddrs import *
from tkinter import *
from tkinter import filedialog
from common import *


JSON_location = ""


def json_button():
    global JSON_location
    file = filedialog.askopenfilename(filetypes=(("JSON(Javascript Object Notation files)", "*.json"),))
    JSON_location = file


ITEM, AUCTION = {}, {}
AUCTION_DURATION = 0
main_window = Tk()
var = IntVar()  # 1 for PUBLIC 2 for PRIVATE
main_window.title("Create an AUCTION")
main_window.geometry("500x500")

auction_details_frame = LabelFrame(
    main_window,
    font=FONT_HEADING,
    text="Auction Settings",
    padx=20, pady=20
)

Label(
    auction_details_frame,
    text="Duration (in seconds)",
    font=FONT_LABELS,
    padx=10, pady=10
).grid(row=1, column=0)
duration_box = Entry(auction_details_frame, font=FONT)
duration_box.grid(row=1, column=1, columnspan=2)

Label(
    auction_details_frame,
    text="Server Type",
    font=FONT_LABELS
).grid(row=2, column=0)
Radiobutton(
    auction_details_frame,
    text="Public",
    font=FONT,
    variable=var,
    value=1,
    padx=4,
    pady=10
).grid(row=2, column=1)

Radiobutton(
    auction_details_frame,
    text="Private",
    font=FONT,
    variable=var,
    value=2,
    padx=4,
    pady=10
).grid(row=2, column=2)


auction_details_frame.pack(padx=20, pady=20)

item_details_frame = LabelFrame(main_window, font=FONT_HEADING, text="Item Details")

Label(
    item_details_frame,
    text="Name",
    font=FONT_LABELS,
    padx=10,
    pady=10
).grid(row=0, column=0)

Item_name = Entry(item_details_frame, font=FONT_LABELS)
Item_name.grid(row=0, column=1, padx=10, pady=10)

Label(
    item_details_frame,
    text="Description",
    font=FONT_LABELS,
    padx=10,
    pady=10
).grid(row=1, column=0)

Item_desc = Entry(item_details_frame, font=FONT)
Item_desc.grid(row=1, column=1, padx=10, pady=10)

Label(
    item_details_frame,
    text="Dimensions",
    font=FONT_LABELS,
    padx=10, pady=10
).grid(row=2, column=0)

Item_dimension = Entry(item_details_frame, font=FONT)
Item_dimension.grid(row=2, column=1, padx=10, pady=10)

Label(
    item_details_frame,
    text="Price",
    font=FONT_LABELS,
    padx=10,
    pady=10
).grid(row=3, column=0)

Item_price = Entry(item_details_frame, font=FONT)
Item_price.grid(row=3, column=1, padx=10, pady=10)


def collect():
    ITEM["name"] = Item_name.get()
    ITEM["dimensions"] = Item_dimension.get()
    ITEM["price"] = Item_price.get()
    ITEM["desc"] = Item_desc.get()
    AUCTION["duration"] = duration_box.get()
    AUCTION["type"] = var.get()
    file_content = f"auction: {str(AUCTION)}\nitem: {str(ITEM)}"
    open(
        f".\\data\\Auction_{datetime.now()}.json", "a").write(file_content)
    main_window.destroy()


# submit button
Button(
    item_details_frame,
    text="SUBMIT",
    font=FONT,
    command=collect
).grid(row=7, column=0)

# JSON button
Button(item_details_frame,
       text="ITEM's file", command=json_button,
       font=FONT
).grid(row=7, column=1)

item_details_frame.pack(padx=15, pady=15)

main_window.mainloop()
