
from wsgiref import headers
import requests
import json


URL = "http://127.0.0.1:8000/studentapi/"

def get_id(id=None):
    data= {}
    if id is not None:
        data = {'id':id}
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.get(url= URL,headers = headers, data = json_data)    
    data = r.json()
    print(data)
    
# get_id()


def post_create():
    data = {
        'name': 'haWk',
        'age' : 1999,
        'address': 'china'

    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url= URL,headers = headers, data = json_data)
    data = r.json()
    print(data)
post_create()

def post_update():
    data = {
        'id': 12,
        'name': 'Tony Stark',
        'age' : 65,
        'address': 'butwal'

    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url= URL,headers = headers, data = json_data)
    data = r.json()
    # print(data)


# post_update()

def del_data(id):
    data ={'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.delete(url = URL, headers = headers, data = json_data)
    data =  r.json()
    print(data)
# del_data(12)

    