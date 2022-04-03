# Data model for the project
import datetime as dt
from marshmallow import Schema, fields
import uuid


class Project():
    def __init__(self, description, requirements, max_budget, bids_deadline, owner):
        self.lowest_bid_amount = None        
        self.assigned_offer = None
        self.id = uuid.uuid4()
        self.description = description
        self.requirements = requirements
        self.max_budget = max_budget
        self.created_at = dt.datetime.now()
        self.owner = owner
        self.bids_deadline = dt.datetime.strptime(
            str(bids_deadline), '%Y-%m-%d %H:%M:%S')
        self.name_best_bid = None

    def assign_better_offer(self, offer):
        if((dt.datetime.now() < self.bids_deadline) and (offer.price < self.max_budget)):
            if (self.assigned_offer == None):
                self.assigned_offer = offer
                self.lowest_bid_amount = offer.price
                self.name_best_bid = offer.seller
            else:
                if (self.assigned_offer.min_price == None):
                    if ((offer.min_price == None) and (offer.price < self.lowest_bid_amount)):
                        self.assigned_offer = offer
                        self.lowest_bid_amount = offer.price
                        self.name_best_bid = offer.seller
                    elif ((offer.min_price != None) and offer.min_price < self.lowest_bid_amount):
                        self.assigned_offer = offer
                        self.lowest_bid_amount = self.lowest_bid_amount-1
                        offer.price = self.lowest_bid_amount
                        self.name_best_bid = offer.seller
                else:
                    if ((offer.min_price == None) and (offer.price < self.assigned_offer.min_price)):
                        self.assigned_offer = offer
                        self.lowest_bid_amount = offer.price
                        self.name_best_bid = offer.seller

                    elif((offer.min_price == None) and (offer.price > self.assigned_offer.min_price) and (offer.price < self.lowest_bid_amount)):
                        self.lowest_bid_amount = offer.price - 1
                        offer.price = self.lowest_bid_amount
                        self.name_best_bid = offer.seller

                    elif ((offer.min_price != None) and offer.min_price < self.assigned_offer.min_price):
                        self.lowest_bid_amount = self.assigned_offer.min_price-1
                        self.assigned_offer = offer
                        offer.price = self.lowest_bid_amount
                        self.name_best_bid = offer.seller


class ProjectSchema(Schema):
    description = fields.Str()
    requirements = fields.Str()
    bids_deadline = fields.Str()
    owner = fields.Str()
    id = fields.UUID()
    amount = fields.Number()
    lowest_bid_amount = fields.Number()
    max_budget = fields.Number()
    name_best_bid = fields.Str()