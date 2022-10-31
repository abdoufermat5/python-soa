class Address:
    def __init__(self, street="", city="", state=""):
        self.street = street
        self.city = city
        self.state = state

    def reprJSON(self):
        return dict(street=self.street, city=self.city, state=self.state)
