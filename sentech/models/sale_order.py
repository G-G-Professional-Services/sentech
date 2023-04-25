from odoo import fields, models


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    libelle = fields.Char(string="Libellé: ")
