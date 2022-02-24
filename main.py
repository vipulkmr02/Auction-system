from tkinter import *

main_window = Tk()
main_window.geometry("600x400")
font = "\"Lucida Bright\" 40"


def create():
    close

def join():
    pass


Button(text="create", command=create, font=font).grid(row=0, column=0)
Button(text="join", command=join, font=font).grid(row=0, column=1)

main_window.mainloop()
main_window.destroy()
