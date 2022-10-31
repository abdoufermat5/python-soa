from spyne.model.complex import ComplexModel
from spyne.model.primitive import Unicode, Float
from model.Address import Address


class Apartment(ComplexModel):
    __namespace__ = 'datascale.services.apartment'
    price = Float
    address = Address
    description = Unicode
    surface = Float
