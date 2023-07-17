from odoo import models, fields


# estamos creando uan tabla en la base de datos
class hrEmployeddTest1(models.Model):
    _inherit = "hr.employee"

    es_supervisor = fields.Boolean(string="Supervisor")
