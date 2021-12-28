import json
import requests

response = requests.post('http://0.0.0.0:5254/user/', json={'name': 'Vlad', 'last_name': 'Yar'})
print(response)
print('response')