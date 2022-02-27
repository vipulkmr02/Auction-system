# from bddrs import *
from json import dumps
from os import system
from tkinter import *
from tkinter import filedialog
from common import *

JSON_location = ""


def json_button():
    global JSON_location
    file = filedialog.askopenfilename(filetypes=(("JSON(Javascript Object Notation files)", "*.json"),))
    JSON_location = file


ITEM, AUCTION, OWNER = {}, {}, {}
main_window = Tk()
var = IntVar()  # 1 for PUBLIC 2 for PRIVATE
var.set(-1)
main_window.title("Create an AUCTION")
main_window.geometry("800x600")

# auction details
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
duration_box = Entry(auction_details_frame, font=FONT, relief=FLAT, bd=1)
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
    padx=10,
    pady=10
).grid(row=2, column=1)

Radiobutton(
    auction_details_frame,
    text="Private",
    font=FONT,
    variable=var,
    value=2,
    padx=10,
    pady=10
).grid(row=2, column=2)

auction_details_frame.pack(padx=20, pady=20)

# Item details
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

Label(
    item_details_frame,
    text="Details",
    font=FONT_LABELS,
    padx=10, pady=10
).grid(row=4, column=0)

Item_details = Entry(
    item_details_frame,
    font=FONT
)
Item_details.grid(row=4, column=1, padx=10, pady=10)

# Owner details
owner_details_frame = LabelFrame(
    main_window,
    text="Owner details",
    font=FONT_HEADING)

Label(
    owner_details_frame,
    text="Name",
    font=FONT_LABELS,
    padx=10,
    pady=10
).grid(row=0, column=0)

owner_name = Entry(owner_details_frame, font=FONT)
owner_name.grid(row=0, column=1, padx=10, pady=10)

Label(
    owner_details_frame,
    text="Mobile no.",
    font=FONT_LABELS,
    padx=10,
    pady=10
).grid(row=1, column=0)
owner_number = Entry(owner_details_frame, font=FONT)
owner_number.grid(row=1, column=1, padx=20, pady=20)


def collect():
    if Item_name.get() == "":
        status.configure(text="Item name is not given")
    else:
        ITEM["name"] = Item_name.get()

    if Item_desc.get() == "":
        status.configure(text="Item description is not given")
    else:
        ITEM["desc"] = Item_desc.get()

    if Item_price.get() == "":
        status.configure(text="Item price is not given")
    else:
        ITEM["price"] = Item_price.get()

    ITEM["dimensions"] = Item_dimension.get()

    ITEM["details"] = Item_details.get()

    if var.get() == 1:
        AUCTION["type"] = "PUBLIC"

    elif var.get() == 2:
        AUCTION["type"] = "PRIVATE"

    else:
        status.configure(text="Please specify TYPE of AUCTION")

    print(AUCTION)

    AUCTION["duration"] = duration_box.get()

    if owner_name.get() == "" or owner_number.get() == "":
        status.configure(text="Owner details are not complete")
    else:
        OWNER["name"] = owner_name.get()
        OWNER["mobile"] = owner_number.get()

    file_content = "{\"auction\":%s, \"item\":%s, \"owner\":%s}" % (dumps(AUCTION), dumps(ITEM), dumps(OWNER))

    auction_file = open(
        f".\\data\\Auction_{ITEM['name']}.json", "w+")

    auction_file.write(file_content)
    auction_file.close()
    main_window.destroy()
    system(".\\auction_GUI.pyw .\\data\\Auction_%s.json" % ITEM['name'])


auction_details_frame.pack(fill='x', padx=15, pady=15)
item_details_frame.pack(fill='x', padx=15, pady=15)
owner_details_frame.pack(fill='x', padx=15, pady=15)
# submit button
Button(
    main_window,
    text="SUBMIT",
    font=FONT,
    command=collect
).pack(padx=10, pady=10, side="left")

# JSON button
Button(
    main_window,
    text="ITEM's file", command=json_button,
    font=FONT,
).pack(padx=10, pady=10, side="right")

# status bar
status = Label(main_window, relief=FLAT, text="", font=("Segoe UI", 10,))
status.pack(anchor=SW)
main_window.geometry("400x700")
main_window.resizable(False, False)
main_window.mainloop()
