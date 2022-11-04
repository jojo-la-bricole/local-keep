# -*- coding: utf-8 -*-
# from odoo import http


# class Coucou(http.Controller):
#     @http.route('/coucou/coucou', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coucou/coucou/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('coucou.listing', {
#             'root': '/coucou/coucou',
#             'objects': http.request.env['coucou.coucou'].search([]),
#         })

#     @http.route('/coucou/coucou/objects/<model("coucou.coucou"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coucou.object', {
#             'object': obj
#         })
