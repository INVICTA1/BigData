import sys
import argparse
from service import check_outfile, check_schema, check_file


def createParser():
    """Create params command line"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')
    parser.add_argument('-o', '--outfile', default=None)
    parser.add_argument('-s', '--schema')

    return parser


def main():
    """Processing the command line and calling functions for the parsing file """

    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])  # 1-й параметр - расположение файла
    if namespace.outfile:
        if not check_outfile(namespace.outfile):
            return 'Outfile not csv or parquet format'
    if namespace.file:
        return check_file(namespace.file, namespace.outfile)
    if namespace.schema:
        return check_schema(namespace.schema)


if __name__ == '__main__':
    print(main())
