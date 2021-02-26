import builtins
import sys
from params import Arguments

path_to_movies = r'resources\movies.csv'
path_to_ratings = r'resources\ratings.csv'


def get_dict_scores(path):
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
    list_genres = genres.split('|')

    return list_genres


def get_name_and_year(cells):
    """Find name and year from cells and return this data"""

    if cells.__len__() == 3:
        name_with_year = cells[1]
    else:
        name_with_year = ','.join(cells[1:-1])
    list_words_from_name = name_with_year.split(' ')
    year_from_name = list_words_from_name[-1]
    year = year_from_name[year_from_name.find('(') + 1: year_from_name.find(')')]
    if year.isdigit():
        name_movie = ' '.join(list_words_from_name[:-1])
    else:
        name_movie = ' '.join(list_words_from_name)
        year = None

    return name_movie, year


def get_rating(dict_ratings, movie_id):
    """Find average rating and return rating data """

    if dict_ratings.get(movie_id):
        list_score = dict_ratings[movie_id]
        rating = round(sum(list_score) / len(list_score), 1)
    else:
        rating = None

    return rating


def read_file(path):
    """Read CSV file adn create movie dictionary """

    dict_movies = {}
    dict_scores = get_dict_scores(path_to_ratings)
    with open(path) as csv_file:
        for line in csv_file:
            row = csv_file.readline()
            if row:
                cells = row.split(',')
                movie_id = int(cells[0])
                list_genres = get_genres(cells)
                name_movie, year = get_name_and_year(cells)
                rating = get_rating(dict_scores, movie_id)
                dict_movies[movie_id] = {'name': name_movie,
                                         'year': year,
                                         'genres': list_genres,
                                         'rating': rating}

    return dict_movies


def main():
    # dict_movies = read_file(path_to_movies)
    arguments = Arguments()
    arguments.find_arguments()


if __name__ == '__main__':
    main()
