import csv
from argument import Arguments
from filter import filter_by_regexp, filter_by_genres, filter_by_from_year, filter_by_to_year, sort_by_rating

FILENAME = "movies.csv"
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


def get_name(cells):
    """Return name"""

    year, list_words_from_name = find_name_and_year(cells)
    if year.isdigit():
        name_movie = ' '.join(list_words_from_name[:-1])
    else:
        name_movie = ' '.join(list_words_from_name)

    return name_movie


def get_rating(dict_ratings, movie_id):
    """Find average rating and return rating data """

    if dict_ratings.get(movie_id):
        list_score = dict_ratings[movie_id]
        rating = round(sum(list_score) / len(list_score), 1)
    else:
        rating = 0

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


def get_year(cells):
    """Return year"""

    year, list_words_from_name = find_name_and_year(cells)
    if not year.isdigit():
        year = None

    return year


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


def write_movies_to_csv(list_movies):
    """Write result to csv file"""

    with open(FILENAME, "w", newline="") as file:
        columns = ['name', 'year', 'genres', 'rating']
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        for movie in list_movies:
            movie['genres'] = '|'.join(movie['genres'])
        writer.writerows(list_movies)


def output_movies(list_movies):
    """Output result on console"""

    result = 'name;year;genres;rating\n'
    delimiter = '; '
    for movie in list_movies:
        name = movie['name']
        year = str(movie['year'])
        genres = '|'.join(movie['genres'])
        rating = str(movie['rating'])
        result += name + delimiter + year + delimiter + genres + delimiter + rating + '\n'
    print(result)


def main():
    """Processing the command line and output result"""

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
        if arguments.limit is not None:
            list_movies = sort_by_rating(dict_movies, arguments.limit)
        else:
            list_movies = sort_by_rating(dict_movies)
        if arguments.csv is not None:
            write_movies_to_csv(list_movies)
        else:
            output_movies(list_movies)
    except BaseException as e:
        raise Exception('Data not found', e)


if __name__ == '__main__':
    main()
