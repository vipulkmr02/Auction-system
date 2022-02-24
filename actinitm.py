class AuctionItem:
    def __init__(self, price, name=None):
        self.name, self.price = name, price
        self.hammer_price = 0
        self.buyer = None

    def sold(self, buyer, hammer_price):
        self.hammer_price = hammer_price
        self.buyer = buyer
