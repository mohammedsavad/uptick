# -*- coding: utf-8 -*-
from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_credit_restriction = fields.Boolean(string='Credit Restriction',
                                            related='pos_config_id.credit_restriction',
                                            readonly=False)
    pos_allowed_customers = fields.Many2many(string='Allowed Customers',
                                             readonly=False,
                                             related='pos_config_id.allowed_customers')
    pos_payment_method_id = fields.Many2one(string='Payment Method',
                                             readonly=False,
                                             related='pos_config_id.payment_method_id')
