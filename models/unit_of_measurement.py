from odoo import models, fields, api


class UnitOfMeasurement(models.Model):
    _name = "unit.measurement"
    _description = "manage unit of measurement"
    _rec_name = 'unit_of_measurement'

    unit_of_measurement = fields.Char(string="Unit Of Measurement", required=True)

