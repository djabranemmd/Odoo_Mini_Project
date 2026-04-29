from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Land(models.Model):
    _name = 'agri.land'
    _description = 'Agricultural Land'

    name = fields.Char("Land Name", required=True)
    latitude = fields.Float("Latitude", digits=(10, 7))
    longitude = fields.Float("Longitude", digits=(10, 7))

    @api.constrains('latitude', 'longitude')
    def _check_coordinates(self):
        for rec in self:
            if rec.latitude and (rec.latitude < -90 or rec.latitude > 90):
                raise ValidationError("Invalid latitude")
            if rec.longitude and (rec.longitude < -180 or rec.longitude > 180):
                raise ValidationError("Invalid longitude")