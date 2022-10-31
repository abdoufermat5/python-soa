class Loan:
    def __init__(self, borrower=None, loan_amount=0, apartment=None):
        self.borrower = borrower
        self.loan_amount = loan_amount
        self.apartment = apartment

    def reprJSON(self):
        return dict(borrower=self.borrower.reprJSON(), loan_amount=self.loan_amount, apartment=self.apartment.reprJSON())