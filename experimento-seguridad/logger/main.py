import requests
import time
import logging
import csv
from dotenv import load_dotenv
import os

load_dotenv()

endpoints = [
    'http://127.0.0.1:3001'
]

AIM_API_URL = os.environ.get('AIM_API_URL')
GESTOR_DEPORTIVO_API_URL = os.environ.get('GESTOR_DEPORTIVO_API_URL')

logging.basicConfig(filename='request_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":

    with open('users.csv', 'r') as file:
        users = csv.DictReader(file)

        for user in users:
            try:
                login = requests.post(AIM_API_URL + '/login',
                                      json={"usuario": user['usuario'], "password": user['password']})

                print(f"Login {user['usuario']} - Status Code: {login.status_code}")

                url = GESTOR_DEPORTIVO_API_URL + '/consultar-perfil-deportivo'
                response = requests.get(url,
                                        headers={"Authorization": f"Bearer {login.json().get('token')}"})

                if response.status_code == 200:
                    log = f"Endpoint {url} - Usuario {user['usuario']} - Status Code: {response.status_code}"
                    logging.info(log)
                    print(log)
                else:
                    log = f"Endpoint {url} - Usuario {user['usuario']} - Status Code: {response.status_code} - Response {response.text}"
                    logging.info(log)
                    print(log)

            except requests.exceptions.RequestException as e:
                logging.error(f"Login - Error: {e}")
                print(f"Login - Error: {e}")
                exit(1)
