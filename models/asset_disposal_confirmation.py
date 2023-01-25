from odoo import models, fields, api


class DisposalConfirmation(models.Model):
    _name = "disposal.confirmation"
    _description = "disposal confirmation"
    # _rec_name = 'unit_of_measurement'

    date = fields.Date(string="Date")
    customer = fields.Char(string="Customer")
    disposal_reason = fields.Many2one("disposal.reason", string="Disposal Reason")
    asset_id = fields.Many2one("asset.master", string="Asset ID")
    uom = fields.Char(string="UOM")
    qty = fields.Char(string="Quantity")
    selling_value = fields.Char(string="Selling Value")
    tax = fields.Char(string="Tax")
    state = fields.Selection([('reject', 'Reject'), ('approve', 'Approve')], string='Status')

    # down tab

    note = fields.Text(string="Note")

    # Buttons

    def action_approve(self):
        self.state = "approve"

    def action_reject(self):
        self.state = "reject"
