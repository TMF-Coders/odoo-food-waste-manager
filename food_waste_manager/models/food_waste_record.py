from odoo import models, fields, api

class FoodWasteRecord(models.Model):
    _name = 'food.waste.record'
    _description = 'Food Waste Record'
    _order = 'date desc, id desc'

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, default=lambda self: 'New')
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
    date = fields.Datetime(string='Date', required=True, default=fields.Datetime.now)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    category_id = fields.Many2one('food.waste.category', string='Category')
    reason_id = fields.Many2one('food.waste.reason', string='Reason', required=True)
    
    qty = fields.Float(string='Quantity', required=True, digits='Product Unit of Measure')
    uom_id = fields.Many2one('uom.uom', string='Unit of Measure', related='product_id.uom_id', readonly=True)
    
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', readonly=True)
    cost = fields.Monetary(string='Estimated Cost', compute='_compute_cost', store=True, currency_field='currency_id')
    
    user_id = fields.Many2one('res.users', string='Reported By', default=lambda self: self.env.user)
    notes = fields.Text(string='Notes')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('food.waste.record') or 'New'
        return super().create(vals_list)

    @api.depends('qty', 'product_id', 'product_id.standard_price')
    def _compute_cost(self):
        for record in self:
            if record.product_id and record.qty:
                record.cost = record.qty * record.product_id.standard_price
            else:
                record.cost = 0.0
