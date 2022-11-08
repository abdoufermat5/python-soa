class Address:
    def __init__(self, street="", city="", state=""):
        """
        Constructor
        :param street:
        :param city:
        :param state:
        """
        self.street = street
        self.city = city
        self.state = state

    def set_street(self, street):
        self.street = street

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_address(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state

    def is_empty(self):
        """
        Check if the address is empty
        :return: Boolean
        """
        return self.street == "" and self.city == "" and self.state == ""

    def reprJSON(self):
        """
        Represent the address as a JSON
        :return: dict
        """
        return dict(street=self.street, city=self.city, state=self.state)

    def __str__(self):
        print("-------------------> ADRESSE")
        address = "Rue: " + self.street + " \n| Ville: " + self.city + " \n| Pays: " + self.state
        return address
