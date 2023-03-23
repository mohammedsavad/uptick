# -*- coding: utf-8 -*-
{
    'name': 'Receipt Print Restriction',
    'version': '16.0.1.0.0',
    'summary': 'Receipt Print Restriction',
    'category': 'Productivity',
    'depends': ['base', 'point_of_sale'],
    'author': '',
    'maintainer': '',
    'company': '',
    'website': '',
    'data': [
        'views/pos.config.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'receipt_print_restriction/static/src/js/restrict_printing.js'
        ],
    },
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False
}
