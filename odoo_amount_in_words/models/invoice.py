# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2021 Cloudroits (info.cloudroits@gmail.com)
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import api, fields, models, _

#Display amount in words in Sale order
class AccountMove(models.Model):

    _inherit = 'account.move'

    def _compute_amount2words(self):
        for rec in self:
                rec.amount_words = str(rec.currency_id.amount_to_text(rec.amount_total))

    amount_words = fields.Char(string="En votre aimable réglement la somme de: ", help=
        "Total amount in words is automatically generated by the system", compute='_compute_amount2words')

    personal_partner_bank_id = fields.Many2one(
        comodel_name='res.partner.bank',
        string="Recipient Bank Account",
        readonly=False,
        store=True,
    )
    
    
  
    