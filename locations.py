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
geolocator = Nominatim(user_agent="0")

locations: list = []
coordinates: list = []

# organize data
for location in data['locations']:
    # from google we get coordinates of E7. we need to convert to the typical cordinates.
    latitude: int = int(location['latitudeE7']) / 10**7
    longitude: int = int(location['longitudeE7']) / 10**7

    # time = parse_timestamp(location['timestamp'])
    # locations.append([time, (latitude, longitude)])
    locations.append([location['timestamp'], (latitude, longitude)])
    coordinates.append((latitude, longitude))


## get data that already exists and cound the information to get the info beyond that
## cant to too many place in one pull.
try: 
    with open('locations.json', 'r') as file:
        existing_list = json.load(file)
except:
    existing_list = []

count_of_previous_searches: int = len(existing_list) if len(existing_list) else 0

addresses = get_address_by_cordinates(geolocator, coordinates[count_of_previous_searches:count_of_previous_searches+50]) ## for testing. next step without :50

for i, address in enumerate(addresses):
    i = i + count_of_previous_searches
    locations[i].append(address)

with open('locations.json', 'w') as file:
    existing_list.extend(locations[:count_of_previous_searches+50])
    json.dump(
        existing_list,
        file, ensure_ascii=False, indent=4
    )

# print(locations)