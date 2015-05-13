import fresh_tomatoes
import media
import json


# gathers movie data from a .json file and returns a list of Movie objects
def gather_movies(filename):
    # open the .json file and convert it to a dictionary
    movie_data = json.loads(open(filename).read())
    movies = []
    for movie in movie_data:
        movies.append(media.Movie(movie_data[movie]["title"],
                      movie_data[movie]["storyline"],
                      movie_data[movie]["poster_image"],
                      movie_data[movie]["trailer_youtube_url"]))
    return movies

# generate movies .html page using data in json
fresh_tomatoes.open_movies_page(gather_movies("favorite_movies.json"))
