# -*- coding: utf-8 -*-
{
    'name': 'POS Disable Refund',
    'version': '16.0.1.0.0',
    'summary': 'POS Disable Refund for users',
    'category': 'Productivity',
    'depends': ['base', 'point_of_sale'],
    'author': '',
    'maintainer': '',
    'company': '',
    'website': '',
    'data': [
        'views/pos_order.xml',
        'views/res_config_settings.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_disable_refund/static/src/js/RefundButton.js',
            'pos_disable_refund/static/src/js/NumpadWidget.js',
            'pos_disable_refund/static/src/js/TicketScreen.js',
            'pos_disable_refund/static/src/xml/RefundButton.xml',
            'pos_disable_refund/static/src/xml/NumpadWidget.xml',
        ],
    },
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False
}
