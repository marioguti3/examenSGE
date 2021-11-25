# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

# pylint: disable=missing-class-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=tow-few-public-methods


class Persona(models.Model):
    
    _name = "personas"
    dni = fields.Char(string="dni", required = True)
    nombre = fields.Char(string="nombre", required = True)
    apellidos = fields.Char(string="apellidos", required = True)
    direccion = fields.Text(string="direccion")
    telefono = fields.Char(string="telefono", required = True)


    class Estudiante(models.Model):
     
     _inherit = "personas"
    portatil = fields.One2many('portatiles',string="portatil")


class Portatil(models.Model):
          
    _name = "portatiles"
    modelo = fields.Char(string="modelo", required = True)
    marca = fields.Char(string="marca", required = True)
    cpu = fields.Char(string="cpu", required = True)
    ram = fields.One2many('portatiles',string="ram")
    discoduro = fields.One2many('portatiles',string="ram")
    fecha_nac = fields.Date(string="Fecha de adquisicion", store=True)
    edad = fields.Float('meses', digits=(12, 1))
comprador = fields.One2many('compradores',string="comprador")
precio = fields.Float(digits=(6, 2),
                            help="Duration in days",
                            compute='precio_venta')
observaciones = fields.Text(string="observaciones");
oferta = fields.Boolean(string="vendido", required = "true")


class Comprador(models.Model):
    _name = "compradores"
    _inherit = "personas"
    _inherit = "portatiles"
_inherit = "ofertas"


class Ram(models.Model):
     frecuencia = fields.Char(string="frecuencia", required = True)
     frecuencia = fields.Char(string="latencia", required = True)
     cantidad = fields.Integer(string="Cantidad ram gigas")
     ram = fields.Selection([('dd3'), ('dd4'), ('dd5')], string='ram')
portatil = fields.Many2one('portatiles', string='Portatil')


class DiscoDuro(models.Model):

     tamaño = fields.Integer(string="Tamaño del disco duro")
     tipo_ram = fields.Selection([('hdd'), ('sdd'), ('nvme')], string='tipo_ram')


class Ofertas(model.Model):

 portatil = fields.One2many('portatiles',string="portatil")
oferta = fields.Boolean(string="aceptada" , required = "true")
comprador = fields.One2many('compradores',string="comprador")
observaciones = fields.Text(string="observaciones");

