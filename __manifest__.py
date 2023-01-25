{
    'name': 'Fixed Assets Management',
    'version': '15.0.0.1',
    'sequence': 200,
    'category': 'Uncategorized ',
    'website': 'https://optimized.lk/',
    'author': 'OPTIMIZED TECHNOLOGIES',
    'summary': 'Manage all  fixed assets of the company',
    'depends': [
        'base','account'
    ],
    'data': [
        'views/unit_of_measurement_views.xml',
        'views/asset_category_views.xml',
        'views/department_views.xml',
        'views/assets_location_views.xml',
        'views/assets_classes_views.xml',
        'views/asset_master_views.xml',
        'views/asset_transfer_views.xml',
        'views/asset_disposal_views.xml',
        'views/disposal_reason_views.xml',
        'views/asset_disposal_confirmation_views.xml',
        'views/menu.xml',
        'security/security.xml',
        'security/ir.model.access.csv'


    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
