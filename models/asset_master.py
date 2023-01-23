from odoo import models, fields, api


class AssetMaster(models.Model):
    _name = "asset.master"
    _description = "asset master"

    asset_class = fields.Many2one("assets.classes", string="Asset Class", required=True)
    asset_id = fields.Char(string="Asset ID", required=1)
    description = fields.Char(string="Description", required=0)
    short_name = fields.Char(string="Short Name", required=1)
    acquition_date = fields.Date(string="Acquition Date", required=1)
    location = fields.Many2one("assets.location", string="Location", required=True)
    acquition_cost = fields.Float(string="Acquition Cost", required=1)
    asset_label = fields.Char(string="Asset Label", required=1)
    warranty_period = fields.Char(string="Warranty Period", required=1)
    last_maintenance = fields.Char(string="Last Maintenance", required=1)



