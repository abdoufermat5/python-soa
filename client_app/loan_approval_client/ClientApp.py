import asyncio
import json
import time

from loan_approval_client.model.Address import Address
from loan_approval_client.model.Apartment import Apartment
from loan_approval_client.model.Loan import Loan
from loan_approval_client.model.User import User
from loan_approval_client.utils.decorators import timer
from loan_approval_client.utils.helpers import get_client, present_menu, ComplexEncoder, input_user_info, \
    input_loan_info

user = User()
apartment = Apartment()
loan = Loan()
address = Address()

YES_OR_NO = ["O", "N"]


class ClientApp:
    def __init__(self, wsdl_url, method_url, service_url, result=None):
        if result is None:
            result = {}
        self.wsdl_url = wsdl_url
        self.method_url = method_url
        self.service_url = service_url
        self.client, self.header_value = get_client(self.wsdl_url, self.method_url, self.service_url)
        self.result = result

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
        print("***************** Réponse: ******************\n\t\t", future.result()[0])
        print("-" * 42)
        self.save_result("solvabilityStatus", future.result()[0])
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
        print("-" * 42)
        print("***************** Réponse: ******************\n\t\t", future.result()[0])
        print("-" * 42)
        self.save_result("appraiseStatus", future.result()[0])
        return future.result()[0]

    def checkApproval(self, user, solvabilityStatus, appraiseStatus):
        if solvabilityStatus == "Approved" and appraiseStatus == "Approved":
            return f"Mr/Mme {user.name} votre demande de prêt est approuvée"
        elif solvabilityStatus == "Denied" or appraiseStatus == "Denied":
            return f"Mr/Mme {user.name} votre demande de prêt est rejetée"

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
            if user.is_empty():
                name, num_ssn, street, city, state, email = input_user_info()
                address.set_address(street, city, state)
                user.set_user(name=name, num_ssn=num_ssn, email=email, address=address)
            else:
                print("Vous avez déjà rempli les informations de votre profil")
                print("Voulez-vous les modifier? (O/N)")
                c = input("-->")
                while c not in YES_OR_NO:
                    print("Mauvais choix, veuillez réessayer!!")
                    print("Voulez-vous les modifier? (O/N)")
                    c = input("-->")
                if c == "O":
                    print(user)
                    name, num_ssn, street, city, state, email = input_user_info()
                    address.set_address(street, city, state)
                    user.set_user(name=name, num_ssn=num_ssn, email=email, address=address)
                print("Votre solvabilité est en cours de vérification...")
            self.checkSolvability(user)
        elif choice == 2:
            if loan.is_empty():
                appart_price, pret, surface, description = input_loan_info()
                apartment.set_apartment(price=appart_price, address=address, surface=surface, description=description)
                loan.set_loan(borrower=user, apartment=apartment, loan_amount=pret)
            else:
                print("Vous avez déjà rempli les informations de votre prêt et de l'appartement")
                print("Voulez-vous les modifier? (O/N)")
                c = input("-->")
                while c not in YES_OR_NO:
                    print("Mauvais choix, veuillez réessayer!!")
                    print("Voulez-vous les modifier? (O/N)")
                    c = input("-->")
                if c == "O":
                    print(loan)
                    appart_price, pret, surface, description = input_loan_info()
                    apartment.set_apartment(price=appart_price, address=address, surface=surface,
                                            description=description)
                    loan.set_loan(borrower=user, apartment=apartment, loan_amount=pret)
                print("Votre prêt est en cours d'évaluation...")
            self.appraise(loan)
        elif choice == 3:
            if self.result.get("solvabilityStatus") is not None and self.result.get("appraiseStatus") is not None:
                print(self.checkApproval(user, self.result.get("solvabilityStatus"), self.result.get("appraiseStatus")))
            else:
                print("Vous devez d'abord vérifier votre solvabilité et évaluer votre prêt")
                present_menu()
                print("(*) Veuillez choisir les options 1 et 2 avant de choisir l'option 3")
        print("Voulez-vous continuer? (O/N)")
        res = input("Entrez votre choix: ")
        while res not in YES_OR_NO:
            print("Mauvais choix, veuillez réessayer!!")
            print("Voulez-vous continuer? (O/N)")
            res = input("Entrez votre choix: ")
        if res == "O":
            self.run()
        else:
            print("Merci d'avoir utilisé l'application!!")

    def save_result(self, key, value):
        self.result[str(key)] = value
