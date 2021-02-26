import sys


# count -n, regexp -r genres -g, year_from -yf,year_to -yt,

class Arguments:
    def __init__(self):
        self.argument_count = '-n'
        self.argument_regexp = '-r'
        self.argument_genres = '-g'
        self.argument_year_from = '-yf'
        self.argument_year_to = '-yt'

        self.count = None
        self.regexp = None
        self.genres = None
        self.year_from = None
        self.year_to = None

    @staticmethod
    def get_argument(list_arguments, argument):
        if argument in list_arguments:
            return list_arguments[list_arguments.index(argument) + 1]

    def find_arguments(self):
        list_arguments = sys.argv[1:]
        if list_arguments.__len__() % 2 == 0 and list_arguments.__len__() > 10:
            raise Exception('Data entered incorrectly')
        self.count = self.get_argument(list_arguments, self.argument_count)
        self.regexp = self.get_argument(list_arguments, self.argument_regexp)
        genres = self.get_argument(list_arguments, self.argument_genres)
        if genres is not None:
            self.genres = genres.split('|')
        self.year_from = self.get_argument(list_arguments, self.argument_year_from)
        self.year_to = self.get_argument(list_arguments, self.argument_year_to)
