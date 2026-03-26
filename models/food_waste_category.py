from odoo import models, fields

class FoodWasteCategory(models.Model):
    _name = 'food.waste.category'
    _description = 'Food Waste Category'
    _order = 'name'

    name = fields.Char(string='Name', required=True, translate=True)
    parent_id = fields.Many2one('food.waste.category', string='Parent Category', index=True)
    color = fields.Integer(string='Color Index')
    active = fields.Boolean(default=True)
