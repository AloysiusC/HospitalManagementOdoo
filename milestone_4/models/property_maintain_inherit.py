# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import Warning, ValidationError
import time
import datetime
import pytz
from datetime import datetime, timedelta
from odoo.exceptions import UserError


class property_maintenace(models.Model):
    _inherit = "property.maintenance"

    # type_ids = fields.Many2many('maintenance.type','property_type_rel','maintain_rel_id', 'property_type_id' ,string='Type')
    type_maintain = fields.Many2many('maintenance.type','property_types_rel','maintains_rel_id', 'property_types_id',string='Type_many')
    state = fields.Selection([
                ('draft', 'Draft'),
                ('approval','Approval'),
                ('progress', 'In Progress'),
                ('incomplete', 'Incomplete'),
                ('done', 'Done')], 'State', default='draft')
    need_approval=fields.Char('Approval Need',compute='_compute_default_response_id')
    respon_person=fields.Many2one('res.users',string='Responsible person')
    # user = fields.Many2one(comodel_name='res.users', string="User", domain="[]")

    @api.multi
    def pass_data(self):
        """
        This button method is used to pass m2o data into m2m field.
        @param self: The object pointer
        """
        for rec in self.search(
                [('type', '!=', False)]):  # Search all the records that have value in m2o field
            rec.write({'type_maintain': [(6, 0, [rec.type.id])]})  # Move data from m2o to m2m
            print('rec......', rec)


    @api.multi
    def start_maint(self):
        """
        This Method is used to change maintenance state to progress.
        @param self: The object pointer
        """

        self.write({'state': 'approval', 'approved_user_id': self.env.uid})


        # group = self.env.ref()

        # # # email code
        # self._cr.execute("""SELECT uid FROM res_groups_users_rel
        #                             WHERE gid IN (
        #                                 SELECT res_id FROM ir_model_data WHERE module=%s AND name=%s)""",
        #                  ('milestone_4', 'group_property_user',))
        # property_approval_access_u_ids= self._cr.fetchone()
        #
        # Users = self.env['res.users'].browse(property_approval_access_u_ids[0])
        # print(Users.email)
        #
        # values = {
        #     'need_approval':str(users[0]),
        # }
        # self.update(values)

        template_id = self.env.ref('milestone_4.send_prop_email')
        print(template_id)
        self.env['mail.template'].browse(template_id.id).send_mail(self.id)
        # print(template)

        return True

    @api.one
    @api.depends('respon_person')
    def _compute_default_response_id(self):
        if self.respon_person:
            self.need_approval = self.respon_person.email
            print(self.respon_person.email)



    @api.onchange('property_id')
    def _compute_group_users(self):
        users = self.env.ref('milestone_4.group_property_user').users.ids

        return {'domain': {'respon_person': [('id', 'in', users)]}}

    @api.multi
    def approve_state(self):
        """
        This Method is used to change maintenance state to progress.
        @param self: The object pointer
        """
        return self.write({'state': 'progress', 'approved_user_id': self.env.uid})





