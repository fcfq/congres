from odoo import models, fields

class EventRegistration(models.Model):
    _inherit = 'event.registration'

    cooperative = fields.Char(string='Cooperative')
    allergies = fields.Text(string='Allergies')
