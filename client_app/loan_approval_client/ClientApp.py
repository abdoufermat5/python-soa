import asyncio
import json
import time

from loan_approval_client.model.Address import Address
from loan_approval_client.model.Apartment import Apartment
from loan_approval_client.model.Loan import Loan
from loan_approval_client.model.User import User
from loan_approval_client.utils.decorators import timer
from loan_approval_client.utils.helpers import get_client, present_menu, ComplexEncoder


class ClientApp:
    def __init__(self, wsdl_url, method_url, service_url):
        self.wsdl_url = wsdl_url
        self.method_url = method_url
        self.service_url = service_url
        self.client, self.header_value = get_client(self.wsdl_url, self.method_url, self.service_url)

    @timer
    def checkSolvability(self, user):
        loop = asyncio.get_event_loop()
        result = self.client.service.checkSolvability(
            user=json.loads(json.dumps(user.__dict__, cls=ComplexEncoder)),
            _soapheaders=[self.header_value]
        )
        task = [result]
        future = asyncio.gather(*task, return_exceptions=True)
        loop.run_until_complete(future)
        loop.run_until_complete(self.client.transport.aclose())
        print("***************** Réponse: ******************\n", future.result()[0])
        print("-" * 42)
        return future.result()[0]

    @timer
    def appraise(self, loan):
        loop = asyncio.get_event_loop()
        result = self.client.service.appraise(
            loan=json.loads(json.dumps(loan.__dict__, cls=ComplexEncoder)),
            _soapheaders=[self.header_value]
        )
        task = [result]
        future = asyncio.gather(*task, return_exceptions=True)

        loop.run_until_complete(future)
        loop.run_until_complete(self.client.transport.aclose())
        print("-" * 42)
        print("***************** Réponse: ******************\n", future.result()[0])
        print("-" * 42)
        return future.result()[0]

    def run(self):
        present_menu()
        choice = input("Entrez votre choix: ")
        while not choice.isdigit() or int(choice) not in [1, 2, 3]:
            print("Mauvais choix, veuillez réessayer!!")
            present_menu()
            choice = input("Entrez votre choix: ")
        self.execute_choice(int(choice))

    def execute_choice(self, choice):
        print("Vous avez choisi l'option: ", choice)
        if choice == 1:
            name = input("Entrez votre nom: \n-->")
            print("\n")
            num_ssn = input("Entrez votre numéro de sécurité sociale: \n-->")
            street = input("Entrez votre rue: \n-->")
            city = input("Entrez votre ville: \n-->")
            state = input("Entrez votre Pays: \n-->")
            email = input("Entrez votre email: \n-->")
            user = User(name=name, num_ssn=num_ssn, email=email, address=Address(street=street, state=state, city=city))
            self.checkSolvability(user)
        elif choice == 2:
            appart_price = input("Entrez le prix de l'appartement: \n-->")
            pret = input("Entrez le montant du prêt: \n-->")
            surface = input("Entrez la surface de l'appartement: \n-->")
            description = input("Entrez la description de l'appartement: \n-->")
            loan = Loan(apartment=Apartment(price=appart_price, surface=surface,
                                            description=description, address=Address()),
                        loan_amount=pret)
            self.appraise(loan)
        print("Voulez-vous continuer? (O/N)")
        res = input("Entrez votre choix: ")
        while res not in ["O", "N"]:
            print("Mauvais choix, veuillez réessayer!!")
            print("Voulez-vous continuer? (O/N)")
            res = input("Entrez votre choix: ")
        if res == "O":
            self.run()
        else:
            print("Merci d'avoir utilisé l'application!!")
