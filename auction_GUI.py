from actinitm import *
from common import *
from actn import *
from tkinter import *
from sys import argv

details = read_auction(argv[1])
auction, item = details["auction"], details["item"]
thing = AuctionItem(name=item["name"], price=item["price"], dimensions=item["dimensions"], desc=item["desc"], details=item["details"], owner=account.name)

auction_window = Tk()
