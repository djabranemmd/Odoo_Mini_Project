# agri_farmers/__manifest__.py
{
    'name': 'Agri Farmers',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'views/farmer_views.xml',   # ← Must be listed here
    ],
}