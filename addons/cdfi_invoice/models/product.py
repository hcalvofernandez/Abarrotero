# -*- coding: utf-8 -*-
from odoo import fields, models, api,_


    
UM_CLAVO_MAP = {
                'Pieza': 'H87',
                'Hora': 'HUR',
                'Kilogramo': 'KGM',
                'Gramo': 'GRM',
                'Litro': 'LTR',
                'Galon': 'A76',
                'Tonelada': 'TNE',
                'Caja': 'XBX',
                'Metro': 'MTR',
                'Metro lineal': 'LM',
                'M2': 'MTK',
                'M3': 'MTQ',
                'Pie': 'FOT',
                'Unidad de servicio': 'E48',
                'Tarifa': 'A9',
                'Dia': 'DAY',
                'Lote': 'XLT',	
                'Conjunto': 'SET',
                'Actividad': 'ACT',
                'Comida': 'Q3',
                'Habitacion': 'ROM',
                'Paquete': 'XPK',
                'Pallet': 'XPX',	
                'Mutuamente definido': 'ZZ',
                'Medida metrica de rollo': 'RK',
                'Uno': 'C62',	
                'Vehiculo': 'XVN',
                'Par': 'PR',
                'Cubeta': 'XBJ',
                'Rollo': 'XRO',
                'Docena': 'DZN',
                'Kit': 'KT',
                'Tableros de pie': 'BFT',
                'Trabajo': 'E51',
                'No disponible': 'XNA',
                'Kilowatt hora': 'KWH',
                'Caja de carton' : 'X4G',
                'Tira' : 'SR',
                'Saco': 'XSA',
                'Docenas de piezas': 'DPC',
                'Paca no comprimida' : 'XBN',
                'Tarro' : 'XJR',
                'Bolsa de plastico' : 'X44',
                'Cajetilla' : 'XPA',
                'Paquete de diez' : 'TP',
               }
    
class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    UNIDAD_MEDIDA_LIST=[
                    ('Pieza', 'Pieza'),
                   ('Hora', 'Hora'),
                   ('Kilogramo', 'Kilogramo'),
                   ('Gramo', 'Gramo'),
                   ('Litro', 'Litro'),
                   ('Galon', 'Galon'),
                   ('Tonelada', 'Tonelada'),
                   ('Caja', 'Caja'),
                   ('Metro', 'Metro'),
                   ('Metro lineal', 'Metro lineal'),
                   ('M2', 'M2'),
                   ('M3', 'M3'),
                   ('Pie', 'Pie'),
                   ('Unidad de servicio', 'Unidad de servicio'),
                   ('Tarifa', 'Tarifa'),
                   ('Dia', 'Dia'),
                   ('Lote', 'Lote'),
                   ('Conjunto', 'Conjunto'),
                   ('Actividad', 'Actividad'),
                   ('Comida', 'Comida'),				   
                   ('Habitacion', 'Habitacion'),
                   ('Pallet', 'Pallet'),
                   ('Paquete', 'Paquete'),	
                   ('Mutuamente definido', 'Mutuamente definido'),
                   ('Medida metrica de rollo', 'Medida metrica de rollo'),
                   ('Uno', 'Uno'),
                   ('Vehiculo', 'Vehiculo'),
                   ('Par', 'Par'),
                   ('Cubeta', 'Cubeta'),
                   ('Rollo', 'Rollo'),
                   ('Docena', 'Docena'),
                   ('Kit', 'Kit'),
                   ('Tableros de pie', 'Tableros de pie'),
                   ('Trabajo', 'Trabajo'),
                   ('No disponible', 'No disponible'),
                   ('Kilowatt hora', 'Kilowatt hora'),
                   ('Caja de carton', 'Caja de carton'),
                   ('Tira', 'Tira'),
                   ('Saco', 'Saco'),
                   ('Docenas de piezas', 'Docenas de piezas'),
                   ('Paca no comprimida', 'Paca no comprimida'),
                   ('Tarro', 'Tarro'),
                   ('Bolsa de plastico', 'Bolsa de plastico'),
                   ('Cajetilla', 'Cajetilla'),
                   ('Paquete de diez', 'Paquete de diez'),
                   ]

    unidad_medida = fields.Selection(selection=UNIDAD_MEDIDA_LIST, string='Unidad SAT')
    clave_unidad = fields.Char(string='Clave unidad', compute='_compute_clave_unidad')
    description_cve_prod = fields.Many2one('catalogos.claveprodserv', string='Descripción CveProd')
    clave_producto = fields.Char(string='Clave producto', related='description_cve_prod.c_claveprodserv')

    @api.depends('unidad_medida')
    @api.one
    def _compute_clave_unidad(self):
        if self.unidad_medida:
            self.clave_unidad = UM_CLAVO_MAP[self.unidad_medida]
