import json
import os

import requests
from pprint import pprint

BEARER_TOKEN = ""
class DataManager:

    def __init__(self):
        self.endpoint = "https://api.sheety.co/089fc79b999338a8a29e08e988fc3fd4/razvan'sFlightDeals/prices"
        #load_dotenv()
        self.bearer_token = BEARER_TOKEN
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.bearer_token,
        }
        self.headers = headers
        self.data = {}

    def fetch_data(self):
        response = requests.get(url=self.endpoint, headers=self.headers)
        data = response.json()
        self.data = data['prices']
        return data['prices']

    def update_iata_codes(self, iata_codes):
        for city_data, iata_code in zip(self.data, iata_codes):
            object_id = city_data['id']
            url = f""

            data = {"price": {"iataCode": iata_code}}
            response = requests.put(url, headers=self.headers, data=json.dumps(data))
