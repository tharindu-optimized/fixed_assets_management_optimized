from odoo import models, fields, api


class DisposalReason(models.Model):
    _name = "disposal.reason"
    _description = "disposal reason "
    _rec_name = 'disposal_reason'

    disposal_reason = fields.Char(string="Disposal Reason")
