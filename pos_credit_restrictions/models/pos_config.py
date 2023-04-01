# -*- coding: utf-8 -*-
from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'

    credit_restriction = fields.Boolean(string='Receipt Restriction')
    allowed_customers = fields.Many2many('res.partner',
                                         string='Restriction limit')
    payment_method_id = fields.Many2one('pos.payment.method',
                                        string='Payment Method')
