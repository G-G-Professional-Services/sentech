# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, _
import logging
_logger = logging.getLogger(__name__)

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'
    
    def _create_invoice(self, order, so_line, amount):
        _logger.debug("=============================== I N S I D E    F U N C T I O N =====================")
        invoice = super()._create_invoice(self, order, so_line, amount)
        invoice['libelle'] = order.libelle
        return invoice

