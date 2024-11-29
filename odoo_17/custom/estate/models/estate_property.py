from odoo import api, fields, models

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Nombre', readonly=True)
    description = fields.Text(string='Descripción')
    postcode = fields.Char(string='Código Postal')
    date_availability = fields.Date(string='Fecha de Disponibilidad')
    expected_price = fields.Float(string='Precio Esperado')
    selling_price = fields.Float(string='Precio de Venta')
    bedrooms = fields.Integer(string='Número de Habitaciones')
    living_area = fields.Integer(string='Área Habitable (m²)')
    facades = fields.Integer(string='Número de Fachadas')
    garage = fields.Boolean(string='Garaje')
    garden = fields.Boolean(string='Jardín')
    garden_area = fields.Integer(string='Área del Jardín (m²)')
    garden_orientation = fields.Selection(
        selection=[
            ('north', 'Norte'),
            ('south', 'Sur'),
            ('east', 'Este'),
            ('west', 'Oeste')
        ],
        string='Orientación del Jardín'
    )