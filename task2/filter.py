def filter_by_regexp(dict_movies, regexp):
    try:
        new_dict_movies = {}
        for movie_id in dict_movies:
            if dict_movies[movie_id]['name'].__contains__(regexp):
                new_dict_movies[movie_id] = dict_movies[movie_id]
        return new_dict_movies
    except BaseException as e:
        raise Exception('Data not found', e)


def filter_by_genres(dict_movies, genres):
    try:
        new_dict_movies = {}
        for movie_id in dict_movies:
            if set(dict_movies[movie_id]['genres']) & set(genres):
                new_dict_movies[movie_id] = dict_movies[movie_id]
        return new_dict_movies
    except BaseException as e:
        raise Exception('Data not found', e)


def filter_by_from_year(dict_movies, year_from):
    try:
        new_dict_movies = {}
        for movie_id in dict_movies:
            if dict_movies[movie_id]['year'] is not None and dict_movies[movie_id]['year'] >= year_from:
                new_dict_movies[movie_id] = dict_movies[movie_id]
        return new_dict_movies
    except BaseException as e:
        raise Exception('Data not found year_from', e)


def filter_by_to_year(dict_movies, year_to):
    try:
        new_dict_movies = {}
        for movie_id in dict_movies:
            if dict_movies[movie_id]['year'] is not None and dict_movies[movie_id]['year'] <= year_to:
                new_dict_movies[movie_id] = dict_movies[movie_id]
        return new_dict_movies
    except BaseException as e:
        raise Exception('Data not found', e)