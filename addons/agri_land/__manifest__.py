{
    'name': 'Agriculture Land',
    'version': '1.0',
    'depends': ['base', 'web'],
    'data': [
        'views/land_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'agri_land/static/src/js/map.js',
            'agri_land/static/src/xml/map_template.xml',
        ],
    },
}