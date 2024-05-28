from app.extensions import db
from app.models.movie import Movie

def seed_data():
    if Movie.query.count() == 0:  # Check if the table is empty
        sample_movies = [
            {
                'name': 'Inception',
                'cover_image': 'inception.jpg',
                'classification': 'PG-13(Parents Strongly Cautioned)',
                'genre': 'Science Fiction',
                'release_date': '2010-07-16',
                'synopsis': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.'
            },
            {
                'name': 'The Matrix',
                'cover_image': 'matrix.jpg',
                'classification': 'R(Restricted)',
                'genre': 'Science Fiction',
                'release_date': '1999-03-31',
                'synopsis': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.'
            },
            {
                'name': 'Interstellar',
                'cover_image': 'interstellar.jpg',
                'classification': 'PG-13(Parents Strongly Cautioned)',
                'genre': 'Science Fiction',
                'release_date': '2014-11-07',
                'synopsis': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.'
            },
            # Add more sample movies here...
            {
                'name': 'The Dark Knight',
                'cover_image': 'dark_knight.jpg',
                'classification': 'PG-13(Parents Strongly Cautioned)',
                'genre': 'Action',
                'release_date': '2008-07-18',
                'synopsis': 'When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.'
            },
            {
                'name': 'Pulp Fiction',
                'cover_image': 'pulp_fiction.jpg',
                'classification': 'R(Restricted)',
                'genre': 'Drama',
                'release_date': '1994-10-14',
                'synopsis': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'
            },
            {
                'name': 'The Godfather',
                'cover_image': 'godfather.jpg',
                'classification': 'R(Restricted)',
                'genre': 'Drama',
                'release_date': '1972-03-24',
                'synopsis': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'
            },
            {
                'name': 'The Shawshank Redemption',
                'cover_image': 'shawshank.jpg',
                'classification': 'R(Restricted)',
                'genre': 'Drama',
                'release_date': '1994-09-23',
                'synopsis': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'
            },
            {
                'name': 'Fight Club',
                'cover_image': 'fight_club.jpg',
                'classification': 'R(Restricted)',
                'genre': 'Action',
                'release_date': '1999-10-15',
                'synopsis': 'An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.'
            },
            {
                'name': 'Forrest Gump',
                'cover_image': 'forrest_gump.jpg',
                'classification': 'PG-13(Parents Strongly Cautioned)',
                'genre': 'Drama',
                'release_date': '1994-07-06',
                'synopsis': 'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75.'
            },
            {
                'name': 'The Lion King',
                'cover_image': 'lion_king.jpg',
                'classification': 'G(General Audience)',
                'genre': 'Animation',
                'release_date': '1994-06-24',
                'synopsis': 'Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.'
            }
        ]

        for movie_data in sample_movies:
            movie = Movie(**movie_data)
            db.session.add(movie)
        db.session.commit()
        print("Sample movies have been added to the database.")
    else:
        print("Database already contains data.")
