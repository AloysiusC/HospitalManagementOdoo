from odoo import models, fields, api

class Wards(models.Model):
    _name = 'wards.details'

    name = fields.Char('Ward name')
    ward_no = fields.Integer(required=True)
    doct_name = fields.Many2one(comodel_name='doctors.details',string='Doctors name')




    def custom_method(self):
        # ward_record_details=self.env['wards.details'].create({'name':'dental','ward_no':44})
        # print(ward_record_details)
        self_search = self.env['wards.details'].search([('name','=','dental')])
        self_search.unlink()
        print(self_search)
       # print(self_search)
       # for wards in self_search:
       #  print(wards.doct_name.id)
       #  print(wards.doct_name.age)
       #  print(wards.doct_name.name)
       #  print(wards.doct_name.gender)
       # sale_browse=self.env['wards.details'].browse(30)
       # if sale_browse.exists():
       #     print('record present')
       # else:
       #     print('record not present')
