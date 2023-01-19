# -*- coding: utf-8 -*-
# from odoo import http


# class SentechLayout(http.Controller):
#     @http.route('/sentech_layout/sentech_layout/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sentech_layout/sentech_layout/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sentech_layout.listing', {
#             'root': '/sentech_layout/sentech_layout',
#             'objects': http.request.env['sentech_layout.sentech_layout'].search([]),
#         })

#     @http.route('/sentech_layout/sentech_layout/objects/<model("sentech_layout.sentech_layout"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sentech_layout.object', {
#             'object': obj
#         })
