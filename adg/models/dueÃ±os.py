# -*- coding: utf-8 -*-

 from odoo import models, fields


 class dueños(models.Model):
     _name = 'dueños.usuarios'
     _description = 'esta clase administra los vehiculos'

     nombre propietario= fields.Char()
     apellido propietario = fields.Char()
     cedula = fields.Integer()
     vehiculo = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
