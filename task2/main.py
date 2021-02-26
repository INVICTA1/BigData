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
            list_from_row = row.split(',')
            movie_id = int(list_from_row[1])
            score = list_from_row[2]
            if ratings.get(movie_id):
                ratings[movie_id].append(float(score))
            else:
                ratings[movie_id] = [float(score)]

    return ratings





def get_genres(row_list):
    genres = row_list[-1].replace('\n', '')
    list_genres = genres.split('|')
    return list_genres


def get_name_and_year(row_list):
    if row_list.__len__() == 3:
        name_with_year = row_list[1]
    else:
        name_with_year = ','.join(row_list[1:-1])
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
    if dict_ratings.get(movie_id):
        list_ratings = dict_ratings[movie_id]
        rating = round(sum(list_ratings) / len(list_ratings), 1)
    else:
        rating = None
    return rating


def create_dict_from_file(path):
    dict_movies = {}
    ratings_dict = get_dict_ratings(path_to_ratings)
    with open(path) as csv_file:
        for line in csv_file:
            row = csv_file.readline()
            if row:
                row_list = row.split(',')
                movie_id = int(row_list[0])
                list_genres = get_genres(row_list)
                name_movie, year = get_name_and_year(row_list)
                rating = get_rating(ratings_dict, movie_id)
                # print(movie_id,list_genres,name_movie,year,rating)
                dict_movies[movie_id] = {'name': name_movie,
                                         'year': year,
                                         'genres': list_genres,
                                         'rating': rating}
    return dict_movies


def main():
    dict_movies = create_dict_from_file(path_to_movies)
    print(dict_movies)

if __name__ == '__main__':
    main()
