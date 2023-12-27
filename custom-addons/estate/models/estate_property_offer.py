from odoo import models, fields

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'
    _order = "price desc"
    _sql_constraints = [
        ("check_price", "CHECK(price > 0)", "The price must be strictly positive"),
    ]

    price = fields.Float("Price", required=True)
    validity = fields.Integer(string="Validity (days)", default=7)