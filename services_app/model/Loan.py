from spyne.model.complex import ComplexModel
from spyne.model.primitive import Float

from model.User import User
from model.Appartment import Apartment


class Loan(ComplexModel):
    __namespace__ = 'datascale.services.loan_details'
    borrower = User
    loan_amount = Float
    apartment = Apartment
