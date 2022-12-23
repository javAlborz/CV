import requests

# Set the API endpoint URL
api_endpoint = "https://my-api.com/endpoint"

# Set the request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer my-api-key"
}

# Set the request parameters (if any)
params = {
    "param1": "value1",
    "param2": "value2"
}

# Make the API request and store the response
response = requests.get(api_endpoint, headers=headers, params=params)

# Check the status code of the response
if response.status_code == 200:
    # If the request was successful, process the response data
    response_data = response.json()
    # Do something with the response data...
else:
    # If the request was not successful, print the error message
    print(f"Error: {response.text}")