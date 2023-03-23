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
        'base', 'point_of_sale', 'stock'
    ],
    'data': [
        'data/picking_type_rule.xml',
        'data/pos_config_rule.xml',
        'views/res_users.xml'
    ],
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False
}