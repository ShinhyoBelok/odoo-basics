# -*- coding: utf-8 -*-
{
    'name': "odoo 14 test1",
    'summary': "aprediendo odoo 14 con Ivan",
    'author': "Shinhyo",
    'category': 'General',
    'version': '1.0.0',
    'depends': ['mail', 'hr'],#cuando cambias el depends hay que actualizar manualmente el modulo
    'data': [
        'views/menu_view.xml',
        'views/libros_view.xml',
        'views/hr_employee_form_view.xml',
        'security/libreria_security.xml',
        'security/ir.model.access.csv'
    ],
}