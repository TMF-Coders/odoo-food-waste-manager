{
    'name': 'Food Waste Management & Kiosk',
    'version': '19.0.1.0.0',
    'category': 'Inventory/Inventory',
    'images': ['static/description/main_screenshot.png'],
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
    'depends': ['stock', 'product', 'hr', 'vituallas_core'],
    'data': [
        'security/food_waste_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/default_reasons_data.xml',
        'views/food_waste_menus.xml',
        'views/res_config_settings_views.xml',
        'views/food_waste_kiosk_action.xml',
        'views/food_waste_category_views.xml',
        'views/food_waste_reason_views.xml',
        'views/food_waste_record_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'food_waste_manager/static/src/components/kiosk/food_waste_kiosk.scss',
            'food_waste_manager/static/src/components/kiosk/food_waste_kiosk.xml',
            'food_waste_manager/static/src/components/kiosk/food_waste_kiosk.js',
        ],
    },
    'installable': True,
    'application': True,
}
