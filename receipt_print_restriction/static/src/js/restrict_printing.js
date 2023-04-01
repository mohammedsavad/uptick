odoo.define('receipt_print_restriction.PrintRestriction', function (require) {
    'use strict';

    const { nextFrame } = require('point_of_sale.utils');
    const AbstractReceiptScreen = require('point_of_sale.AbstractReceiptScreen');
    const Registries = require('point_of_sale.Registries');
    const { useRef } = owl;

    const  PrintRestriction = AbstractReceiptScreen =>
        class extends AbstractReceiptScreen {
            setup() {
                if (this.props.order){
                    this.order_id = this.props.order
                }else{
                    this.order_id = this.env.pos.selectedOrder
                }
                if (!this.order_id.receipt_print_count){
                    var order_data = localStorage.getItem(this.order_id.uid)
                    if(!order_data){
                       this.order_id.receipt_print_count = 0;
                       localStorage.setItem(this.order_id.uid, 0)
                    }else{
                        this.order_id.receipt_print_count = parseInt(order_data)
                    }
                }
            super.setup();
            }
            async _printReceipt() {
                if (this.env.pos.config.receipt_restriction){
                    if (this.order_id.receipt_print_count < this.env.pos.config.restriction_limit){
                        this.order_id.receipt_print_count += 1;
                        localStorage.setItem(this.order_id.uid, this.order_id.receipt_print_count)
                        super._printReceipt()
                    }else{
                        const { confirmed, payload } = await this.showPopup('ErrorPopup', {
                           title: this.env._t('Error Popup'),
                           body: this.env._t('Print limit Reached : '+this.env.pos.config.restriction_limit),
                        });
                    }
                }else{
                    super._printReceipt()
                }
            }
    };
    Registries.Component.extend(AbstractReceiptScreen, PrintRestriction );
    return PrintRestriction;

});