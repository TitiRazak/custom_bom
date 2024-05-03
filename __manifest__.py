# -*- coding: utf-8 -*-
{
    'name': "CUSTOM BOM",

    'summary': """
        Add product sale price from bom""",

    'description': """
        Add product sale price from bom
    """,
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mrp', 'sale', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/custom_mrp_bom_line_view.xml',
        'views/product_product_views.xml',
    ],
    'license': 'LGPL-3'
}
