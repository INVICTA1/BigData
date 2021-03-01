import csv


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
