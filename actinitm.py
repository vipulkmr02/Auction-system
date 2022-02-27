class AuctionItem:
    def __init__(self, price, name, dimensions, desc, details, owner):
        self.name, self.price = name, price
        self.hammer_price = 0
        self.buyer = None
        self.dimensions = dimensions
        self.desc = desc
        self.details = details
        self.owner = owner

    def sold(self, buyer, hammer_price):
        self.hammer_price = hammer_price
        self.buyer = buyer
