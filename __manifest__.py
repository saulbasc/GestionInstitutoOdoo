# -*- coding: utf-8 -*-
{
    'name': 'Instituto',

    'summary': 'Gestión de un instituto',

    'description': """
        Gestión de profesores, alumnado, cursos, grupos,
        horarios, asignaturas y calificaciones.
    """,

    'author': 'My Company',
    'website': 'https://www.yourcompany.com',

    'category': 'Uncategorized',
    'version': '16.0.1.0.0',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/horario.xml',
        'views/asignatura.xml',
        'views/profesor.xml',
        'views/curso.xml',
        'views/estudiante.xml',
        'views/calificacion.xml',
        'views/grupo.xml',
        'views/menu.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'GestionInstitutoOdoo/static/src/css/styles.css',
        ],
    },

    'application': True,
    'installable': True,
}