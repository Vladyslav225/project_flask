import json
import requests

response = requests.post('http://0.0.0.0:5274/wine_list/', json={'name': 'Vladaaaasssss', 'last_name': 'YarAAA'})
print(response)
print('response')

#TODO requests.get
#TODO requests.put
#TODO requests.tag
#TODO requests.delete
