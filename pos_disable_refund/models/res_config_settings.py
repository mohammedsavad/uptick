# -*- coding: utf-8 -*-
from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_refund_restriction = fields.Boolean(string='Receipt Restriction',
                                            related='pos_config_id.refund_restriction',
                                            readonly=False)
