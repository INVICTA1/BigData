import sys
import argparse
from movie_searcher import get_scores, get_movies, write_result_to_csv, print_result
from movie_filter import filter_by_regexp, filter_by_genres, filter_by_from_year, filter_by_to_year, sort_by_rating

PATH_TO_MOVIES = r'resources\movies.csv'
PATH_TO_RATINGS = r'resources\ratings.csv'


def get_parser_arguments():
    """Create params command line"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--limit', type=int, default=None, help='Number of returned items')
    parser.add_argument('-r', '--regex', type=str, default=None, help='Regular expression')
    parser.add_argument('-g', '--genres', type=str, default=None, help='Genres of movie')
    parser.add_argument('-yf', '--year_from', type=int, default=None, help='Movies from a certain year')
    parser.add_argument('-yt', '--year_to', type=int, default=None, help='Movies up to a certain year')
    parser.add_argument('-c', '--csv', type=str, default=None, help='Writing to a csv file')

    return parser


def main():
    """Processing the command line and output result"""

    score_dict = get_scores(PATH_TO_RATINGS)
    movie_dict = get_movies(PATH_TO_MOVIES, score_dict)
    parser = get_parser_arguments()
    namespace = parser.parse_args(sys.argv[1:])

    try:
        if namespace.regex:
            movie_dict = filter_by_regexp(movie_dict, namespace.regex)
        if namespace.genres is not None:
            movie_dict = filter_by_genres(movie_dict, namespace.genres)
        if namespace.year_from is not None:
            movie_dict = filter_by_from_year(movie_dict, namespace.year_from)
        if namespace.year_to is not None:
            movie_dict = filter_by_to_year(movie_dict, namespace.year_to)
        if namespace.limit is not None:
            movie_list = sort_by_rating(movie_dict, namespace.limit)
        else:
            movie_list = sort_by_rating(movie_dict)
        if namespace.csv is not None:
            write_result_to_csv(movie_list, namespace.csv)
        else:
            print_result(movie_list)
    except BaseException as e:
        raise Exception('Data not found', e)


if __name__ == '__main__':
    main()
