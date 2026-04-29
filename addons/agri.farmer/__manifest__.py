{
    'name': 'Agri Farmers',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',   # ← أول شيء يُحمَّل
        'views/farmer_views.xml',
    ],
}