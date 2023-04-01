/** @odoo-module **/
const PaymentScreen = require('point_of_sale.PaymentScreen');
const session = require('web.session');
const { useRef, onPatched, onMounted, useState } = owl;
import { patch } from "@web/core/utils/patch";

patch(PaymentScreen.prototype, 'credit_restriction',{
    setup(){
         this._super(...arguments);
         this.state = useState({
            method_id: false
         })
          console.log(this.env.pos.config)
         if (this.env.pos.config.credit_restriction){
            var partner_id = this.env.pos.selectedOrder.partner.id
            if(!this.env.pos.config.allowed_customers.includes(partner_id)){
                this.state.method_id = this.env.pos.config.payment_method_id[0]
            }
         }
    },
})
