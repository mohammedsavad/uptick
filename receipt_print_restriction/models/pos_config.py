# -*- coding: utf-8 -*-
from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'

    receipt_restriction = fields.Boolean(string='Receipt Restriction',
                                         default=True)
    restriction_limit = fields.Integer(string='Restriction limit', default=1)
