import csv
import logging
import os
import json
from time import sleep

import requests
from dotenv import load_dotenv

load_dotenv()

AIM_API_URL = os.environ.get('AIM_API_URL')
GESTOR_DEPORTIVO_API_URL = os.environ.get('GESTOR_DEPORTIVO_API_URL')

logging.basicConfig(filename='request_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def create_json_log(log):
    with open('request_log.json', 'a') as file:
        # write with double quotes
        file.write(json.dumps(log))
        file.write("\n")


json_logs = []

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

                sleep(5)

                if response.status_code == 200:
                    log = f"Endpoint {url} - Usuario {user['usuario']} - Status Code: {response.status_code}"
                    logging.info(log)
                    json_log = {
                        "endpoint": url,
                        "usuario": user['usuario'],
                        "status_code": response.status_code,
                        "response": "OK"
                    }
                    json_logs.append(json_log)
                    print(log)
                else:
                    log = f"Endpoint {url} - Usuario {user['usuario']} - Status Code: {response.status_code} - Response {response.text}"
                    json_log = {
                        "endpoint": url,
                        "usuario": user['usuario'],
                        "status_code": response.status_code,
                        "response": response.json()['mensaje']
                    }
                    json_logs.append(json_log)
                    logging.info(log)
                    print(log)

            except requests.exceptions.RequestException as e:
                logging.error(f"Login - Error: {e}")
                print(f"Login - Error: {e}")
                json_log = {
                    "endpoint": url,
                    "usuario": user['usuario'],
                    "status_code": 500,
                    "response": "Error"
                }

                json_logs.append(json_log)

    create_json_log(json_logs)
