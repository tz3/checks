# checks
```python
from main import *
response = sign_up(email, name, password)
# check the response's status code
# https://habr.com/ru/post/358966/?_ga=2.63021999.1021629629.1554542391-1414310797.1549829968
# try to sign in
auth = HTTPBasicAuth(username.encode('utf-8'), password)
response = sign_in(auth)
# the same as above
    
```
1. Fix `config.ini`
2. `cp config.ini.example config.ini`



```
fiscal_number, fiscal_document, fiscal_sign = parse_qr_string(qr_scan(image_path))
response = get_information(auth, fiscal_number, fiscal_document, fiscal_sign)
if response.status_code == 200:
    item = parse_items(res.json())

```