
from odoo import models, fields, api
import random



class Doctors(models.Model):
    _name = 'doctors.details'
    _description = 'hosptality_management.hosptality_management'

    name = fields.Char(string='Doctors name',compute='_compute_name')
    designation = fields.Char('Designation')
    age = fields.Integer()
    gender =fields.Selection([
        ('F', 'Female'),
        ('M', "Male")],string='Gender')
    pat_assg = fields.One2many(comodel_name='doctorsspersonal.details', inverse_name='pt_id', string='Patients Asssig')
    pat_select = fields.Many2many('patients.details', 'doctor_patients_rel', 'pat_ids', 'docts_id', string='Patients')

    # name_filter = fields.Char(string="SAY MY NAME")
    # age_filter = fields.Integer(string="AGE")
    # gender_filter = fields.Selection([('M', 'Male'), ('F', 'Female')], string="GENDER")
    nationality = fields.Many2one('res.country', string="Nationality")

    def _compute_name(self):
        for record in self:
            record.name=str(random.randint(1,1e6))

class Doctors_Detail(models.Model):
    _name = 'doctorsspersonal.details'

    patient_name = fields.Many2one('patients.details','Patient Assigned')
    status =fields.Selection([
        ('D', 'Done'),
        ('UD', "Still working")],string='Treatment status')
    pt_id= fields.Many2one('patients.details','patient id')

