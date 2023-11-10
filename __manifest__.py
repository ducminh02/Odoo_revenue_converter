# -*- coding: utf-8 -*-
{
    'name': "odoo revenue converter",

    'summary': """
        This module converts Euro currency to VND
        """,

    'description': """
        This module converts Euro to VND and display it to the user.
    """,

    'author': "Minh Vu",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["crm"],

    # always loaded
    'data': [
        "views/crm_lead_views.xml"
    ],

    'qweb': [
    ],
}
