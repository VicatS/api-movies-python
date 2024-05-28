import os
import uuid
from flask import request, jsonify, current_app
from werkzeug.utils import secure_filename
from app.models.movie import Movie
from app.serializers.movie_serializer import movie_schema, movies_schema

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

def save_image(file):
    if file and allowed_file(file.filename):
        # Generar un nombre de archivo único
        extension = file.filename.rsplit('.', 1)[1].lower()
        unique_filename = f"{uuid.uuid4().hex}.{extension}"
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], secure_filename(unique_filename))
        file.save(file_path)
        return unique_filename
    else:
        raise ValueError("Invalid file format")

def create_movie():
    """
    Create a new movie
    ---
    tags:
      - Movies
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: Inception
            cover_image:
              type: string
              example: inception.jpg
            classification:
              type: string
              example: PG-13
            genre:
              type: string
              example: Action
            release_date:
              type: string
              example: 2010-07-16
            synopsis:
              type: string
              example: A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.
    responses:
      201:
        description: Movie created successfully
        schema:
          $ref: '#/definitions/Movie'
    """
    try:
        data = request.form.to_dict()
        if 'cover_image' not in request.files:
            raise ValueError("cover_image is required")

        file = request.files['cover_image']
        data['cover_image'] = save_image(file)

        new_movie = Movie.create(data)
        return movie_schema.jsonify(new_movie), 201
    except ValueError as e:
        return jsonify({"errors": e.args[0] if isinstance(e.args[0], dict) else {"error": str(e)}}), 400

def get_movies():
    """
    Get all movies
    ---
    tags:
      - Movies
    responses:
      200:
        description: A list of movies
        schema:
          type: array
          items:
            $ref: '#/definitions/Movie'
    """
    movies = Movie.get_all()
    return movies_schema.jsonify(movies), 200

def get_movie(id):
    """
    Get a movie by ID
    ---
    tags:
      - Movies
    parameters:
      - name: id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: A movie
        schema:
          $ref: '#/definitions/Movie'
    """
    movie = Movie.get_by_id(id)
    return movie_schema.jsonify(movie), 200

def update_movie(id):
    """
    Update a movie by ID
    ---
    tags:
      - Movies
    parameters:
      - name: id
        in: path
        required: true
        type: integer
        example: 1
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: Inception
            cover_image:
              type: string
              example: inception_updated.jpg
            classification:
              type: string
              example: PG-13
            genre:
              type: string
              example: Action
            release_date:
              type: string
              example: 2010-07-16
            synopsis:
              type: string
              example: Updated synopsis.
    responses:
      200:
        description: Movie updated successfully
        schema:
          $ref: '#/definitions/Movie'
    """
    try:
        data = request.form.to_dict()
        movie = Movie.get_by_id(id)
        print(data)
        
        if 'cover_image' in request.files:
            file = request.files['cover_image']
            data['cover_image'] = save_image(file)

        movie.update(data)
        return movie_schema.jsonify(movie), 200
    except ValueError as e:
        return jsonify({"errors": e.args[0] if isinstance(e.args[0], dict) else {"error": str(e)}}), 400


def delete_movie(id):
    """
    Delete a movie by ID
    ---
    tags:
      - Movies
    parameters:
      - name: id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      204:
        description: Movie deleted successfully
    """
    Movie.delete(id)
    return '', 204
