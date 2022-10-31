from spyne.model.complex import ComplexModel
from spyne.model.primitive import Unicode


class Address(ComplexModel):
    __namespace__ = 'datascale.services.address'
    street = Unicode
    city = Unicode
    state = Unicode
    telephone = Unicode
