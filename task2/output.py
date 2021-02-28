import csv
import os


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
