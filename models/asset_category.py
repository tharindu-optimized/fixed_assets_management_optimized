from odoo import models, fields, api


class AssetCategory(models.Model):
    _name = "asset.category"
    _description = "manage asset category"
    # _rec_name = 'unit_of_measurement'

    cat_code = fields.Char(string="Category Code", required=True)
    name = fields.Char(string="Name", required=True)
    uom = fields.Many2one("uom.uom", string="UOM", required=True)
    sale_ac = fields.Many2one("account.journal", string="Sales Account", required=True,
                              domain=[('type', 'in', ('bank', 'cash'))])
    asset_account = fields.Many2one("account.journal", string="Asset Account", required=True,
                              domain=[('type', 'in', ('bank', 'cash'))])
    deprecation_ac = fields.Many2one("account.journal", string="Deprecation Cost Account", required=True,
                              domain=[('type', 'in', ('bank', 'cash'))])
    deprecation_ac_disposal_ac= fields.Many2one("account.journal", string="Deprecation/Disposal Account", required=True,
                              domain=[('type', 'in', ('bank', 'cash'))])
