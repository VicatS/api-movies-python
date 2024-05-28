from flask import Blueprint, send_from_directory, current_app
from app.controllers.movie_controller import create_movie, get_movies, get_movie, update_movie, delete_movie

movie_bp = Blueprint('movies', __name__)

movie_bp.route('/movies', methods=['POST'])(create_movie)
movie_bp.route('/movies', methods=['GET'])(get_movies)
movie_bp.route('/movies/<int:id>', methods=['GET'])(get_movie)
movie_bp.route('/movies/<int:id>', methods=['PUT'])(update_movie)
movie_bp.route('/movies/<int:id>', methods=['DELETE'])(delete_movie)

@movie_bp.route('/uploads/<filename>', methods=['GET'])
def get_image(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)