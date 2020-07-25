from odoo import api, models, fields , _

class AccountInvoice(models.Model):
    
    _inherit = 'account.invoice'
    _description = 'Account Invoice'

        
    intercompany_transfer_id = fields.Many2one('inter.company.transfer.ept', string="ICT", copy=False)
    transfer_fee_id = fields.Float("Costo de Transf. (%)", related="intercompany_transfer_id.transfer_fee")
    amount_transfer_fee = fields.Float("Monto Costo de Transf.", compute='_compute_amount')
    
    @api.model
    def create(self, vals):
        res = super(AccountInvoice, self).create(vals)
        order_id = self.env['sale.order'].search([('name', '=', res.origin)])
        if not order_id:
            order_id = self.env['purchase.order'].search([('name', '=', res.origin)])
        if order_id and order_id.intercompany_transfer_id:
            res.intercompany_transfer_id = order_id.intercompany_transfer_id.id
        return res

    @api.one
    @api.depends('invoice_line_ids.price_subtotal', 'tax_line_ids.amount', 'currency_id', 'company_id', 'date_invoice',
                 'global_discount_type', 'global_order_discount', 'amount_tax', 'amount_untaxed',
                 'total_extra_discount', 'transfer_fee_id')
    def _compute_amount(self):
        super(AccountInvoice, self)._compute_amount()
        self.amount_transfer_fee = self.amount_total*(self.transfer_fee_id/100)
        self.amount_total += self.amount_transfer_fee

