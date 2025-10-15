import requests
import os
from dotenv import load_dotenv

USERNAME = 'jaganmohan'

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
    'id': 'graph1',
    'name': 'My Habit Traker',
    'unit': 'commit',
    'type': 'int',
    'color': 'ajisai',
}

headers = {
    'X-USER-TOKEN': os.getenv('MY_PIXELA_TOKEN'),
}

response = requests.post(url=graph_end_point, json=graph_parameters, headers=headers)
print(response.text)