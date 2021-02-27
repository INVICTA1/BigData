import re


def filter_by_regexp(movie_dict, regexp):
    """Filter data by parameter regexp"""

    try:
        result = {}
        for movie_id in movie_dict:
            if re.search(regexp, movie_dict[movie_id]['name']):
                result[movie_id] = movie_dict[movie_id]
        return result
    except BaseException as e:
        raise Exception('Data not found by regexp', e)


def filter_by_genres(movie_dict, genres):
    """Filter data by parameter genres"""

    try:
        genres = genres.split('|')
        result = {}
        for movie_id in movie_dict:
            if set(movie_dict[movie_id]['genres']) & set(genres):
                result[movie_id] = movie_dict[movie_id]
        return result
    except BaseException as e:
        raise Exception('Data not found by genres', e)


def filter_by_from_year(movie_dict, year_from):
    """Filter data by parameter year_from"""

    try:
        result = {}
        for movie_id in movie_dict:
            if movie_dict[movie_id]['year'] is not None and movie_dict[movie_id]['year'] >= year_from:
                result[movie_id] = movie_dict[movie_id]
        return result
    except BaseException as e:
        raise Exception('Data not found by year from', e)


def filter_by_to_year(movie_dict, year_to):
    """Filter data by parameter year_to"""

    try:
        result = {}
        for movie_id in movie_dict:
            if movie_dict[movie_id]['year'] is not None and movie_dict[movie_id]['year'] <= year_to:
                result[movie_id] = movie_dict[movie_id]
        return result
    except BaseException as e:
        raise Exception('Data not found by to year', e)


def sort_by_rating(movie_dict, limit=None):
    """The sort movies parameter depending on the rating"""
        
    try:
        sort_dict = {}
        result = []
        for movie_id in movie_dict:
            sort_dict[movie_id] = movie_dict[movie_id]['rating']
        sort_movies = sorted(sort_dict.items(), key=lambda kv: kv[1], reverse=True)

        if limit is None or len(movie_dict) <= int(limit):
            for movie in sort_movies:
                result.append(movie_dict[movie[0]])
            return result
        else:
            for movie in sort_movies[:int(limit)]:
                result.append(movie_dict[movie[0]])
            return result
    except BaseException as e:
        raise Exception('Data not found', e)
