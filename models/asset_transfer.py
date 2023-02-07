from odoo import models, fields, api


class AssetTransfer(models.Model):
    _name = "asset.transfer"
    _description = "manage asset transfer"

    transfer_from = fields.Many2one("assets.location", string="Transfer From", required=True)
    transfer_to = fields.Many2one("assets.location", string="Transfer To", required=True)
    transfer_by = fields.Selection([
        ('asset', 'Asset'),
        ('asset group', 'Asset Group')], string="Transfer By")
    transfer_date = fields.Date(string="Transfer Date", required=1)
    transfer_type = fields.Selection([
        ('individual asset transfer', 'Individual Asset Transfer'),
        ('mass asset transfer', 'Mass Asset Transfer')], string="Transfer Type")
    description = fields.Char(string="Description", required=0)
    asset_id = fields.Many2one("asset.master", string="Asset Id")
    uom = fields.Many2one("uom.uom", string="UOM", required=True)
    qty = fields.Char(string="Quantity", required=0)
