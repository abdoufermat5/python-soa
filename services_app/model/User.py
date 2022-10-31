from spyne.model.complex import ComplexModel
from spyne.model.primitive import Unicode

from model.Address import Address


class User(ComplexModel):
    __namespace__ = 'datascale.services.user'
    name = Unicode
    num_ssn = Unicode
    email = Unicode
    address = Address
