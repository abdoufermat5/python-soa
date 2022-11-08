class Loan:
    def __init__(self, borrower=None, loan_amount=0, apartment=None):
        self.borrower = borrower
        self.loan_amount = loan_amount
        self.apartment = apartment

    def set_borrower(self, borrower):
        self.borrower = borrower

    def set_loan_amount(self, loan_amount):
        self.loan_amount = loan_amount

    def set_apartment(self, apartment):
        self.apartment = apartment

    def set_loan(self, borrower, loan_amount, apartment):
        self.borrower = borrower
        self.loan_amount = loan_amount
        self.apartment = apartment

    def is_empty(self):
        """
        Check if the loan is empty
        :return: Boolean
        """
        return self.borrower is None and self.loan_amount == 0 and self.apartment is None

    def reprJSON(self):
        """
        Represent the loan as a JSON
        :return: Dict
        """
        return dict(borrower=self.borrower.reprJSON(), loan_amount=self.loan_amount,
                    apartment=self.apartment.reprJSON())

    def __str__(self):
        print("-------------------> EMPRUNT")
        loan = "Emprunteur: " + str(self.borrower) + " \n| Montant de l'emprunt: " + str(
            self.loan_amount) + " \n| Appartement: \n" + str(self.apartment)
        return loan
