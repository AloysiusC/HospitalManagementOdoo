from odoo import models, fields, api

class Patients(models.Model):
    _name = 'patients.details'

    name = fields.Char('Patients name')
    f_name= fields.Char('First name')
    l_name= fields.Char('Last name')
    disease= fields.Char('disease')
    age = fields.Integer()
    gender =fields.Selection([
        ('F', 'Female'),
        ('M', "Male")],string='Gender')
    doc_head=fields.Many2one(comodel_name='res.partner', string='Doctor Head')
    doc_assg = fields.One2many(comodel_name='patientspersonal.details',inverse_name='dt_id',string='Doctors Asssig')
    doct_select= fields.Many2many('doctors.details','patient_doctor_rel','doct_ids','patient_id', string='doctors')
    job_position=fields.Char(string='Job Position' ,related='doc_head.function')

    # name_filter = fields.Char(string="SAY MY NAME")
    # age_filter = fields.Integer(string="AGE")
    # gender_filter = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="GENDER")
    # nationality = fields.Many2one('res.nation', string="Nationality")

    @api.onchange('f_name','l_name')
    def generate_fullname(self):
        for record in self:
            if record.f_name:
                if record.l_name:
                    record.name=str(record.f_name)+' '+str(record.l_name)


class Patients_Detail(models.Model):
    _name = 'patientspersonal.details'

    ward_name = fields.Many2one('wards.details','Ward Assigned')
    fees =fields.Selection([
        ('P', 'Paid'),
        ('UP', "Unpaid")],string='Fees')
    dt_id= fields.Many2one('patients.details','Doctor id')


class Management_staff(models.Model):
    _name = 'managestaff.details'

    staff_name=fields.Char('Staff name')
    job_post=fields.Char('Job position')
    age = fields.Integer()
    gender = fields.Selection([
        ('F', 'Female'),
        ('M', "Male")], string='Gender')

class SuperSalesGod(models.Model):
    _inherit = 'sale.order'

    Flex = fields.Char(string="Flex", readonly=True)

    def action_confirm(self):
        go_super = super(SuperSalesGod, self).action_confirm()
        go_super_2 = self.partner_id.email
        self.update({'Flex': go_super_2})
        return go_super


