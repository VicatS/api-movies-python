from flask_marshmallow import Marshmallow
from app.models.movie import Movie

ma = Marshmallow()

class MovieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Movie

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
