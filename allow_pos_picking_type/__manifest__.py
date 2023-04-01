# -*- coding: utf-8 -*-
{
    'name': 'Allow POS, Picking Type',
    'version': '16.0.1.0.0',
    'category': 'Productivity',
    'author': '',
    'maintainer': '',
    'company': '',
    'website': '',
    'depends': [
        'base', 'point_of_sale', 'stock', 'account'
    ],
    'data': [
        'data/picking_type_rule.xml',
        'data/pos_config_rule.xml',
        # 'data/purchase_journal_rule.xml',
        # 'data/pos_payment_method.xml',
        'views/res_users.xml',
        'views/payment_register.xml'
    ],
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False
}