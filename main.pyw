from os import system as sys
from tkinter import *

main_window = Tk()
main_window.title("AUCTION SYSTEM")
main_window.geometry("600x200")
# main_window.configure(background="white")
font = "\"Lucida Bright\" 40"


def create():
    main_window.destroy()
    sys(".\\auction_details_gui.pyw")


def join():
    main_window.destroy()
    sys(".\\join_GUI.pyw")


# create auction button
Button(
    text="create",
    command=create,
    padx=50,
    font=font,
    anchor=CENTER, 
    relief=FLAT
).pack()

# join button
Button(
    text="join",
    command=join,
    padx=50,
    font=font,
    relief=FLAT
).pack()

main_window.resizable(False, False)
main_window.mainloop()
