import requests
import os
from dotenv import load_dotenv
from datetime import datetime

USERNAME = 'jaganmohan'
GRAPH_ID = 'graph1'

#create a new pixela user
user_end_point = 'https://pixe.la/v1/users'
load_dotenv()  # Automatically reads .env in project folder
load_dotenv(dotenv_path="token.env")  # <-- specify your file
create_user_paramters = {
    'token': os.getenv('MY_PIXELA_TOKEN'),
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',    
}

# creating a pixelation graph
graph_end_point = f"{user_end_point}/{USERNAME}/graphs"

graph_parameters = {
    'id': GRAPH_ID,
    'name': 'My Habit Traker',
    'unit': 'commit',
    'type': 'int',
    'color': 'ajisai',
}

headers = {
    'X-USER-TOKEN': os.getenv('MY_PIXELA_TOKEN'),
}

# adding value to the graph
add_to_graph_end_point = f"{graph_end_point}/{GRAPH_ID}"
date_entry = datetime(year=2025, month=10, day=9)

add_to_graph_paramters = {
    'date': date_entry.strftime('%Y%m%d'),
    'quantity': '10'
}
response = requests.post(url=add_to_graph_end_point, json=add_to_graph_paramters, headers=headers)
print(response.text)