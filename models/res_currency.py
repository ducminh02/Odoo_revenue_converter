from odoo import models, fields, api, exceptions
from requests import get
import datetime
import logging

BASE_URL = "http://api.exchangeratesapi.io/v1/"

_logger = logging.getLogger(__name__)


class ResCurrency(models.Model):
    _inherit = 'res.currency'

    def get_currencies(self):
        api_key = self.env['ir.config_parameter'].sudo().get_param("currency_realtime_ api")
        print(api_key)
        endpoint = f"latest?access_key={api_key}"

        url = BASE_URL + endpoint
        # Check if json_response is not None
        if get(url).json() is None:
            print("Error: JSON response is None.")
            return None

        # Extract rates from the JSON response
        rates = get(url).json().get("rates")

        # Check if rates is not None
        if rates is None:
            raise exceptions.ValidationError("Rates not found in the provided JSON response")

        if self.name in rates:
            # Perform the conversion
            print(rates)
            print(self.name)
            target_rate = rates[self.name]
            curr_real_time = {
                'rate': target_rate
            }
            print(self.date)
            print(datetime.date.today())
            if self.date == datetime.date.today():
                _logger.info("update record")
                rate_record = self.env["res.currency.rate"].search(
                    [("currency_id", "=", self.id),
                        ("name", "=", datetime.date.today())],
                    limit=1

                )
                self.write({
                    'rate_ids': [(1, rate_record.id, curr_real_time)]
                })
            else:
                _logger.info("create new record")
                self.write({
                    'rate_ids': [(0, 0, curr_real_time)]
                })
            print('Success')
        else:
            print(f"{self.name} rate not found in the provided JSON response.")
            raise exceptions.ValidationError(f"{self.name} rate not found in the provided JSON response.")

    @api.model
    def automate_currency_update(self):
        currencies = self.env["res.currency"].search([])
        for curr in currencies:
            curr.get_currencies()
