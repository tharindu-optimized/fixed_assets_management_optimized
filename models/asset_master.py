from odoo import models, fields, api


class AssetMaster(models.Model):
    _name = "asset.master"
    _description = "asset master"
    _rec_name = 'asset_id'

    asset_class = fields.Many2one("assets.classes", string="Asset Class")
    asset_category = fields.Many2one("asset.category", string="Asset Category")
    asset_id = fields.Char(string="Asset ID", required=1)
    description = fields.Char(string="Description", required=0)
    short_name = fields.Char(string="Short Name", required=1)
    acquition_date = fields.Date(string="Acquisition  Date", required=1)
    location = fields.Many2one("assets.location", string="Location", required=True)
    acquition_cost = fields.Float(string="Acquisition Cost")
    asset_label = fields.Char(string="Asset Label", required=1)
    warranty_period = fields.Char(string="Warranty Period")
    last_maintenance = fields.Char(string="Last Maintenance")
