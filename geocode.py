from geopy.geocoders import Nominatim   # imported library

geolocator = Nominatim(user_agent="ssw540_assignment", timeout=10)  # geocoder to search for address + time period for it to work

address = input("enter a US address: ") # user address entry

location = geolocator.geocode(address, country_codes="us")  # find gps coordinates

if location:    # check if address was found and if so print latitude and longitude
    print("latitude:", location.latitude)
    print("longitude:", location.longitude)
else:   # if not found
    print("address not found")

#github link: