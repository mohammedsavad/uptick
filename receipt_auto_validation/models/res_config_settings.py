# -*- coding: utf-8 -*-
from odoo import models, fields, api
from ast import literal_eval


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    receipt_auto_validate = fields.Boolean(string='Receipt Auto Validate',
                                           config_parameter='readonly.receipt_auto_validate')
    allowed_user_ids = fields.Many2many('res.users', string='Allowed Users')

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'allowed_user_ids', self.allowed_user_ids.ids)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo().get_param(
            'allowed_user_ids')
        res.update(
            allowed_user_ids=[(6, 0, literal_eval(params))] if params else False, )
        return res
