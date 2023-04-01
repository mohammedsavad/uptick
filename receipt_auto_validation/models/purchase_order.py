# -*- coding: utf-8 -*-
from odoo import models
import json


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        if self.env['ir.config_parameter'].sudo().get_param(
                'readonly.receipt_auto_validate'
        ):
            user_ids = str(self.env['ir.config_parameter'].sudo().get_param(
                'allowed_user_ids'
            ))
            user_ids = json.loads(user_ids)
            if self.env.uid in user_ids:
                flag = True
                for rec in self.order_line:
                    if rec.product_id.tracking != 'none':
                        flag = False

                if flag and self.picking_ids:
                    for rec in self.picking_ids:
                        rec.action_set_quantities_to_reservation()
                        rec.button_validate()
        return res
