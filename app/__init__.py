from flask import Flask, jsonify
from .config import Config
from .extensions import db, migrate
from .routes.movie_route import movie_bp
from flasgger import Swagger # type: ignore
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(movie_bp, url_prefix='/api/v1')
    
    swagger = Swagger(app)
    
    app.config['SWAGGER'] = {
        'title': 'Movie API',
        'uiversion': 3
    }
    
    @app.errorhandler(404)
    def not_found_error(error):
        response = jsonify({
            "message": "The resource does not exist."
        })
        response.status_code = 404
        return response
    
    # Manejador de errores para ValueError
    @app.errorhandler(ValueError)
    def handle_value_error(error):
        response = jsonify({
            "errors": error.args[0] if isinstance(error.args[0], dict) else {"error": str(error)}
        })
        response.status_code = 400
        return response

    return app

# Add Movie definition for Swagger
def add_movie_definition(app):
    @app.before_first_request
    def register_movie_definition():
        app.config['SWAGGER']['definitions'] = {
            'Movie': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'cover_image': {'type': 'string'},
                    'classification': {'type': 'string'},
                    'release_date': {'type': 'string'},
                    'synopsis': {'type': 'string'},
                    'created_at': {'type': 'string', 'format': 'date-time'},
                    'updated_at': {'type': 'string', 'format': 'date-time', 'nullable': True}
                }
            }
        }
