# Application services

---
## Description
Nous avons créé une application services qui permet de déployer les différents services SOAP que nous avons créés.
Pour ce faire on a utilisé la librairie spyne ([https://spyne.io/](https://spyne.io/)) qui permet de créer des services SOAP.



---

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
│   ├── misc.xml
│   ├── modules.xml
│   ├── services_app.iml
│   └── workspace.xml
│
├── model\
│   ├── __pycache__\
│   │   ├── Address.cpython-39.pyc
│   │   ├── Appartment.cpython-39.pyc
│   │   ├── Loan.cpython-39.pyc
│   │   ├── User.cpython-39.pyc
│   │   └── __init__.cpython-39.pyc
│   │
│   ├── Address.py
│   ├── Appartment.py
│   ├── Loan.py
│   ├── User.py
│   └── __init__.py
│
├── services\
│   ├── credit_check\
│   │   ├── __pycache__\
│   │   │   ├── CreditCheckService.cpython-39.pyc
│   │   │   └── __init__.cpython-39.pyc
│   │   │
│   │   ├── CreditCheckService.py
│   │   └── __init__.py
│   │
│   ├── home_appraisal\
│   │   ├── __pycache__\
│   │   │   ├── HomeAppraisalService.cpython-39.pyc
│   │   │   └── __init__.cpython-39.pyc
│   │   │
│   │   ├── HomeAppraisalService.py
│   │   └── __init__.py
│   │
│   ├── loan_approval\
│   │   ├── LoanApprovalService.py
│   │   └── __init__.py
│   │
│   ├── __pycache__\
│   │   └── __init__.cpython-39.pyc
│   │
│   ├── .env
│   └── __init__.py
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
├── main.py
├── Pipfile
├── Pipfile.lock
├── README.md
├── test.md
└── tree.py
```

