# -*- coding: utf-8 -*-
from odoo import http


# class Phonestore(http.Controller):
#     @http.route('/phonestore/phonestore/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/phonestore/phonestore/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('phonestore.listing', {
#             'root': '/phonestore/phonestore',
#             'objects': http.request.env['phonestore.phonestore'].search([]),
#         })

#     @http.route('/phonestore/phonestore/objects/<model("phonestore.phonestore"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('phonestore.object', {
#             'object': obj
#         })
