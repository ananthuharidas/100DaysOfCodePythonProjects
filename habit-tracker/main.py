import requests
from datetime import datetime,timedelta
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "ananthuharidas"
TOKEN = "jhbfdasjchxzbcaskdbj"
GRAPH_ID = "graph1"
'''Create an account'''
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=pixela_parameters)
print(response.text)

'''Create a graph'''

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": GRAPH_ID,
    "name": "Yoga Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
print(response.text)

'''Add data/pixel to the graph'''
add_data_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
yesterday = datetime.today() - timedelta(days=1)
add_data_parameters = {
    "quantity": input("How many minutes did you pratice today?"),
    "date": yesterday.strftime("%Y%m%d"),
}

response = requests.post(url=add_data_endpoint, json=add_data_parameters, headers=headers)
print(response.text)

modify_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"
update_pixel_parameters = {
    "quantity": "13"
}
response = requests.put(url=modify_pixel_endpoint, json=update_pixel_parameters, headers=headers)
print(response.text)

'''Delete a pixel'''

response = requests.delete(url=modify_pixel_endpoint, headers=headers)
print(response.text)