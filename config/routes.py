from app import app
from controllers import locations

app.register_blueprint(locations.router, url_prefix='/api')
