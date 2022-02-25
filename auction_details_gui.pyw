from bddrs import *
from tkinter import *
from common import *

AUCTION_DURATION = 0
server_type = IntVar()
main_window = Tk()
main_window.title("Create an AUCTION")
main_window.geometry("500x500")

auction_details_frame = LabelFrame(
    main_window,
    font=FONT_HEADING,
    text="Auction Settings"
    # height="200p", width="200p"
)

Label(auction_details_frame, text="Duration (in seconds)", font=FONT).grid(row=1, column=0)
duration_box = Entry(auction_details_frame, font=FONT)
duration_box.grid(row=1, column=1, columnspan=2)

Label(auction_details_frame, text="Server Type", font=FONT).grid(row=2, column=0)
server_type_radio_pb = Radiobutton(auction_details_frame, font=FONT, variable=server_type, value=1, text="Public")
server_type_radio_pr = Radiobutton(auction_details_frame, font=FONT, variable=server_type, value=2, text="Private",
                                   command=lambda: 1)
server_type_radio_pb.grid(row=2, column=1)
server_type_radio_pr.grid(row=2, column=2)

auction_details_frame.pack()

item_details_frame = LabelFrame(main_window, text="Item Details")

Label(item_details_frame, text="Name", font=FONT).grid(row=0, column=0)
Item_name = Entry(item_details_frame, font=FONT)
Item_name.grid(row=0, column=1)

Button(item_details_frame,
       text="ITEM JSON", relief=GROOVE,
       bd=3, command=json_button,
       font=FONT, activebackground="black",
       activeforeground="white"
       ).grid(row=1, column=0)

item_details_frame.pack()

main_window.mainloop()
