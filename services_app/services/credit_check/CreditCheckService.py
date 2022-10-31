from rpclib.decorator import srpc
from rpclib.service import ServiceBase
from rpclib.model.primitive import Integer, String, Float

from model.User import User


class CreditCheckService(ServiceBase):
    """Service de vérification de crédit
    Ce service permet de vérifier si un client est crédible ou non
    L’information métier portée par le message d’entrée de l’opération concernée de ce service
    comprend le nom, numéro de sécurité sociale (SSN), et l’adresse du demandeur.
    La condition qui doit être vérifié par ce service est la suivante : Un demandeur ayant le SSN
    commençant par le numéro 6 sera considéré comme solvable. Sinon, la personne est considérée
    comme non solvable.
    @param appart_price prix de l'appartement
    @param pret montant du prêt
    @return status de la solvabilité du client
    """
    @srpc(User, _returns=String)
    def checkSolvability(user):
        print("User: ", user)
        if str(user.num_ssn)[0] == '6':
            return f"{user.name} habitant à l'adresse {user.address.street} est solvable"
        else:
            return f"{user.name} habitant à l'adresse {user.address.street} n'est pas solvable"