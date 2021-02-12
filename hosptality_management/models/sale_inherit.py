from odoo import models, fields, api

class SalesOrderInherit(models.Model):

    _inherit = 'res.partner'

    # second_partner_id = fields.Many2one('res.partner',string='Customer',ondelete='cascade')
    trying=fields.Char('trying')


