from odoo import models, fields, api

class InvoicePatient(models.Model):

    _inherit = 'purchase.order'

    doct_invoice_detail= fields.Char('try_it')
    hobby =fields.Char('Hobby')


