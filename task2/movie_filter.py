import re


def filter_by_regexp(movies: list, regexp: str) -> list:
    """Filter data by parameter regexp"""

    try:
        result = []
        for movie in movies:
            if re.search(regexp, movie['name']):
                result.append(movie)
        return result
    except BaseException as e:
        raise Exception('Error when filtering regex', e)


def filter_by_genres(movies: list, genres: str) -> list:
    """Filter data by parameter genres"""

    try:
        genres = genres.split('|')
        result = []
        for movie in movies:
            if set(movie['genres']) & set(genres):
                result.append(movie)
        return result
    except BaseException as e:
        raise Exception('Error when filtering genres', e)


def filter_by_from_year(movies: list, year_from: int) -> list:
    """Filter data by parameter year_from"""

    try:
        result = []
        for movie in movies:
            if movie['year'] is not None and movie['year'] >= year_from:
                result.append(movie)
        return result
    except BaseException as e:
        raise Exception('Error when filtering from year', e)


def filter_by_to_year(movies: list, year_to: int) -> list:
    """Filter data by parameter year_to"""

    try:
        result = []
        for movie in movies:
            if movie['year'] is not None and movie['year'] <= year_to:
                result.append(movie)
        return result
    except BaseException as e:
        raise Exception('Error when filtering up to a year', e)


def sort_by_rating(movies: list) -> list:
    """The sort movies parameter depending on the rating"""

    return sorted(movies, key=lambda movie: movie['rating'], reverse=True)


def sort_by_number_genres(movies: list, genres: str, number: int) -> list:
    """The sort movies parameter depending on the rating and genres and return limit """

    try:
        result = []
        genres = genres.split('|')
        movies = sorted(movies, key=lambda movie: movie['rating'], reverse=True)
        for genre in genres:
            limit = 0
            for movie in movies:
                if genre in movie['genres'] and limit <= number:
                    result.append({'genres': genre,
                                   'name': movie['name'],
                                   'year': movie['year'],
                                   'rating': movie['rating']})
                    limit += 1
                elif limit > number:
                    continue
        return result
    except BaseException as e:
        raise Exception('Data not found', e)
