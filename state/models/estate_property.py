from odoo import fields, models
class EstateProperty(models.Model):
  _name = "estate_property"
  _description = "Estate Property"
  _postcode = "postcode"
  _date_availability = "'date_availability'"
  _expected_price = "expected_price"
  _selling_price = "selling_price"
  _bedrooms = "bedrooms"
  _living_area = "living_area"
  _facades = 'facades'
  _garage = "garage"
  _garden = "garden"
  _garden_area = "garden_area"
  _garden_orientation = '"garden_orientation"'


  name = fields.Char()
  postcode = fields.Char()
  date_availability = fields.Date()
  expected_price = fields.Float()
  selling_price = fields.Float()
  bedrooms = fields.Integer()
  living_area = fields.Integer()
  facades = fields.Integer()
  garage = fields.Boolean()
  garden = fields.Boolean()
  garden_area = fields.Integer()
  garden_orientation = fields.Selection(
    string='Type',
    selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
  )