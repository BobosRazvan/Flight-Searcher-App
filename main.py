from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_manager = DataManager()
sheet_data = data_manager.fetch_data()


cities = [row['city'] for row in sheet_data]
iata_codes = [row['iataCode'] for row in sheet_data]
lowest_prices = [row['lowestPrice'] for row in sheet_data]

flight_searcher = FlightSearch(cities)

flight_data = FlightData(iata_codes)
cheapest_flights = flight_data.search_cheapest_flights()

for my_flights,online_flights in zip(flight_data,cheapest_flights):
    if online_flights<my_flights:
        print(f"Found a cheaper flight with {my_flights-online_flights}")

