from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    user_access = fields.Boolean(string='User Access',
                                 compute='_compute_user_access')

    @api.depends('partner_id')
    def _compute_user_access(self):
        for rec in self:
            rec.user_access = False
            if self.env.user.has_group('purchase.group_purchase_manager'):
                rec.user_access = True
