# -*- coding: utf-8 -*-
{
    'name': "sentech",

    'summary': """
        Module pour afficher les entêtes et les pieds de page de la structure SENTECH""",

    'description': """
        Long description of module's purpose
    """,

    'author': "GandG",
    'website': "https://www.gandgcorp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale_management'],

    # always loaded
    'data': [
        
        'views/custom_external_layout.xml',
        'views/sale_order.xml',
        'report/invoice_report.xml',
    ],
    # only loaded in demonstration mode
    
}
