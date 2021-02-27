import csv
import os
import sys
from searcher import get_scores, get_movies
from argument import get_parser_arguments
from filter import filter_by_regexp, filter_by_genres, filter_by_from_year, filter_by_to_year, sort_by_rating


PATH_TO_MOVIES = r'resources\movies.csv'
PATH_TO_RATINGS = r'resources\ratings.csv'


def write_movies_to_csv(movie_list, name):
    """Write result to csv file"""

    csv_file = os.path.splitext(name)[0] + '.csv'
    with open(csv_file, "w", newline="") as file:
        columns = ['name', 'year', 'genres', 'rating']
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        for movie in movie_list:
            movie['genres'] = '|'.join(movie['genres'])
        writer.writerows(movie_list)


def output_movies(movie_list):
    """Output result on console"""

    result = 'name;year;genres;rating\n'
    delimiter = '; '
    for movie in movie_list:
        name = movie['name']
        year = str(movie['year'])
        genres = '|'.join(movie['genres'])
        rating = str(movie['rating'])
        result += name + delimiter + year + delimiter + genres + delimiter + rating + '\n'
    print(result)


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
            write_movies_to_csv(movie_list, namespace.csv)
        else:
            output_movies(movie_list)
    except BaseException as e:
        raise Exception('Data not found', e)


if __name__ == '__main__':
    main()
