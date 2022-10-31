class Apartment:
    def __init__(self, price=0, address=None, description="", surface=0):
        self.price = price
        self.address = address
        self.description = description
        self.surface = surface

    def reprJSON(self):
        return dict(price=self.price, address=self.address.reprJSON(), description=self.description, surface=self.surface)