from dateutil import parser
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def parse_timestamp(timestamp: str) -> dict:
    # Parse the ISO 8601 timestamp
    dt = parser.isoparse(timestamp)
    
    # Extract date and time
    date = dt.date()
    time = dt.time()
    
    # Store in dictionary
    result = {
        'date': date,
        'time': time
    }
    
    return result


def get_address_by_cordinates(geolocator: Nominatim, coordinates: list[tuple]):

    # List to store location results
    location_results = []

    # Iterate over coordinates and retrieve location information
    for lat, lon in coordinates:
        try:
            location = geolocator.reverse(f"{lat}, {lon}")
            location_results.append(location.address)
        except GeocoderTimedOut:
            print(f"Geocoding service timed out for coordinates: {lat}, {lon}")
            location_results.append(None)  # Or handle the error as needed

    return location_results
