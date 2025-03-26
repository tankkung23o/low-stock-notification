{
    'สินค้าใกล้หมด': 'สินค้าใกล้หมด',
    'version': '1.0',
    'summary': 'สินค้าใกล้หมด',
    'description': """
        This module sends internal notifications to all salespersons
        when the stock level of a product falls below 10 units.
    """,
    'author': 'Admins',
    'website': 'Need sotre',
    'category': 'Inventory',
    'depends': ['sale_management', 'stock'],
    'data': [
        'data/scheduled_action.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}  