from odoo import models, fields


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    pos_session_id = fields.Many2one('pos.session', related='payment_id.pos_session_id')
    pos_config_id = fields.Many2one('pos.config', store=True,
                                    related='pos_session_id.config_id',
                                    string='Point of Sale')
