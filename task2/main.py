import builtins
import sys
import re
from argument import Arguments

path_to_movies = r'resources\movies.csv'
path_to_ratings = r'resources\ratings.csv'


def get_scores(path):
    """Read csv file and return dict{movieId:[rating]}"""

    dict_scores = {}
    with open(path) as csv_file:
        for line in csv_file:
            row = csv_file.readline()
            cells = row.split(',')
            movie_id = int(cells[1])
            score = cells[2]
            if dict_scores.get(movie_id):
                dict_scores[movie_id].append(float(score))
            else:
                dict_scores[movie_id] = [float(score)]

    return dict_scores


def get_genres(cells):
    """Get genres from cells"""

    genres = cells[-1].replace('\n', '')

    return genres.split('|')


def find_name_and_year(cells):
    """Find name and year from cells and return this data"""

    if cells.__len__() == 3:
        name_with_year = cells[1]
    else:
        name_with_year = ','.join(cells[1:-1])
    list_words_from_name = name_with_year.split(' ')
    year_from_name = list_words_from_name[-1]
    year = year_from_name[year_from_name.find('(') + 1: year_from_name.find(')')]

    return year, list_words_from_name


def get_name(cells):
    """Return name"""

    year, list_words_from_name = find_name_and_year(cells)
    if year.isdigit():
        name_movie = ' '.join(list_words_from_name[:-1])
    else:
        name_movie = ' '.join(list_words_from_name)

    return name_movie


def get_year(cells):
    """Return year"""

    year, list_words_from_name = find_name_and_year(cells)
    if not year.isdigit():
        year = None

    return year


def get_rating(dict_ratings, movie_id):
    """Find average rating and return rating data """

    if dict_ratings.get(movie_id):
        list_score = dict_ratings[movie_id]
        rating = round(sum(list_score) / len(list_score), 1)
    else:
        rating = None

    return rating


def get_movies(path, dict_scores):
    """Read CSV file adn create movie dictionary """

    dict_movies = {}
    with open(path) as csv_file:
        for line in csv_file:
            row = csv_file.readline()
            if row:
                cells = row.split(',')
                movie_id = int(cells[0])
                list_genres = get_genres(cells)
                name_movie = get_name(cells)
                year = get_year(cells)
                rating = get_rating(dict_scores, movie_id)
                dict_movies[movie_id] = {'name': name_movie,
                                         'year': year,
                                         'genres': list_genres,
                                         'rating': rating}

    return dict_movies


def filter_by_regexp(dict_movies, regexp):
    try:
        new_dict_movies = {}
        for movie_id in dict_movies:
            if dict_movies[movie_id]['name'].__contains__(regexp):
                new_dict_movies[movie_id] = dict_movies[movie_id]
        return new_dict_movies
    except BaseException as e:
        raise Exception('Data not found', e)


def filter_by_genres(dict_movies, genres):
    try:
        new_dict_movies = {}
        for movie_id in dict_movies:
            if set(dict_movies[movie_id]['genres']) & set(genres):
                new_dict_movies[movie_id] = dict_movies[movie_id]
        return new_dict_movies
    except BaseException as e:
        raise Exception('Data not found', e)


def filter_by_from_year(dict_movies, year_from):
    try:
        new_dict_movies = {}
        for movie_id in dict_movies:
            if dict_movies[movie_id]['year'] is not None and dict_movies[movie_id]['year'] >= year_from:
                new_dict_movies[movie_id] = dict_movies[movie_id]
        return new_dict_movies
    except BaseException as e:
        raise Exception('Data not found year_from', e)


def filter_by_to_year(dict_movies, year_to):
    try:
        new_dict_movies = {}
        for movie_id in dict_movies:
            if dict_movies[movie_id]['year'] is not None and dict_movies[movie_id]['year'] <= year_to:
                new_dict_movies[movie_id] = dict_movies[movie_id]
        return new_dict_movies
    except BaseException as e:
        raise Exception('Data not found', e)


def sort_by_rating(dict_movies, count=None):
    try:
        sort_dict = {}
        for movie_id in dict_movies:
            sort_dict[dict_movies[movie_id]['rating']] = movie_id
        sort_dict.keys()

    except BaseException as e:
        raise Exception('Data not found', e)


def main():
    dict_scores = get_scores(path_to_ratings)
    dict_movies = get_movies(path_to_movies, dict_scores)

    arguments = Arguments()
    arguments.find_arguments()
    try:
        if arguments.regexp is not None:
            dict_movies = filter_by_regexp(dict_movies, arguments.regexp)
        if arguments.genres is not None:
            dict_movies = filter_by_genres(dict_movies, arguments.genres)
        if arguments.year_from is not None:
            dict_movies = filter_by_from_year(dict_movies, arguments.year_from)
        if arguments.year_to is not None:
            dict_movies = filter_by_to_year(dict_movies, arguments.year_to)
        print(dict_movies)
        # if arguments.count is not None:
        #     movies = sort_by_rating(dict_movies, arguments.count)
        # else:
        #     movies = sort_by_rating(dict_movies)
        print(arguments.genres, arguments.regexp, arguments.count, arguments.year_to, arguments.year_from)
    except BaseException as e:
        raise Exception('Data not found', e)





if __name__ == '__main__':
    main()
