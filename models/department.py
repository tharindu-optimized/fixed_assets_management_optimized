from odoo import models, fields, api


class Department(models.Model):
    _name = "add.department"
    _description = "Department"

    name = fields.Char(string="Department Name")
