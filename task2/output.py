import csv
import os


def print_result(movies: list):
    """Output result on console"""

    result = 'genres,name,year,rating'
    print(result)
    for movie in movies:
        genres = movie['genres']
        if type(genres) == list:
            genres = '|'.join(genres)
        name = movie['name']
        year = str(movie['year'])
        rating = str(movie['rating'])
        result = '{0},{1},{2},{3}'.format(genres, name, year, rating)
        print(result)
