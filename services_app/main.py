# Main
import logging
import os
from pathlib import Path
from wsgiref.simple_server import make_server

from spyne.application import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from services.home_appraisal.HomeAppraisalService import AppraisalService
from services.credit_check.CreditCheckService import CreditCheckService
import environ

PATH_BASE = Path(__file__).resolve().parent
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

if __name__ == '__main__':
    print("PATH_BASE: ", PATH_BASE)
    env_file = os.path.join(PATH_BASE, "services/.env")

    if os.path.exists(env_file):
        print("ENVIRONMENT FILE FOUND")
        env.read_env(env_file)
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
    app = Application([CreditCheckService, AppraisalService], 'datascale.services.loan_approval.http',
                      in_protocol=Soap11(validator='lxml'),
                      out_protocol=Soap11(),
                      )
    # We then wrap the Spyne application with its wsgi wrapper
    wsgi_app = WsgiApplication(app)
    # We now register the WSGI application as the handler to the wsgi server, and run the http server:
    server = make_server(host=env("HOST", default="localhost"), port=env.int("PORT", default=8000), app=wsgi_app)
    logging.info(f'listening on http://{env("HOST", default="localhost")}:{env("PORT", default=8000)}')
    logging.info(f'wsdl is at: http://{env("HOST", default="localhost")}:{env("PORT", default=8000)}/app/?wsdl')

    server.serve_forever()
