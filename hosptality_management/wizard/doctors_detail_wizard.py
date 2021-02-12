from odoo import models, fields, api

class DoctorsWizard(models.TransientModel):
    _name = 'doctors.wizard'

    patient_name = fields.Char(string="SAY MY NAME")
    x = fields.Char(string="X", compute='_onchange_name')

    @api.onchange('patient_name')
    def _onchange_name(self):
        if self.patient_name:
            if self.paient_name == 'Heisenberg':
                self.x = "YOU'RE GODDAMN RIGHT."
            else:
                self.x = ""