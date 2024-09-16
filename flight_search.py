import requests

API_KEY = ""
API_SECRET = ""
ACCES_TOKEN = ""

class FlightSearch:

    def __init__(self,flight_list):
        self.flight_list = flight_list
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET
        self.token = ACCES_TOKEN


    def return_iata_codes_testing(self):
        iata_codes=[]
        iata_codes_lenght = len(self.flight_list)
        for i in range(0,iata_codes_lenght):
            iata_codes.append("TESTING")
        return iata_codes

    def return_iata_codes(self):

        url = ""

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        iata_codes = []
        for city in self.flight_list:
            params = {
                "max": "2",
                "include": "AIRPORTS",
                "keyword": city
            }

            response = requests.get(url, headers=headers, params=params)
            data = response.json()
            iata_codes.append(data["data"][0]['iataCode'])



        return iata_codes


    def get_new_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        data = {
            "grant_type": "client_credentials",
            "client_id": self.API_KEY,
            "client_secret": self.API_SECRET
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        response = requests.post(url, headers=headers, data=data)
        print(response.text)

        if response.status_code == 200:
            access_token = response.json().get('access_token')
            print("Access token:", access_token)
            return access_token
        else:
            print("Failed to get access token. Server responded with:", response.content)
            return None