from odoo import api, fields, models

class IcaTeacher(models.Model):
    _name = 'ica.teacher'
    _description = 'IcaTeacher'

    name = fields.Char()
    parent_id = fields.Many2one("ica.teacher")
    child_ids = fields.One2many("ica.teacher", 'parent_id')

