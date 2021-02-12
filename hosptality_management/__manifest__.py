# -*- coding: utf-8 -*-
{
    'name': "Hosptality_management",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/patients_view.xml',
        'views/ward_view.xml',
        'views/sale_inherit_view.xml',
        'views/invoice_patient_inherit_view.xml',
        'views/patients_wizard_view.xml',
        'report/report.xml',
        'report/patient_details_report.xml',
        'report/sale_report_inherit.xml',
        'views/Management_staff_view.xml',
        'views/doctors_detail_wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
