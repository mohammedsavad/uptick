from odoo import models, fields


class PosOrder(models.Model):
    _inherit = 'pos.order'

    account_analytic_id = fields.Many2one(
        comodel_name='account.analytic.account', copy=False, string='Analytic Account')

    def _prepare_invoice_line(self, order_line):
        res = super(PosOrder, self)._prepare_invoice_line(order_line)
        if order_line.order_id.account_analytic_id:
            res['analytic_distribution'] = {order_line.order_id.account_analytic_id.id: 100}
        return res

    def write(self, vals):
        for order in self:
            if not order.account_analytic_id and order.config_id.account_analytic_id:
                vals['account_analytic_id'] = \
                    order.config_id.account_analytic_id.id or False
        return super(PosOrder, self).write(vals)
