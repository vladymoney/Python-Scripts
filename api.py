# import requests
# #SPEEEDY INTEGRATION
# # Define the Speedy API credentials and base URL
# SPEEDY_API_USERNAME = '1995892'
# SPEEDY_API_PASSWORD = '8721425144'
# SPEEDY_API_BASE_URL = 'https://api.speedy.bg/v1/'
# LANGUAGE = 'BG'

# # Define the request payload for finding offices by city name
# payload = {
#     'userName': SPEEDY_API_USERNAME,
#     'password': SPEEDY_API_PASSWORD,
#     'language': LANGUAGE,
#     'countryId': 100,  # Country ID for Bulgaria
#     'name': 'PETRICH'    # Replace with the desired city name (e.g., 'SOFIA')
# }

# # Define the API endpoint for finding offices
# endpoint = SPEEDY_API_BASE_URL + 'location/office/'

# # Make a POST request to the Speedy API to get offices by city name
# response = requests.post(endpoint, json=payload)

# # Print the response status code
# print("Response Status Code:", response.status_code)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()

#     # Check if the 'offices' key exists in the response
#     if 'offices' in data:
#         # Loop through the offices and print their names
#         for office in data['offices']:
#             print(office['name'])  # Print the name of each office
#     else:
#         print("No offices found.")
# else:
#     print(f"Error: {response.status_code}")



import requests

# Econt API credentials and base URL
ECONT_API_USERNAME = 'prolux97@gmail.com'
ECONT_API_PASSWORD = 'Stanimira135'
ECONT_API_BASE_URL = 'https://ee.econt.com/services/Nomenclatures/NomenclaturesService.getOffices.json'
LANGUAGE = 'BG'

# Define the request payload with only essential parameters
payload = {
    'username': ECONT_API_USERNAME,
    'password': ECONT_API_PASSWORD,
    'language': LANGUAGE,
    'countryCode': 'BGR',  # Bulgaria's ISO Alpha-3 code
    'cityID': 4        # Static city ID, make sure this is correct
}

# Make the API request
response = requests.post(ECONT_API_BASE_URL, json=payload)

# Debugging: Inspect the response
print("Response Status Code:", response.status_code)

# Check if the response is empty
if response.text.strip():
    print("Non-empty response received.")

    try:
        # Attempt to parse the JSON response (if possible)
        data = response.json()

        # Check if offices exist in the response
        if 'offices' in data:
            print("Offices Found:")
            for office in data['offices']:
                # Only print the name of each office
                print(f"Name: {office.get('name')}")
                print("-" * 40)
        else:
            print("No offices found in the JSON response.")
    except requests.exceptions.JSONDecodeError:
        print("Failed to parse JSON. The raw response is not in JSON format.")
        print("Raw Response Body:", response.text)
else:
    print("Empty Response Content. Raw response body:", response.text)


