# Data model for the offer

import uuid
from marshmallow import Schema, fields, post_load


class Offer():
    def __init__(self, project_id, price, seller, min_price=None):
        self.id = uuid.uuid4()
        self.project_id = project_id
        self.price = price
        self.seller = seller
        self.min_price = min_price


class OfferSchema(Schema):
    id = fields.UUID()
    project_id = fields.UUID()
    price = fields.Number()
    min_price = fields.Number()
    buyer = fields.Str()
    seller = fields.Str()

    @post_load
    def make_offer(self, data, **kwargs):
        return Offer(**data)