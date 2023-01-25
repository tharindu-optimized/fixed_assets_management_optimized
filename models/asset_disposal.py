from odoo import models, fields, api


class AssetDisposal(models.Model):
    _name = "asset.disposal"
    _description = "asset disposal "

    date = fields.Date(string="Date")
    customer = fields.Char(string="Customer", required=1)
    disposal_reason = fields.Many2one("disposal.reason", string="Disposal Reason")
    asset_id = fields.Many2one("asset.master", string="Asset ID")
    uom = fields.Char(string="UOM")
    qty = fields.Char(string="Quantity")
    selling_value = fields.Char(string="Selling Value")
    tax = fields.Char(string="Tax")

