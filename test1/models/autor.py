from odoo import models, fields

# estamos creando uan tabla en la base de datos
class Autor(models.Model):
    _name = 'autores' #nombre de la tabla

    name = fields.Char(string="Nombre del autor", required=True)
    last_name = fields.Char(string="Apellido")