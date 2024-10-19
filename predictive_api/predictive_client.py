import requests

def get_predictive_maintenance(machine_data):
    api_url = "https://predictive-api.com/maintenance"
    response = requests.post(api_url, json=machine_data)
    return response.json()  # Assuming the API returns JSON
