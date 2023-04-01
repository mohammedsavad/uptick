# -*- coding: utf-8 -*-
from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'

    refund_restriction = fields.Boolean(string='Receipt Restriction')
