from odoo.tests import TransactionCase, tagged
import pytest
import datetime


@tagged('-standard', 'post_install', 'curr')
class TestResCurrency(TransactionCase):
    def setUp(self):
        super(TestResCurrency, self).setUp()
        self.my_model = self.env["res.currency"]

    def test_currency_not_empty(self):

        currency = self.my_model.search([
            ("name", "=", "VND")
        ])

        before_modification_datetime = currency.write_date

        currency.get_currencies()

        self.assertEqual(currency.name, "VND")
        self.assertEqual(currency.symbol, "₫")
        self.assertNotEqual(currency.rate, 1)
        self.assertNotEqual(currency.rate_ids, None)
        self.assertEqual(currency.date, datetime.date.today())

        after_modification_datetime = currency.write_date

        self.assertNotEqual(before_modification_datetime, after_modification_datetime)
