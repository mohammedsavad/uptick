from odoo import models, fields


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    pos_config_id = fields.Many2one('pos.config', related='pos_session_id.config_id')

