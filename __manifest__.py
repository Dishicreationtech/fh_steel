# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Web Api",
    'category': 'Website/Website',
    "summary": "Public category",
    "version": "16.0.1",
    "author": "Dishi Creation",
    "license": "AGPL-3",
    "website": "https://www.dishicreation.com",
    "depends": ["base","web", "crm"],
    "data": [
        'security/ir.model.access.csv',
        'security/activity_security.xml',
        "views/view.xml",
        'views/task.xml',
        ],
    'external_dependencies': {
        'python': ['geopy'],
    },
    "images": ["static/description/main.png"],
    'assets': {
        'web.assets_qweb': [
            'website_api/src/**/*',
        ],
    },
    "development_status": "Alpha",
    'installable': True,
    'application': True,
    'auto_install': False,
}
