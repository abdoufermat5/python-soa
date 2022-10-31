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
    print(" ------------- BIENVENUE DANS LA CONSOLE DE TRAITEMENT DE DEMANDE DE PRÊT IMMOBILIER  --------------")
    print("-" * 42)
    print("Les différentes options:")
    print("1. Verifier votre solvabilité")
    print("2. Vérifier si l'appartement est éligible")
    print("3. Quitter")
    print("-" * 42)
