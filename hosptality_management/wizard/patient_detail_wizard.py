from odoo import models, fields, api

class Patients(models.TransientModel):
    _name = 'patients.wizard'


    name = fields.Char('Name')



