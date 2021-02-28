import csv
import re


def split_genres(cell: str) -> list:
    """Split genres from cell"""

    return cell.split('|')


def get_name(cell: str) -> str:
    """search for a name in a cell"""

    return re.sub(r'\((\d+)\)', '', cell)


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
            score = scores[movie['id']]
            rating = round(sum(score) / len(score), 1)
            movie['rating'] = rating
        else:
            movie['rating'] = 0

    return movies


def read_movies(path: str) -> list:
    """Read CSV file adn create movie dictionary """

    movies = []
    with open(path, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            id = int(row[0])
            name = get_name(row[1])
            year = get_year(row[1])
            genres = split_genres(row[2])
            movies.append({'id': id,
                           'name': name,
                           'year': year,
                           'genres': genres})

    return movies
