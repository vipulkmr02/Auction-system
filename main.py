from actinitm import *
from actn import *

item = AuctionItem(name="watch", price=400)

auction = Auction(
    item,
    addr=("localhost", 61000),
    bid_increment=2,
    duration=50
)

auction.start()

while True:
    i = input(">")

    if i == "stop":
        break
        auction.stop()
