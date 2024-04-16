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

get_data(2)

def post_data():
    data = {
        'name':'Shantee Banstola',
        'roll':290,
        'city':'USA',
        'grade':'B.Economics'
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
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
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():

    data = {'id': 6}
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)

# delete_data()



