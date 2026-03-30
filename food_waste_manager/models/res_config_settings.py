from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_food_waste_alerts = fields.Boolean(
        string='Enable Waste Alerts',
        help='Send automatic emails to managers when waste exceeds a certain threshold.'
    )
    
    waste_threshold_cost = fields.Monetary(
        string='Cost Threshold for Alerts',
        related='company_id.waste_threshold_cost',
        readonly=False,
        help='Notify managers if a single waste record exceeds this cost.'
    )
