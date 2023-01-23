from odoo import models, fields, api


class AssetClasses(models.Model):
    _name = "assets.classes"
    _description = "Assets Classes"

    class_code = fields.Char(string="Class Code")
    name = fields.Char(string="Name", required=1)
    description = fields.Char(string="Description", required=1)
    basic_depr_rate = fields.Integer(string="Basic Depreciation Rate", required=1)
