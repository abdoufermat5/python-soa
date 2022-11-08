import asyncio
import json

import zeep


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)


def get_client(wsdl_url, method_url, service_url):
    """
    This function is used to get the client
    :param wsdl_url:
    :param method_url:
    :param service_url:
    :return: client, header_value
    """
    # create the header element
    header = zeep.xsd.Element(
        "Header",
        zeep.xsd.ComplexType(
            [
                zeep.xsd.Element(
                    "{http://www.w3.org/2005/08/addressing}Action", zeep.xsd.String()
                ),
                zeep.xsd.Element(
                    "{http://www.w3.org/2005/08/addressing}To", zeep.xsd.String()
                ),
            ]
        ),
    )
    header_value = header(Action=method_url, To=service_url)
    client = zeep.AsyncClient(wsdl_url)

    return client, header_value


def present_menu():
    """
    This function is used to present the menu to the user
    :return: None
    """
    print(" ------------- BIENVENUE DANS LA CONSOLE DE TRAITEMENT DE DEMANDE DE PRÊT IMMOBILIER  --------------")
    print("-" * 42)
    print("Les différentes options:")
    print("1. Verifier votre solvabilité")
    print("2. Vérifier si l'appartement est éligible")
    print("3. Vérifier si votre demande de prêt est acceptée")
    print("4. Quitter")
    print("-" * 42)


def input_user_info():
    """
    This function is used to get the user information from the user
    :return: the user information
    """
    name = input("Entrez votre nom: \n-->")
    print("\n")
    num_ssn = input("Entrez votre numéro de sécurité sociale: \n-->")
    street = input("Entrez votre rue: \n-->")
    city = input("Entrez votre ville: \n-->")
    state = input("Entrez votre Pays: \n-->")
    email = input("Entrez votre email: \n-->")

    return name, num_ssn, street, city, state, email


def input_loan_info():
    """
    This function is used to get the loan information from the user
    :return: the loan information
    """
    appart_price = input("Entrez le prix de l'appartement: \n-->")
    pret = input("Entrez le montant du prêt: \n-->")
    surface = input("Entrez la surface de l'appartement: \n-->")
    description = input("Entrez la description de l'appartement: \n-->")

    return appart_price, pret, surface, description
