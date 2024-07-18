{
    'name': 'Evomed',
    'version': '17.0',
    'author': "Valentyn Kovalenko",
    'website': "https://resume-valentin-kovalenko.netlify.app/",
    'category': 'Human Resources',
    'summary': 'Upgrade HR Modules',
    'depends': ['hr', 'hr_recruitment', 'hr_skills', 'hr_contract', 'hr_holidays'],
    'demo': [
        'demo/hr_job_demo.xml',
        'demo/hr_department_demo.xml',
        'demo/hr_employee_demo.xml',

        # TODO: BRGM: there is no such file
    #    'demo/resource_calendar_demo.xml',

        'demo/hr_contract_type_demo.xml',

        # TODO: BRGM: commented due to errors in file
    #    'demo/hr_contract_demo.xml',

        'demo/hr_employee_position_demo.xml',
    ],
    'data': [
        'views/hr_employee_views.xml',
        'views/hr_job_view.xml',

        # TODO: BRGM: lack of acl - need to grant all 4
        'security/ir.model.access.csv'
    ],
    'assets': {
        'web.assets_backend': [
            'evomed_test_task/static/src/fields/**/*',
        ]
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3'
}
