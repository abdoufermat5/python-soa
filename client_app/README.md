# Application client

---

## Description
Nous avons créé une application client qui permet de se connecter à notre serveur et de consommer les différents services qu'on a déployés.
Pour ce faire on a utilisé la librairie zeep ([https://python-zeep.readthedocs.io/en/master/](https://python-zeep.readthedocs.io/en/master/)) qui permet de consommer des services SOAP.

---
L'application client se présente sous la forme d'une console qui permet de saisir les informations relatives au demandeur de prêt et à l'appartement.

La structure de l'application est la suivante:

```
.\
│
├── .idea\
│   ├── inspectionProfiles\
│   │   ├── profiles_settings.xml
│   │   └── Project_Default.xml
│   │
│   ├── ZeppelinRemoteNotebooks\
│   │
│   ├── .gitignore
│   ├── client_app.iml
│   ├── misc.xml
│   ├── modules.xml
│   └── workspace.xml
│
├── loan_approval_client\
│   ├── model\
│   │   ├── __pycache__\
│   │   │   ├── Address.cpython-39.pyc
│   │   │   ├── Apartment.cpython-39.pyc
│   │   │   ├── Loan.cpython-39.pyc
│   │   │   ├── User.cpython-39.pyc
│   │   │   └── __init__.cpython-39.pyc
│   │   │
│   │   ├── Address.py
│   │   ├── Apartment.py
│   │   ├── Loan.py
│   │   ├── User.py
│   │   └── __init__.py
│   │
│   ├── utils\
│   │   ├── __pycache__\
│   │   │   ├── decorators.cpython-39.pyc
│   │   │   └── __init__.cpython-39.pyc
│   │   │
│   │   ├── decorators.py
│   │   ├── helpers.py
│   │   └── __init__.py
│   │
│   ├── __pycache__\
│   │   ├── ClientApp.cpython-39.pyc
│   │   └── __init__.cpython-39.pyc
│   │
│   ├── ClientApp.py
│   └── __init__.py
│
├── screenshots\
│   └── clientAppInit.png
│
├── tree_generator\
│   ├── __pycache__\
│   │   ├── cli.cpython-39.pyc
│   │   ├── rtree.cpython-39.pyc
│   │   └── __init__.cpython-39.pyc
│   │
│   ├── cli.py
│   ├── rtree.py
│   └── __init__.py
│
├── .env
├── main.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── tree.py
```
- utils: contient les fonctions utilitaires utilisées dans l'application client.

> get_client: permet de créer un client SOAP à partir des urls du WSDL, du service et de la méthode.
>> On initialise un client SOAP à partir du WSDL du service et de la méthode à appeler.(Ici on l'a fait asynchrone)

```python
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
```
- ClientApp.py: contient la classe ClientApp qui permet de gérer l'application client.
> init: initialise les attributs de la classe.

```python
    def __init__(self, wsdl_url, method_url, service_url):
        self.wsdl_url = wsdl_url
        self.method_url = method_url
        self.service_url = service_url
        self.client, self.header_value = get_client(self.wsdl_url, self.method_url, self.service_url)
```

> checkSolvability: permet de vérifier la solvabilité d'un utilisateur.
>> Ici on a utilisé asyncio pour effectuer les appels en asynchrones (Ce n'est évidemment pas obligatoire).
>><br/> Le timer est un décorateur qui permet de mesurer le temps d'exécution de la fonction.

```python
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
```

>appraise: permet de verifier si l'Appart est éligible à un prêt 
>> Pareil on a utilisé asyncio
- model: contient les classes qui représentent les différents objets utilisés dans l'application client.

Vous pouvez lancer l'application en exécutant la commande suivante:
```bash
python main.py
```