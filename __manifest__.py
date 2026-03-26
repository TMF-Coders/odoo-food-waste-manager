{
    'name': 'Food Waste Management & Kiosk',
    'version': '19.0.1.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'Track, measure, and analyze food waste with a touch Kiosk interface',
    'description': """
Food Waste Management
=====================
A complete solution for hospitality, catering, and collective dining to track food waste,
comply with sustainability laws (EGAlim), and calculate financial impact.

Key Features:
-------------
* **Cost Calculation**: Real-time financial impact of wasted items.
* **Reason Tracking**: Categorize into avoidable vs unavoidable waste.
* **Advanced Analytics**: Pivot tables and graphs to spot inefficiencies.
    """,
    'author': 'TMFCoders SL',
    'license': 'OPL-1',
    'depends': ['stock', 'product', 'hr'],
    'data': [
        'security/food_waste_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/default_reasons_data.xml',
        'views/food_waste_menus.xml',
        'views/food_waste_category_views.xml',
        'views/food_waste_reason_views.xml',
        'views/food_waste_record_views.xml',
    ],
    'installable': True,
    'application': True,
}
