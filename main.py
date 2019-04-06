# -*- coding: utf-8 -*-

import pyzbar.pyzbar as pyzbar
from requests import Response
import cv2
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'https://proverkacheka.nalog.ru:9999/v1'
authorize_data = {"email": "email", "name": "name", "phone": "phone"}
username = authorize_data['phone']
password = 1231231
image_path = 'IMAGE 2019-04-06 13:16:58.jpg'
auth = HTTPBasicAuth(username.encode('utf-8'), password)


def sign_up(email: str, name: str, phone: str) -> Response:
    sign_up_url = '/mobile/users/signup'
    authorize_data: dict = {"email": email, "name": name, "phone": phone}
    url = BASE_URL + sign_up_url
    response = requests.post(url, json=authorize_data)
    return response


def sign_in(auth: HTTPBasicAuth) -> Response:
    sign_in_url = '/mobile/users/login'
    url = BASE_URL + sign_in_url
    response = requests.get(url, auth=auth)
    return response


def reset_password(phone: str) -> Response:
    reset_password_url = '/mobile/users/restore'
    url = BASE_URL + reset_password_url
    restore_data = {"phone": phone}
    response = requests.post(url, json=restore_data)
    return response


def get_information(auth: HTTPBasicAuth, fiscal_number: str, fiscal_document: str,
                    fiscal_sign: str) -> Response:
    url = BASE_URL + f'/inns/*/kkts/*/fss/{fiscal_number}/tickets/{fiscal_document}?fiscalSign={fiscal_sign}&sendToEmail=no'
    headers = {"device-id": '', 'device-os': ''}
    response = requests.get(url, auth=auth, headers=headers)
    return response


def qr_scan(img_path: str) -> pyzbar.Decoded:
    im = cv2.imread(img_path)
    decoded_objects = pyzbar.decode(im)
    return decoded_objects


# object_str = qr_scan(image_path)
def parse_qr_string(line: pyzbar.Decoded) -> tuple:
    objectives = line[0].data.decode("utf-8").split('&')
    fn = objectives[2].split('=')[1]
    i = objectives[3].split('=')[1]
    fp = objectives[4].split('=')[1]
    fiscal_number = fn
    fiscal_document = i
    fiscal_sign = fp
    return fiscal_number, fiscal_document, fiscal_sign


def parse_items(api_data: dict) -> list:
    return api_data.get('document', {}).get('receipt', {}).get('items', [])
