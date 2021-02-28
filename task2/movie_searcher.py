import csv
import os


def get_genres(cells):
    """Get genres from cells"""

    genres = cells[-1].replace('\n', '')

    return genres.split('|')


def get_name(cells):
    """Return file_name"""

    year, list_words_from_name = get_name_and_year(cells)
    if year.isdigit():
        name = ' '.join(list_words_from_name[:-1])
    else:
        name = ' '.join(list_words_from_name)

    return name


def get_year(cells):
    """Return year"""

    year, list_words = get_name_and_year(cells)
    if not year.isdigit():
        year = None
    else:
        year = int(year)

    return year


def get_name_and_year(cells):
    """Find file_name and year from cells and return this data"""

    if cells.__len__() == 3:
        name_with_year = cells[1]
    else:
        name_with_year = ','.join(cells[1:-1])
    words_list = name_with_year.split(' ')
    year_from_name = words_list[-1]
    year = year_from_name[year_from_name.find('(') + 1: year_from_name.find(')')]

    return year, words_list


def read_scores(path: str) -> dict:
    """Read csv file and return dict{movieId:[rating]}"""

    score_dict = {}
    with open(path) as csv_file:
        for line in csv_file:
            row = csv_file.readline()
            cells = row.split(',')
            movie_id = int(cells[1])
            score = cells[2]
            if score_dict.get(movie_id):
                score_dict[movie_id].append(float(score))
            else:
                score_dict[movie_id] = [float(score)]

    return score_dict


def map_scores_to_movies(movies: list, scores: dict) -> list:
    """Map scores to movies"""

    for movie in movies:
        if scores.get(movie['id']):
            score = scores[movie['id']]
            rating = round(sum(score) / len(score), 1)
            movie['rating'] = rating
        else:
            movie['rating'] = 0

    return movies


def read_movies(path: str) -> list:
    """Read CSV file adn create movie dictionary """

    movies = []
    with open(path) as csv_file:
        for line in csv_file:
            row = csv_file.readline()
            if row:
                cells = row.split(',')
                id = int(cells[0])
                genres = get_genres(cells)
                name = get_name(cells)
                year = get_year(cells)
                movies.append({'id': id,
                               'name': name,
                               'year': year,
                               'genres': genres})

    return movies


def write_result_to_csv(movies: list, file_name: str):
    """Write result to csv file"""

    csv_file = os.path.splitext(file_name)[0] + '.csv'
    with open(csv_file, "w", newline="") as file:
        columns = ['name', 'year', 'genres', 'rating']
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        for movie in movies:
            movie['genres'] = '|'.join(movie['genres'])
        writer.writerows(movies)


def print_result(movies: list):
    """Output result on console"""

    result = 'name;year;genres;rating\n'
    delimiter = '; '
    for movie in movies:
        name = movie['name']
        year = str(movie['year'])
        genres = '|'.join(movie['genres'])
        rating = str(movie['rating'])
        result += name + delimiter + year + delimiter + genres + delimiter + rating + '\n'
    print(result)
