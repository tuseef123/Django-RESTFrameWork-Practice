import requests
import json
URL =""

data = [{
    'name':'ali',
    'roll':1510,
    'city':'Gujrat'
},
{
    'name':'yasir',
    'roll':1511,
    'city':'Gujrat'
},
]
print(data)
json_data = json.dumps(data)
print(json_data)
r = requests.post(url = URL , data = json_data)