import json
from geopy.geocoders import Nominatim
from utils import *

# Define the file name
file_name = '../Records.json'

# Open the JSON file and load its content
# will be changed to using google api and get the data for the user
with open(file_name, 'r') as file:
    data = json.load(file)

# # Initialize the Nominatim geocoder
geolocator = Nominatim(user_agent="00")

locations: list = []
coordinates: list = []

# organize data
for location in data['locations']:
    # from google we get coordinates of E7. we need to convert to the typical cordinates.
    latitude: int = int(location['latitudeE7']) / 10**7
    longitude: int = int(location['longitudeE7']) / 10**7

    time = parse_timestamp(location['timestamp'])
    locations.append([time, (latitude, longitude)])
    coordinates.append((latitude, longitude))


# Initialize Nominatim geocoder
geolocator = Nominatim(user_agent="my_app")

addresses = get_address_by_cordinates(geolocator, coordinates[:50]) ## for testing. next step without :50

for i, address in enumerate(addresses):
    locations[i].append(address)


print(locations)

