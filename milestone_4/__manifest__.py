# -*- coding: utf-8 -*-
{
    'name': 'Milestone 4',
    'version': '1.0.1',
    'Author': "Eman Taha",
    'category': 'Other',
    'sequence': 20,
    'summary': 'Property maintenance',
    'depends': [
        'base', 'account','realestate','realestate_contract',],
    'data': [
        'views/property_maintain_inherit_view.xml',
        'security/approval_security.xml',
        'views/email_approval.xml',
    ],
    'demo': [
    ],
    'qweb': [],
    'installable': True,
    'application': True,
}
