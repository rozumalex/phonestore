# -*- coding: utf-8 -*-
{
    'name': "Phone Store",
    'summary': """Phone Store Mangement""",
    'description': """
        A great phone store where you can set Manufacturer and Model
    """,
    'author': "Aleksandr Rozum",
    'website': "http://github.com/rozumalex",
    'category': 'Sales',
    'version': '0.1',
    'depends': ['sale',],
    'data': [
        'security/ir.model.access.csv',
        'views/phonestore.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
