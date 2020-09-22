# -*- coding: utf-8 -*-

from odoo import models, fields


class ClaveProdServ(models.Model):
    _name = 'catalogos.claveprodserv'
    _rec_name = "descripcion"

    c_claveprodserv = fields.Char(string='Clave de Producto o servicio')
    descripcion = fields.Char(string='Descripción')
