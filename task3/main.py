import sys
import argparse
from connector import connect_to_database
from mysql.connector import Error


def get_parser_arguments():
    """Create params command line"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', type=int, default=None, help='Number of returned items')
    parser.add_argument('-r', '--regex', type=str, default=None, help='Regular expression')
    parser.add_argument('-g', '--genres', type=str, default=None, help='Genres of movie')
    parser.add_argument('-yf', '--year_from', type=int, default=None, help='Movies from a certain year')
    parser.add_argument('-yt', '--year_to', type=int, default=None, help='Movies up to a certain year')
    parser.add_argument('-c', '--csv', type=str, default=None, help='Writing to a csv file')

    return parser


def main():
    """Processing the command line and output result"""
    try:
        parser = get_parser_arguments()
        namespace = parser.parse_args(sys.argv[1:])
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            params = [namespace.number,namespace.regex,namespace.year_from, namespace.year_to,namespace.genres]
            cursor.callproc('usp_find_top_rated_movies',params)
            for result in cursor.stored_results():
                results = result.fetchall()
            for row in results:
                if row:
                    print(','.join(map(str,row)))
    except (BaseException, Error) as e:
        raise Exception("The program cannot be executed", e)


if __name__ == '__main__':
    main()