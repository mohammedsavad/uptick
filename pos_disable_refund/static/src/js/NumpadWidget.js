/** @odoo-module **/
const RefundButton = require('point_of_sale.NumpadWidget');
const session = require('web.session');
const { useRef, onPatched, onMounted, useState } = owl;
import { patch } from "@web/core/utils/patch";

patch(RefundButton.prototype, 'disable_refund_button',{
    setup(){
         this.state = useState({
            has_access: true
         })
        if (this.env.pos.config.refund_restriction){
            session.user_has_group('point_of_sale.group_pos_manager')
            .then((has_group) => {
                    this.state.has_access = has_group
                }
            )
         }
    },
})
