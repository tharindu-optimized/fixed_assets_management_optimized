from odoo import models, fields, api


class AssetsLocation(models.Model):
    _name = "assets.location"
    _description = "Assets Location "

    loc_code = fields.Char(string="Location Code")
    name = fields.Char(string="Name", required=1)
    address = fields.Char(string="Address", required=1)
    department = fields.Many2one(
        comodel_name="add.department", string="Department", required=1)
    contact_person = fields.Char(string="Contact Person", required=1)
