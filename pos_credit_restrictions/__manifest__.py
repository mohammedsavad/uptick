# -*- coding: utf-8 -*-
{
    'name': 'POS Credit Sale Restriction',
    'version': '16.0.1.0.0',
    'summary': 'POS Credit Sale Restriction',
    'category': 'Productivity',
    'depends': ['base', 'point_of_sale'],
    'author': '',
    'maintainer': '',
    'company': '',
    'website': '',
    'data': [
        'views/res_config_settings.xml'
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_credit_restrictions/static/src/js/PaymentScreen.js',
            'pos_credit_restrictions/static/src/xml/PaymentScreen.xml',
        ],
    },
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False
}
