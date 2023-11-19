from requests import get

BASE_URL = "http://api.exchangeratesapi.io/v1/"
API_KEY = "d84f806e4738c9c256647db53c4c0de9"


def get_currencies(currency):
    endpoint = f"latest?access_key={API_KEY}"
    url = BASE_URL + endpoint

    # Check if json_response is not None
    if get(url).json() is None:
        print("Error: JSON response is None.")
        return None

    # Extract rates from the JSON response
    rates = get(url).json().get("rates")

    # Check if rates is not None
    if rates is None:
        print("Error: Rates not found in the provided JSON response.")
        return None

    if currency in rates:
        # Perform the conversion
        target_rate = rates[currency]
        return target_rate
    else:
        print(f"{currency} rate not found in the provided JSON response.")
        return None


rate = get_currencies('VND')
print(rate)
