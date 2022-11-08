from loan_approval_client.model.Address import Address


class User:
    def __init__(self, name="", num_ssn="", email="", address=Address()):
        self.name = name
        self.num_ssn = num_ssn
        self.address = address
        self.email = email

    def set_name(self, name):
        self.name = name

    def set_num_ssn(self, num_ssn):
        self.num_ssn = num_ssn

    def set_email(self, email):
        self.email = email

    def set_address(self, address):
        self.address = address

    def set_user(self, name, num_ssn, email, address):
        self.name = name
        self.num_ssn = num_ssn
        self.email = email
        self.address = address

    def is_empty(self):
        """
        Check if the user is empty
        :return: Boolean
        """
        return self.name == "" and self.num_ssn == "" and self.email == "" and self.address.is_empty()

    def reprJSON(self):
        """
        Represent the user as a JSON
        :return: Dict
        """
        return dict(name=self.name, num_ssn=self.num_ssn, email=self.email, address=self.address.reprJSON())

    def __str__(self):
        print("-------------------INFORMATION GENERALE-------------------")
        user = "Nom: " + self.name + " \n| Numéro de sécurité sociale: " + self.num_ssn + " \n| Adresse: " + str(
            self.address) + " \n| Email: " + self.email
        return user
