# -*- coding: utf-8 -*-

from openerp import models, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def _get_invoice_vals(self, key, inv_type, journal_id, move):
        vals = super(StockPicking, self)._get_invoice_vals(key, inv_type, journal_id, move)

        if inv_type in ['in_invoice', 'in_refund']:
            # update the user id with the current user when we create an invoice from input movement
            vals.update({'user_id': self._uid})

        return vals
