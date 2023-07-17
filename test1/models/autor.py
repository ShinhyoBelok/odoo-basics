from odoo import models, fields


# estamos creando uan tabla en la base de datos
class Autor(models.Model):
    _name = 'autores'  # nombre de la tabla
    # rec_name cambia el field que regresa un many2one de este modelo, que por default es name en este caso ahora va a reqresar last_name
    _rec_name = 'last_name'

    name = fields.Char(string="Nombre del autor", required=True)
    last_name = fields.Char(string="Apellido")
