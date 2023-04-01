{
    'name': 'Bank Reconciliation Pos Filter',
    'version': '16.0.1.0.0',
    'summary': 'Bank Reconciliation Pos Filter',
    'category': 'Productivity',
    'depends': ['base', 'account', 'point_of_sale'],
    'author': '',
    'maintainer': '',
    'company': '',
    'website': '',
    'data': [
        'views/bank_rec_widget_view.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'bank_reconciliation_pos_filter/static/src/js/bank_rec_list_view.js'
        ]
    },
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False
}