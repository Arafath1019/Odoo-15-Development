{
    'name': "Estate",
    'version': '1.0',
    'summary': 'Estate Module',
    'sequence': 1,
    'depends': ['base'],
    'author': "Yeasin Arafath",
    'category': '',
    'description': """
    Estate Description Text
    """,
    'images': [],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_type.xml',
        'views/estate_property_tag.xml',
        'views/estate_property_offer.xml',
        'views/estate_property.xml',
        'report/estate_report_views.xml',
        'report/estate_reports.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '',
    'license': 'LGPL-3'
}