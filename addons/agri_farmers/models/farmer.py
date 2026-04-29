from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Farmer(models.Model):
    _name = 'agri.farmer'
    _description = 'Farmer'

    name = fields.Char(required=True)

    national_id = fields.Char(required=True)

    phone = fields.Char()

    birth_date = fields.Date()

    province = fields.Char()

    commune = fields.Char()

    verified = fields.Boolean(default=False)

    state = fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('approved','Approved')
    ], default='draft')


    _sql_constraints = [
        (
            'national_id_unique',
            'unique(national_id)',
            'National ID must be unique'
        )
    ]


    @api.constrains('phone')
    def check_phone(self):
        for rec in self:
            if rec.phone and len(rec.phone) < 10:
                raise ValidationError(
                    'Phone invalid'
                )