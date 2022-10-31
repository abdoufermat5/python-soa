from loan_approval_client.model.Address import Address


class User:
    def __init__(self, name="", num_ssn="", email="", address=Address()):
        self.name = name
        self.num_ssn = num_ssn
        self.address = address
        self.email = email

    def reprJSON(self):
        return dict(name=self.name, num_ssn=self.num_ssn, email=self.email, address=self.address.reprJSON())
