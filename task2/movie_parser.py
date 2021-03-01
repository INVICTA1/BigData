import csv
import re


def split_genres(cell: str) -> list:
    """Split genres from cell"""

    return cell.split('|')


def get_name(cell: str) -> str:
    """search for a name in a cell"""

    return re.sub(r'\((\d+)\)', '', cell).strip()


def get_year(cell: str) -> int:
    """Search for the year in a cell"""

    year = re.search(r'\((\d+)\)', cell)
    if year is not None:
        year = int(year.group(0)[1:-1])
    else:
        year = 0

    return year


def map_scores_to_movies(movies: list, scores: dict) -> list:
    """Map scores to movies"""

    for movie in movies:
        if scores.get(movie['id']):
            sum = scores[movie['id']]['sum']
            num = scores[movie['id']]['num']
            rating = round(sum / num, 1)
            movie['rating'] = rating
        else:
            movie['rating'] = 0

    return movies


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


def read_movies(path: str) -> list:
    """Read CSV file adn create movie dictionary """

    try:
        movies = []
        with open(path, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)
            for movie_id, title, genres in reader:
                id = int(movie_id)
                name = get_name(title)
                year = get_year(title)
                genres = split_genres(genres)
                movies.append({'id': id,
                               'name': name,
                               'year': year,
                               'genres': genres})

        return movies
    except BaseException as e:
        raise Exception("Can't read movies file", e)


def read_rating(path: str) -> dict:
    """Read csv file and return dict{movieId:[rating]}"""
    try:
        scores = {}
        with open(path, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                movie_id = int(row[1])
                score = float(row[2])
                if scores.get(movie_id):
                    scores[movie_id]['sum'] += score
                    scores[movie_id]['num'] += 1
                else:
                    scores[movie_id] = {'sum': score, 'num': 1}
        return scores
    except BaseException as e:
        raise Exception("Can't read rating file", e)
