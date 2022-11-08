class Apartment:
    def __init__(self, price=0, address=None, description="", surface=0):
        self.price = price
        self.address = address
        self.description = description
        self.surface = surface

    def set_price(self, price):
        self.price = price

    def set_address(self, address):
        self.address = address

    def set_description(self, description):
        self.description = description

    def set_surface(self, surface):
        self.surface = surface

    def set_apartment(self, price, address, description, surface):
        self.price = price
        self.address = address
        self.description = description
        self.surface = surface

    def is_empty(self):
        return self.price == 0 and self.address is None and self.description == "" and self.surface == 0

    def reprJSON(self):
        """
        Represent the apartment as a JSON
        :return: Dict
        """
        return dict(price=self.price, address=self.address.reprJSON(), description=self.description,
                    surface=self.surface)

    def __str__(self):
        print("-------------------> APPARTEMENT")
        apartment = "Prix: " + str(self.price) + " \n| Adresse: \n" + str(
            self.address) + " \n| Description: " + self.description + " \n| Surface (en m^2): " + str(self.surface)
        return apartment
