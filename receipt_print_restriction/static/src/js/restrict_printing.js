odoo.define('receipt_print_restriction.PrintRestriction', function (require) {
    'use strict';

    const { nextFrame } = require('point_of_sale.utils');
    const AbstractReceiptScreen = require('point_of_sale.AbstractReceiptScreen');
    const Registries = require('point_of_sale.Registries');
    const { useRef } = owl;

    const  PrintRestriction = AbstractReceiptScreen =>
        class extends AbstractReceiptScreen {
            setup() {
                console.log(this)
                this.receipt_print_count = 0;
            super.setup();
            }
            async _printReceipt() {
                if (this.env.pos.config.receipt_restriction){
                    if (this.receipt_print_count < this.env.pos.config.restriction_limit){
                        this.receipt_print_count += 1;
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