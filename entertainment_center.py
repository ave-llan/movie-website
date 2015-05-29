import fresh_tomatoes
import media
import json
from sys import argv
import codecs

# output file name should end in .html
_script, output_file_name = argv


# gathers movie data from a .json file and returns a list of Movie objects
def gather_movies(filename):
    # open the .json file as utf-8
    movie_file = codecs.open(filename, 'r', 'utf-8')
    # read the file and convert to dictionary
    movie_data = json.loads(movie_file.read())
    movies = []
    for movie in movie_data:
        movies.append(media.Movie(movie_data[movie]["title"],
                      movie_data[movie]["storyline"],
                      movie_data[movie]["poster_image"],
                      movie_data[movie]["trailer_youtube_url"]))
    return movies

# generate movies .html page using data in json
fresh_tomatoes.open_movies_page(gather_movies("favorite_movies.json"),
                                output_file_name)
