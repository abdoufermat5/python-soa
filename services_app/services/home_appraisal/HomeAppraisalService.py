from rpclib.decorator import srpc
from rpclib.service import ServiceBase
from rpclib.model.primitive import Integer, String, Float

from model.Appartment import Apartment
from model.Loan import Loan


class AppraisalService(ServiceBase):
    """Service d'évaluation de l'appartement
    Ce service permet d'évaluer si un appartement est éligible ou non pour un prêt
    L’information métier portée par le message d’entrée de l’opération concernée de ce service
    comprend le prix de l’appartement et le montant du prêt.
    La condition qui doit être vérifié par ce service est la suivante : Un appartement dont le prix
    est inférieur ou égal au montant du prêt sera considéré comme non éligible. Sinon, l’appartement
    est considéré comme éligible.
    @param appart_price prix de l'appartement
    @param pret montant du prêt
    @return status de l'éligibilité de l'appartement
    """
    @srpc(Loan, _returns=String)
    def appraise(loan):
        if loan.loan_amount > loan.apartment.price:
            return "Denied"
        else:
            return "Approved"
