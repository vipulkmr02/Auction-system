from os import system as sys
from tkinter import *

main_window = Tk()
main_window.title("AUCTION SYSTEM")
main_window.geometry("600x200")
main_window.configure(background="white")
font = "\"Lucida Bright\" 40"


def create():
    main_window.destroy()
    sys(".\\auction_details_gui.pyw")

def join():

    pass

# create auction button
Button(
    text="create",
    command=create,
    padx=50,
    font=font,
    anchor=CENTER

).grid(row=0, column=0)

# join button
Button(
    text="join",
    command=join,
    padx=50,
    font=font
).grid(row=0, column=1)

main_window.resizable(False, False)
main_window.mainloop()
