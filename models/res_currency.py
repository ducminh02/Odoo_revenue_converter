from odoo import models, fields, api
from requests import get

BASE_URL = "http://api.exchangeratesapi.io/v1/"
API_KEY = "d84f806e4738c9c256647db53c4c0de9"


class ResCurrency(models.Model):
    _inherit = 'res.currency'

    def get_currencies(self):
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

        if self.name in rates:
            # Perform the conversion
            target_rate = rates[self.name]
            curr_real_time = {
                'rate': target_rate
            }
            self.write({
                'rate_ids': [(0, 0, curr_real_time)]
            })
            print('Success')
        else:
            print(f"{self.name} rate not found in the provided JSON response.")
