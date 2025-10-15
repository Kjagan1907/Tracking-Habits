import requests
import os
from dotenv import load_dotenv

#create a new pixela user
end_point = 'https://pixe.la/v1/users'
load_dotenv()  # Automatically reads .env in project folder
load_dotenv(dotenv_path="token.env")  # <-- specify your file
paramters = {
    'token': os.getenv('MY_PIXELA_TOKEN'),
    'username': 'jaganmohan',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',    
}

response = requests.post(url=end_point, json=paramters)
print(response.text)