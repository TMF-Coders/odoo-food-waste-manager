from odoo import models, fields

class FoodWasteReason(models.Model):
    _name = 'food.waste.reason'
    _description = 'Food Waste Reason'
    _order = 'name'

    name = fields.Char(string='Reason', required=True, translate=True)
    type = fields.Selection([
        ('avoidable', 'Avoidable'),
        ('unavoidable', 'Unavoidable')
    ], string='Type', required=True, default='avoidable', help='Avoidable waste can be reduced, unavoidable is inherent to the process.')
    active = fields.Boolean(default=True)
