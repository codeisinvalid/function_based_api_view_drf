import requests 
import json

URL = "http://127.0.0.1:8000/student-api/"

def get_data(id=None):
    data = {}
    if id is not None:
        url_with_id = f"{URL}?id={id}"
        r = requests.get(url= url_with_id)
    else:
        r = requests.get(url= URL)
    data = r.json()
    print(data)

# get_data(2)

def post_data():
    data = {
        'name':'Sujita Kshettry',
        'roll':15,
        'city':'USA',
        'grade':'B.Economics'
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

# post_data()

def update_data():

    data = {
        'id':2,
        'name':'Alan Neupane',
        'roll':4565,
        'city':'Palpa',
        'grade':'B.Tech'
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.put(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

update_data()

def delete_data():

    data = {'id': 1}
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.delete(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

# delete_data()



