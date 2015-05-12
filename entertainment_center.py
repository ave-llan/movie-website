import fresh_tomatoes
import media
import json

# gathers movie data from a .json file and returns a list of Movie objects
def gather_movies(filename):
    # open the .json file and convert it to a dictionary
    movie_data = json.loads(open(filename).read())
    movies = []
    for movie in movie_data:
        m = movie_data[movie]
        # create a media.Movie instance for each movie
        movies.append(media.Movie(m["title"], m["storyline"], m["poster_image"], m["trailer_youtube_url"]))
    return movies

#print gather_movies("favorite_movies.json")
fresh_tomatoes.open_movies_page(gather_movies("favorite_movies.json"))
