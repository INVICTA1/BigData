import sys
import argparse

from movie_parser import read_movies, map_scores_to_movies, print_result, read_rating
from movie_filter import filter_by_regexp, filter_by_genres, filter_by_from_year, filter_by_to_year, \
    sort_by_rating, sort_by_number_genres

PATH_TO_MOVIES = r'resources\movies.csv'
PATH_TO_RATINGS = r'resources\ratings.csv'


def get_parser_arguments():
    """Create params command line"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', type=int, default=None, help='Number of returned items')
    parser.add_argument('-r', '--regex', type=str, default=None, help='Regular expression')
    parser.add_argument('-g', '--genres', type=str, default=None, help='Genres of movie')
    parser.add_argument('-yf', '--year_from', type=int, default=None, help='Movies from a certain year')
    parser.add_argument('-yt', '--year_to', type=int, default=None, help='Movies up to a certain year')
    parser.add_argument('-c', '--csv', type=str, default=None, help='Writing to a csv file')

    return parser


def main():
    """Processing the command line and output result"""

    try:
        parser = get_parser_arguments()
        namespace = parser.parse_args(sys.argv[1:])
        scores = read_rating(PATH_TO_RATINGS)
        movies = read_movies(PATH_TO_MOVIES)
        movies = map_scores_to_movies(movies, scores)
        if namespace.regex:
            movies = filter_by_regexp(movies, namespace.regex)
        if namespace.genres is not None:
            movies = filter_by_genres(movies, namespace.genres)
        if namespace.year_from is not None:
            movies = filter_by_from_year(movies, namespace.year_from)
        if namespace.year_to is not None:
            movies = filter_by_to_year(movies, namespace.year_to)
        if namespace.number is not None and namespace.genres is not None:
            movies = sort_by_number_genres(movies, namespace.genres, namespace.number)
        elif namespace.number is not None and len(movies) > namespace.number:
            movies = sort_by_rating(movies)[:namespace.number]
        else:
            movies = sort_by_rating(movies)
        print_result(movies)
    except BaseException as e:
        raise Exception("Can't process file", e)


if __name__ == '__main__':
    main()
