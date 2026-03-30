from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError

class TestFoodWaste(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company_a = cls.env['res.company'].create({'name': 'Company A'})
        cls.company_b = cls.env['res.company'].create({'name': 'Company B'})
        
        cls.product = cls.env['product.product'].create({
            'name': 'Test Chicken',
            'type': 'product',
            'standard_price': 10.0,
        })
        
        cls.reason = cls.env['food.waste.reason'].create({
            'name': 'Burned',
            'type': 'avoidable'
        })
        
        cls.user_a = cls.env['res.users'].create({
            'name': 'User A',
            'login': 'usera',
            'company_id': cls.company_a.id,
            'company_ids': [(4, cls.company_a.id)],
            'groups_id': [(4, cls.env.ref('food_waste_manager.group_food_waste_manager').id)]
        })

    def test_cost_calculation(self):
        """Test if the cost is correctly calculated based on quantity and standard price."""
        record = self.env['food.waste.record'].create({
            'product_id': self.product.id,
            'reason_id': self.reason.id,
            'qty': 2.5,
            'company_id': self.company_a.id
        })
        self.assertEqual(record.cost, 25.0, "Cost should be qty (2.5) * standard_price (10.0)")

    def test_multi_company_isolation(self):
        """Test that Company A cannot read Company B's records."""
        record_b = self.env['food.waste.record'].create({
            'product_id': self.product.id,
            'reason_id': self.reason.id,
            'qty': 1.0,
            'company_id': self.company_b.id
        })
        
        # User A trying to read Record B should raise an AccessError (Record Rule)
        with self.assertRaises(AccessError):
            record_b.with_user(self.user_a).read(['name'])
