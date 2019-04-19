from app import db, ma
from marshmallow import fields
from .base import BaseModel

class Location(db.Model, BaseModel):

    __tablename__ = 'locations'

    name = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)

class LocationSchema(ma.ModelSchema):

    class Meta:
        model = Location

    photos = fields.Nested('PhotoSchema', many=True, exclude=('location',)) # this allows us to actually see the photos


class Photo(db.Model, BaseModel):

    __tablename__ = 'photos'

    image = db.Column(db.String, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id')) # ForeignKey indicates we'll store ref to location id
    location = db.relationship('Location', backref='photos') #The backref means photos will be created on the location model


class PhotoSchema(ma.ModelSchema):

    class Meta:
        model = Photo
