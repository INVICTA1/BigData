def get_genres(cells):
    """Get genres from cells"""

    genres = cells[-1].replace('\n', '')

    return genres.split('|')


def get_name(cells):
    """Return name"""

    year, list_words_from_name = find_name_and_year(cells)
    if year.isdigit():
        name = ' '.join(list_words_from_name[:-1])
    else:
        name = ' '.join(list_words_from_name)

    return name


def get_rating(dict_ratings, movie_id):
    """Find average rating and return rating data """

    if dict_ratings.get(movie_id):
        scores = dict_ratings[movie_id]
        rating = round(sum(scores) / len(scores), 1)
    else:
        rating = 0

    return rating


def get_year(cells):
    """Return year"""

    year, list_words = find_name_and_year(cells)
    if not year.isdigit():
        year = None
    else:
        year = int(year)

    return year


def find_name_and_year(cells):
    """Find name and year from cells and return this data"""

    if cells.__len__() == 3:
        name_with_year = cells[1]
    else:
        name_with_year = ','.join(cells[1:-1])
    words_list = name_with_year.split(' ')
    year_from_name = words_list[-1]
    year = year_from_name[year_from_name.find('(') + 1: year_from_name.find(')')]

    return year, words_list


def get_scores(path):
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


def get_movies(path, score_dict):
    """Read CSV file adn create movie dictionary """

    movie_dict = {}
    with open(path) as csv_file:
        for line in csv_file:
            row = csv_file.readline()
            if row:
                cells = row.split(',')
                movie_id = int(cells[0])
                genres = get_genres(cells)
                name_movie = get_name(cells)
                year = get_year(cells)
                rating = get_rating(score_dict, movie_id)
                movie_dict[movie_id] = {'name': name_movie,
                                        'year': year,
                                        'genres': genres,
                                        'rating': rating}

    return movie_dict
