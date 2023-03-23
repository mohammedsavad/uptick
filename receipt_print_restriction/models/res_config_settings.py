# -*- coding: utf-8 -*-
from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_receipt_restriction = fields.Boolean(string='Receipt Restriction',
                                             related='pos_config_id.receipt_restriction',
                                             readonly=False)
    pos_restriction_limit = fields.Integer(string='Restriction limit', readonly=False,
                                           related='pos_config_id.restriction_limit')
