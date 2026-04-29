from odoo import models,fields


class Land(models.Model):

    _name='agri.land'

    name=fields.Char(required=True)

    farmer_id=fields.Many2one(
        'agri.farmer',
        string='Farmer'
    )

    latitude=fields.Float()

    longitude=fields.Float()

    area=fields.Float()

    soil_type=fields.Selection([
      ('clay','Clay'),
      ('sand','Sand'),
      ('silt','Silt')
    ])