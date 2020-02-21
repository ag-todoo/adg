# -*- coding: utf-8 -*-
# from odoo import http


# class Adg(http.Controller):
#     @http.route('/adg/adg/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/adg/adg/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('adg.listing', {
#             'root': '/adg/adg',
#             'objects': http.request.env['adg.adg'].search([]),
#         })

#     @http.route('/adg/adg/objects/<model("adg.adg"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('adg.object', {
#             'object': obj
#         })
