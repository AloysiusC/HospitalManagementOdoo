# -*- coding: utf-8 -*-
# from odoo import http


# class HosptalityManagement(http.Controller):
#     @http.route('/hosptality_management/hosptality_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hosptality_management/hosptality_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hosptality_management.listing', {
#             'root': '/hosptality_management/hosptality_management',
#             'objects': http.request.env['hosptality_management.hosptality_management'].search([]),
#         })

#     @http.route('/hosptality_management/hosptality_management/objects/<model("hosptality_management.hosptality_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hosptality_management.object', {
#             'object': obj
#         })
