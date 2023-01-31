
from odoo import api, fields, models

#Display amount in words in Sale order
class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'
    
    invoice_id = fields.Many2one('account.move')
    
    
            
    def action_create_payments(self):
        payments = self._create_payments()

        if self._context.get('dont_redirect_to_payments'):
            return True

        if self._context.get('active_model') == 'account.move':
                invoice_id = self.env['account.move'].browse(self._context.get('active_ids', [])).id
                
        action = {
            'name': _('Payments'),
            'type': 'ir.actions.act_window',
            'res_model': 'account.payment',
            'context': {'create': False},
        }
        if len(payments) == 1:
            action.update({
                'view_mode': 'form',
                'res_id': payments.id,
            })
        else:
            action.update({
                'view_mode': 'tree,form',
                'domain': [('id', 'in', payments.ids)],
            })
        return action
