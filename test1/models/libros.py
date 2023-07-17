from odoo import models, fields

# estamos creando uan tabla en la base de datos
class Libros(models.Model):
    _name = 'libros' #nombre de la tabla
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nombre del libro", required=True, tracking=True) #nombre del campo
    editorial = fields.Char(string="Editorial", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    autor_id = fields.Many2one(comodel_name="autores", string="Autor", required=True)
    image = fields.Binary(string="image")
    categoria = fields.Many2one(comodel_name="libros.categoria", string="Categoria", required=True)
    state = fields.Selection([('draft','Borrador'),('published','Publicado')], default='draft')

    def btn_publicar(self):
        self.state = 'published'

    def btn_borrador(self):
        self.state = 'draft'

    _sql_constraints = [("name_uiq", "unique (name)", "El nombre del libro ya existe")]
    #nombre del sql constraint
    #unique (los valores que queremos que sean unique)
    #mensaje de error
    # NOTA: CUANDO QUERAMOS ELIMINAR ESTE CONSTRAINT SE QUITA EL CODIGO Y SE ELIMINA EL CONSTRAINT CREADO POR SQL DIRECTAMENTE EN LA BASE DE DATOS POR PGADMIN4

class Categoria(models.Model):
    _name = 'libros.categoria'

    name = fields.Char(string="Categoria")