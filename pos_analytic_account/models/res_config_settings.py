from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_account_analytic_id = fields.Many2one(
        related='pos_config_id.account_analytic_id', readonly=False)
