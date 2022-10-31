# This is a sample Python script.
import os
from pathlib import Path
import environ

from loan_approval_client.ClientApp import ClientApp

PATH_BASE = Path(__file__).resolve().parent
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("PATH_BASE: ", PATH_BASE)
    env_file = os.path.join(PATH_BASE, ".env")

    if os.path.exists(env_file):
        print("ENVIRONMENT FILE FOUND")
        env.read_env(env_file)

    clientApp = ClientApp(method_url=env("METHOD_URL"), service_url=env("SERVICE_URL"), wsdl_url=env("WSDL_URL"))
    clientApp.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
