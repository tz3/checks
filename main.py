# -*- coding: utf-8 -*-
from pprint import pprint

import requests

authorize_data = {"email": "email@gmail.com", "name": "Your Name", "phone": "+70000000000"}
password = 000000
# %%
# registration
url = 'https://proverkacheka.nalog.ru:9999/v1/mobile/users/signup'
r = requests.post(url, json=authorize_data)
# %%
# login
url = 'https://proverkacheka.nalog.ru:9999/v1/mobile/users/login'
r = requests.get(url, auth=(authorize_data['phone'].encode('utf-8'), password))
r.status_code
# %%
# reset password
url = 'https://proverkacheka.nalog.ru:9999/v1/mobile/users/restore'
restore_data = {"phone": "+79033885735"}
r = requests.post(url, json=restore_data)
# %%

qr_code = 't=20190406T104300&s=641.93&fn=9289000100110273&i=80715&fp=1246602073&n=1'
t = '20190406T104300'
s = 641.93
fn = 9289000100110273
i = 80715
fp = 1246602073
n = 1

fiscalNumber = fn
fiscalDocument = i
fiscalSign = fp
url = f"https://proverkacheka.nalog.ru:9999/v1/inns/*/kkts/*/fss/{fiscalNumber}/tickets/{fiscalDocument}?fiscalSign={fiscalSign}&sendToEmail=no"

headers = {"device-id": '', 'device-os': ''}
r = requests.get(url, auth=(authorize_data['phone'].encode('utf-8'), password), headers=headers)
pprint(r.json())
print(r.text)
