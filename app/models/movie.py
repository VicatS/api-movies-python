from datetime import datetime
from app.extensions import db
import os
from flask import current_app, url_for

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    cover_image = db.Column(db.String(255), nullable=False)
    classification = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    synopsis = db.Column(db.Text(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, cover_image, classification, genre, release_date, synopsis):
        self.name = name
        self.cover_image = cover_image
        self.classification = classification
        self.genre = genre
        self.release_date = release_date
        self.synopsis = synopsis

    @staticmethod
    def create(data):
        errors = {}
        required_fields = ['name', 'cover_image', 'classification', 'genre', 'release_date', 'synopsis']
        
        for field in required_fields:
            if field not in data or not data[field]:
                errors[field] = f"{field} is required and cannot be empty."
        
        if errors:
            raise ValueError(errors)
            
        new_movie = Movie(
            name=data['name'],
            cover_image=data['cover_image'],
            classification=data['classification'],
            genre=data['genre'],
            release_date=data['release_date'],
            synopsis=data['synopsis']
        )
        db.session.add(new_movie)
        db.session.commit()
        return new_movie

    @staticmethod
    def get_all():
        return Movie.query.all()

    @staticmethod
    def get_by_id(movie_id):
        return Movie.query.get_or_404(movie_id)

    def update(self, data):
        errors = {}
        required_fields = ['name', 'cover_image', 'classification', 'genre', 'release_date', 'synopsis']
        
        for field in required_fields:
            if field in data and not data[field]:
                errors[field] = f"{field} cannot be empty."
                
        if 'name' in data:
            self.name = data['name']
        if 'cover_image' in data:
            # Eliminar la imagen anterior
            if self.cover_image and os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], self.cover_image)):
                os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], self.cover_image))
            self.cover_image = data['cover_image']
        if 'classification' in data:
            self.classification = data['classification']
        if 'genre' in data:
            self.genre = data['genre']
        if 'release_date' in data:
            self.release_date = data['release_date']
        if 'synopsis' in data:
            self.synopsis = data['synopsis']
            
        self.updated_at = datetime.now()
        db.session.commit()
        return self

    @staticmethod
    def delete(movie_id):
        movie = Movie.query.get_or_404(movie_id)
        # Eliminar la imagen al eliminar la película
        if movie.cover_image and os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], movie.cover_image)):
            os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], movie.cover_image))
        db.session.delete(movie)
        db.session.commit()
        
    def get_image_url(self):
        return url_for('static', filename=f'uploads/{self.cover_image}', _external=True)