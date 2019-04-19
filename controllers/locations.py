from flask import Blueprint, jsonify, request   # blueprint mini router. request to access req params or body JSON
# from marshmallow import ValidationError
from models.location import Location, LocationSchema
from app import db

router = Blueprint(__name__, 'locations')

location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)

@router.route('/locations', methods=['GET'])
def index():
    locations = Location.query.all()

    return locations_schema.jsonify(locations, many=True), 200


@router.route('/locations/<int:location_id>', methods=['GET'])
def show(location_id):
    location = Location.query.get(location_id)

    if not location:
        return jsonify({ 'message': 'Not found'}), 404

    return location_schema.jsonify(location), 200
