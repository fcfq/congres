from odoo import models, fields

class EventRegistration(models.Model):
    _inherit = 'event.registration'

    coop = fields.Char(string='coop')
    allergies = fields.Text(string='Allergies')
