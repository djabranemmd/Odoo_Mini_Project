from odoo import models,fields

class Production(models.Model):

 _name='agri.production'

 farmer_id=fields.Many2one(
 'agri.farmer'
 )

 land_id=fields.Many2one(
 'agri.land'
 )

 crop_type=fields.Char()

 expected_qty=fields.Float()

 actual_qty=fields.Float()

 state=fields.Selection([
 ('sowing','Sowing'),
 ('irrigation','Irrigation'),
 ('growth','Growth'),
 ('harvest','Harvest')
 ],default='sowing')
 
def action_irrigation(self):
 self.state='irrigation'

def action_growth(self):
 self.state='growth'

def action_harvest(self):
 self.state='harvest'