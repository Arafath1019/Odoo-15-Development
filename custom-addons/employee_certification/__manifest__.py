# -*- coding: utf-8 -*-
{
    'name': 'Employee Certification',
    'summary': "This module use for employee module.",
    'category': 'Human Resource',
    'author': 'BJIT',
    'version': '16.0.0.1',
    'website': 'https://bjitgroup.com',
    'license': 'LGPL-3',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'security/rules.xml',
        'views/employee_certification_views.xml',
    ],
}
