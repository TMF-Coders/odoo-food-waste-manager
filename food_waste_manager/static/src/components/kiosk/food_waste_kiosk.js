/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class FoodWasteKiosk extends Component {
    setup() {
        this.orm = useService("orm");
        this.action = useService("action");
        this.notification = useService("notification");

        this.state = useState({
            step: 'category', // category -> product -> reason -> quantity -> success
            categories: [],
            products: [],
            reasons: [],
            selectedCategoryId: null,
            selectedProductId: null,
            selectedUomName: '',
            selectedReasonId: null,
            quantity: '',
        });

        onWillStart(async () => {
            await this.loadInitialData();
        });
    }

    async loadInitialData() {
        // Load Categories
        this.state.categories = await this.orm.searchRead('food.waste.category', [], ['id', 'name']);
        // Load Reasons
        this.state.reasons = await this.orm.searchRead('food.waste.reason', [], ['id', 'name', 'type']);
    }

    async selectCategory(categoryId) {
        this.state.selectedCategoryId = categoryId;
        // Fetch products for this category (we assume a simple link, or just all products if category link is not on product)
        // Wait, does product.product have a link to food_waste_category? No, we didn't add it to product.product.
        // Let's just load all storable products for now. In a real scenario, you'd filter by a specific pos_category or categ_id.
        // For demonstration, let's load first 50 storable products.
        this.state.products = await this.orm.searchRead(
            'product.product', 
            [['type', '=', 'product']], 
            ['id', 'name', 'uom_id'],
            { limit: 50 }
        );
        this.state.step = 'product';
    }

    selectProduct(productId, uomId) {
        this.state.selectedProductId = productId;
        this.state.selectedUomName = uomId[1];
        this.state.step = 'reason';
    }

    selectReason(reasonId) {
        this.state.selectedReasonId = reasonId;
        this.state.quantity = '';
        this.state.step = 'quantity';
    }

    numpadPress(btn) {
        if (btn === 'C') {
            this.state.quantity = '';
        } else if (btn === '.') {
            if (!this.state.quantity.includes('.')) {
                this.state.quantity += this.state.quantity === '' ? '0.' : '.';
            }
        } else {
            if (this.state.quantity === '0') {
                this.state.quantity = btn;
            } else {
                this.state.quantity += btn;
            }
        }
    }

    goBack() {
        if (this.state.step === 'product') this.state.step = 'category';
        else if (this.state.step === 'reason') this.state.step = 'product';
        else if (this.state.step === 'quantity') this.state.step = 'reason';
    }

    async submitRecord() {
        const qty = parseFloat(this.state.quantity);
        if (isNaN(qty) || qty <= 0) {
            this.notification.add("Please enter a valid quantity.", { type: "warning" });
            return;
        }

        try {
            await this.orm.create('food.waste.record', [{
                category_id: this.state.selectedCategoryId,
                product_id: this.state.selectedProductId,
                reason_id: this.state.selectedReasonId,
                qty: qty
            }]);
            
            this.state.step = 'success';
            
            // Auto close success screen after 3 seconds
            setTimeout(() => {
                if (this.state.step === 'success') {
                    this.resetKiosk();
                }
            }, 3000);
            
        } catch (error) {
            this.notification.add("Error saving record.", { type: "danger" });
            console.error(error);
        }
    }

    resetKiosk() {
        this.state.selectedCategoryId = null;
        this.state.selectedProductId = null;
        this.state.selectedReasonId = null;
        this.state.quantity = '';
        this.state.step = 'category';
    }
}

FoodWasteKiosk.template = "food_waste_manager.Kiosk";

registry.category("actions").add("food_waste_kiosk_action", FoodWasteKiosk);
