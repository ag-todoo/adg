# -*- coding: utf-8 -*-

 from odoo import models, fields, api


 class vehiculos(models.Model):
     _name = 'vehiculos.usuarios'
     _description = 'esta clase administra los vehiculos'

     nombre = fields.Char()
     apellido = fields.Char()
     cedula = fields.Integer()
     vehiculo = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
