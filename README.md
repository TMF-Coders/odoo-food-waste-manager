# Food Waste Management & Kiosk

A complete solution for hospitality, catering, and collective dining to track food waste, comply with sustainability laws, and calculate financial impact in Odoo 19.

## Features

- **Waste Tracking:** Log every wasted item with category, reason, and quantity.
- **Cost Analysis:** Automatically calculates the financial cost based on standard price.
- **Reporting:** Out of the box pivot tables and graphs to analyze waste over time.
- **Multi-Company:** Fully isolated for multi-company operations.

## Installation

1. Clone this repository into your Odoo addons path.
2. Update the apps list.
3. Install the `food_waste_manager` module.

## Configuration

Navigate to **Food Waste > Configuration > Reasons** to set up your waste reasons.
Navigate to **Food Waste > Configuration > Categories** to group products.

## Pre-commit

This repository uses OCA pre-commit hooks.
```bash
pre-commit install
```
