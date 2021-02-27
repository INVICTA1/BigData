import re


# return list(filter(lambda movie: re.search(regexp, movies[movie]['name']), movies))


def filter_by_regexp(dict_movies, regexp):
    try:
        new_dict_movies = {}
        for movie_id in dict_movies:
            if re.search(regexp, dict_movies[movie_id]['name']):
                new_dict_movies[movie_id] = dict_movies[movie_id]
        return new_dict_movies
    except BaseException as e:
        raise Exception('Data not found by regexp', e)


def filter_by_genres(dict_movies, genres):
    try:
        new_dict_movies = {}
        for movie_id in dict_movies:
            if set(dict_movies[movie_id]['genres']) & set(genres):
                new_dict_movies[movie_id] = dict_movies[movie_id]
        return new_dict_movies
    except BaseException as e:
        raise Exception('Data not found by genres', e)


def filter_by_from_year(dict_movies, year_from):
    try:
        new_dict_movies = {}
        for movie_id in dict_movies:
            if dict_movies[movie_id]['year'] is not None and dict_movies[movie_id]['year'] >= year_from:
                new_dict_movies[movie_id] = dict_movies[movie_id]
        return new_dict_movies
    except BaseException as e:
        raise Exception('Data not found by year from', e)


def filter_by_to_year(dict_movies, year_to):
    try:
        new_dict_movies = {}
        for movie_id in dict_movies:
            if dict_movies[movie_id]['year'] is not None and dict_movies[movie_id]['year'] <= year_to:
                new_dict_movies[movie_id] = dict_movies[movie_id]
        return new_dict_movies
    except BaseException as e:
        raise Exception('Data not found by to year', e)


def sort_by_rating(dict_movies, limit=None):
    try:
        sort_dict = {}
        list_movies = []
        for movie_id in dict_movies:
            sort_dict[movie_id] = dict_movies[movie_id]['rating']
        sort_movies = sorted(sort_dict.items(), key=lambda kv: kv[1], reverse=True)

        if limit is None or len(dict_movies) <= int(limit):
            for movie in sort_movies:
                list_movies.append(dict_movies[movie[0]])
            return list_movies
        else:
            for movie in sort_movies[:int(limit)]:
                list_movies.append(dict_movies[movie[0]])
            return list_movies
    except BaseException as e:
        raise Exception('Data not found', e)
