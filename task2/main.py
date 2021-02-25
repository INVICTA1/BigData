import builtins
import sys

path_to_movies = r'resources\movies.csv'
path_to_ratings = r'resources\ratings.csv'


class Params:
    def __init__(self, count, genres, year_from, year_to, regexp):
        self.count = count
        self.genres = genres
        self.year_from = year_from
        self.year_to = year_to
        self.regexp = regexp


def get_dict_ratings(path):
    """Read csv file and return dict{movieId:[rating]}"""
    ratings = {}
    with open(path) as csv_file:
        for line in csv_file:
            row = csv_file.readline()
            row_list = row.split(',')
            movie_id = row_list[1]
            score = row_list[2]
            if ratings.get(movie_id):
                ratings[movie_id].append(float(score))
            else:
                ratings[movie_id] = [float(score)]

    return ratings


def write_genres_to_dict(movie_id, genres, dict_genres):
    for genre in genres:
        if dict_genres.get(genre):
            dict_genres[genre].append(movie_id)
        else:
            dict_genres[genre] = [movie_id]
    return dict_genres


def create_movie_dict(movie_id, genres, name, year, rating):
    # movie_dict = {'movie_id': {
    #                     {'genres': ['жанр']},
    #                     {'name': 'имя'},
    #                     {'year': 'year'},
    #                     {'rating': 'rating'}, }
    #             }

    movie_dict = {movie_id}


def main(path):
    ratings_dict = get_dict_ratings(path_to_ratings)
    movies_dict = {}
    with open(path) as csv_file:
        for line in csv_file:
            row = csv_file.readline()
            if row:

                row_list = row.split(',')
                movie_id = int(row_list[0])
                # genres
                genres = row_list[-1].replace('\n', '')
                genres = genres.split('|')
                # name
                if row_list.__len__() == 3:
                    name = row_list[1]
                else:
                    name = ','.join(row_list[1:-1])

                # year
                name_list = name.split(' ')
                name = ' '.join(name_list[0:-1])

                year_new = name_list[-1]

                year = year_new[year_new.find('(') + 1: year_new.find(')')]
                if not year.isdigit():
                    year = ''

                # ratings
                if ratings_dict.get(movie_id):
                    rating_list = ratings_dict[movie_id]
                    rating = round(sum(rating_list) / len(rating_list), 1)
                else:
                    rating = 0
                movies_dict[movie_id] = {}
                movies_dict[movie_id]['name'] = name
                movies_dict[movie_id]['year'] = year
                movies_dict[movie_id]['genres'] = genres
                movies_dict[movie_id]['rating'] = rating

        print(movies_dict)
                # genres_dict = write_genres_to_dict(movie_id, genres, genres_dict)
                # create_movie_dict(movie_id,genres)

main(path_to_movies)
                # Tasks
                # просчитать для каждого фильма средний рейтинг(по id в rating файле)
                # записать в промежуточный хеш значение id и среднего фильма и потом при чтении фильмов брать данный из хеша
movies = {'name': {'year': '', 'genres': [], 'movieId': '', 'rating': ''}}
moviess = {'genres': {'year': '', 'genres': [], 'movieId': '', 'rating': ''}}
genres = {'Animation|Comedy|Fantasy': "movieId"}
