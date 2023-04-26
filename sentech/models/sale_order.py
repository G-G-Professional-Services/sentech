from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    libelle = fields.Char(string="Libellé: ")

    def action_view_invoice(self):
        _logger.debug("=============================== I N S I D E    F U N C T I O N =====================")
        action = super().action_view_invoice()
        context = {
            'default_move_type': 'out_invoice',
        }
        if len(self) == 1:
            context.update({
                'default_libelle': self.libelle,
            })
        action['context'] = context
        return action
