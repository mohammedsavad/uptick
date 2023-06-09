# -*- coding: utf-8 -*-
from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    allowed_pos_ids = fields.Many2many('pos.config', string='Allowed POS')
    allowed_picking_ids = fields.Many2many('stock.picking.type',
                                           string='Allowed Picking')
    allowed_journal = fields.Many2one('account.journal', string="Allowed journal",
                                      domain="[('type', 'in', ('bank', 'cash'))]")
    # allowed_journal = fields.Many2many('account.journal', string="Allowed journal")
