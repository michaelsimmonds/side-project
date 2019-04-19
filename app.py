from flask import Flask                         # creates server
from flask_sqlalchemy import SQLAlchemy         # sqlalchemy allows flask to acces our database
from flask_marshmallow import Marshmallow      # marshmallow converts data to JSON to send onto client

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/side-project-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # this speeds up SQLAlchemy

db = SQLAlchemy(app)
ma = Marshmallow(app)

from models.location import Location, LocationSchema
location_schema = LocationSchema(many=True)       # many=true will handle an array of locations

from config import routes

# @app.route('/locations')
# def index():
#     locations = Location.query.all()
#
#     return location_schema.jsonify(locations), 200
