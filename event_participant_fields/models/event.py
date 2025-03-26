from odoo import models, fields

class EventRegistration(models.Model):
    _inherit = 'event.registration'

    coopératives = fields.Char(string='Coopératives')
    allergies = fields.Text(string='Allergies')
