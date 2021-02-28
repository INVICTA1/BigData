import re


def filter_by_regexp(movies: list, regexp: str) -> list:
    """Filter data by parameter regexp"""

    return list(filter(lambda movie: re.search(regexp, movie['name']), movies))

    # how correctly to throw and catch exception?

    # try:
    #     result = []
    #     for movie in movies:
    #         if re.search(regexp, movie['name']):
    #             result.append(movie)
    #     return result
    # except BaseException as e:
    #     raise Exception('Data not found by regexp', e)


def filter_by_genres(movies: list, genres: str) -> list:
    """Filter data by parameter genres"""

    genres = genres.split('|')

    return list(filter(lambda movie: set(movie['genres']) & set(genres), movies))


def filter_by_from_year(movies: list, year_from: int) -> list:
    """Filter data by parameter year_from"""

    return list(filter(lambda movie: movie['year'] is not None and movie['year'] >= year_from, movies))


def filter_by_to_year(movies: list, year_to: int) -> list:
    """Filter data by parameter year_to"""

    return list(filter(lambda movie: movie['year'] is not None and movie['year'] <= year_to, movies))


def sort_by_rating_and_limit(movies: list) -> list:
    """The sort movies parameter depending on the rating"""

    return sorted(movies, key=lambda movie: movie['rating'], reverse=True)
