odoo.define('pos_refund_password.RefundPasswordButton', function (require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require("@web/core/utils/hooks");
    const TicketScreen = require('point_of_sale.TicketScreen');
    const session = require('web.session');

     const PosResTicketScreen1 = (TicketScreen) =>
        class extends TicketScreen {
            async _onDoRefund() {
                if (this.env.pos.config.refund_restriction){
                    session.user_has_group('point_of_sale.group_pos_manager')
                    .then((has_group) => {
                        if(!has_group){
                            var body = this.env._t("You do not have access to issue a refund")
                            this.showPopup('ErrorPopup',{title: this.env._t('Access error'),body:body})
                        }
                        else{
                             super._onDoRefund();
                        }
                    })
                }else{
                     super._onDoRefund();
                }
            }
        };
        Registries.Component.extend(TicketScreen, PosResTicketScreen1);
    });
