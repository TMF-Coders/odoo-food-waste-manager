from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    waste_threshold_cost = fields.Monetary(string='Waste Cost Threshold', default=50.0)
