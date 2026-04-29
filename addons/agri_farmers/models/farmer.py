from odoo import models,fields,api
from odoo.exceptions import ValidationError

class Farmer(models.Model):
    _name='agri.farmer'
    _description='Farmer'

    name=fields.Char(required=True)
    national_id=fields.Char(required=True)
    phone=fields.Char()
    birth_date=fields.Date()

    province=fields.Char()
    commune=fields.Char()

    verified=fields.Boolean(default=False)