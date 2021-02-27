import sys
import argparse



def get_parser_arguments():
    """Create params command line"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--limit', type=int, default=None, help='Number of returned items')
    parser.add_argument('-r', '--regex', type=str, default=None, help='Regular expression')
    parser.add_argument('-g', '--genres', type=str, default=None, help='Genres of movie')
    parser.add_argument('-yf', '--year_from', type=int, default=None, help='Movies from a certain year')
    parser.add_argument('-yt', '--year_to', type=int, default=None, help='Movies up to a certain year')
    parser.add_argument('-c', '--csv', type=str, default=None, help='Writing to a csv file')

    return parser
