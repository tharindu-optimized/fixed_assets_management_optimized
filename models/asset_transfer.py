from odoo import models, fields, api


class AssetTransfer(models.Model):
    _name = "asset.transfer"
    _description = "manage asset transfer"

    transfer_from = fields.Many2one("assets.location", string="Transfer From", required=True)
    transfer_to = fields.Many2one("assets.location", string="Transfer To", required=True)
    transfer_by = fields.Selection([
        ('asset', 'Asset'),
        ('asset group', 'Asset Group')], string="Transfer By")
