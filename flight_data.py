from datetime import date, datetime, timedelta

import requests

API_KEY = ""
API_SECRET = ""
ACCES_TOKEN = ""


class FlightData:

    def __init__(self,iata_codes):
        self.iata_codes = iata_codes
        self.return_date = None
        self.departure_date = None
        self.calculate_dates()

        self.origin_code = "LON"
        self.no_of_persons = 1

        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET
        self.token = ACCES_TOKEN

    def search_cheapest_flights(self):

        cheapest_flights=[]
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        for iata_code in self.iata_codes:
            print(f"Getting flights for {iata_code}...")
            params = {
                "originLocationCode": self.origin_code,
                "destinationLocationCode": iata_code,
                "departureDate": self.departure_date,
                "returnDate": self.return_date,
                "adults": 1,
                "nonStop": "true",
                "max": 200,
            }

            response = requests.get(url, headers=headers, params=params)
            data = response.json()

            cheapest_flight = self.get_cheapest_flight(data['data'])
            print(f"{iata_code}: € {cheapest_flight}")
            cheapest_flights.append(cheapest_flight)

        return cheapest_flights



    def get_cheapest_flight(self,data):
        cheapest_flight = None
        lowest_price = float('inf')

        for flight in data:
            total_price = float(flight['price']['total'])
            if total_price < lowest_price:
                lowest_price = total_price
                cheapest_flight = flight

        if lowest_price == float('inf'):
            return 0.0
        else:
            return lowest_price




    def calculate_dates(self):
        tomorrow = datetime.now() + timedelta(days=1)
        six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

        self.departure_date = tomorrow.strftime('%Y-%m-%d')
        self.return_date = six_month_from_today.strftime('%Y-%m-%d')

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

