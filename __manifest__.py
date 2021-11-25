# -*- coding: utf-8 -*-
{
    'name': "Wallapop centro educativo",

    'summary': """Wallapop""",
    
    'description': """
        Esto es un sistema para gestionar la venta de portatiles cuando los alumnos
        abandonen el centro educativo.:
    """,


    'author': "Mario Gutierrez",
    'website': "http://www.salesianos.edu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Examen',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
    ],
}