from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    user_access = fields.Boolean(string='User Access',
                                 compute='_compute_user_access')

    @api.depends('picking_type_id')
    def _compute_user_access(self):
        for rec in self:
            rec.user_access = False
            if self.env.user.has_group('stock.group_stock_manager'):
                rec.user_access = True
