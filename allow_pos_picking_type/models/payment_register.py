from odoo import models, fields, api


class PaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    user_access = fields.Boolean(string='User Access',
                                 compute='_compute_user_access')

    @api.depends('partner_id')
    def _compute_user_access(self):
        for rec in self:
            rec.user_access = False
            if self.env.user.has_group('purchase.group_purchase_manager'):
                rec.user_access = True

    @api.depends('available_journal_ids')
    def _compute_journal_id(self):
        if not self.env.user.has_group('purchase.group_purchase_manager'):
            self.journal_id = self.env.user.allowed_journal.id
        else:
            for wizard in self:
                if wizard.can_edit_wizard:
                    batch = wizard._get_batches()[0]
                    wizard.journal_id = wizard._get_batch_journal(batch)
                else:
                    wizard.journal_id = self.env['account.journal'].search([
                        ('type', 'in', ('bank', 'cash')),
                        ('company_id', '=', wizard.company_id.id),
                        ('id', 'in', self.available_journal_ids.ids)
                    ], limit=1)
