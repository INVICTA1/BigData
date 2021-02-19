import sys
import argparse
import os
from converting import parsing_parquet_in_csv, get_parquet_schema, parsing_csv_in_parquet


def get_parse_arguments():
    """Create params command line"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')
    parser.add_argument('-o', '--outfile', default=None)
    parser.add_argument('-s', '--schema')

    return parser
def check_outfile(outfile):
    """ Check outfile file on right format"""

    format_outfile = os.path.splitext(outfile)[1]
    return format_outfile in ['.csv', '.parquet']

def main():
    """Processing the command line and calling functions for the parsing file """

    parser = get_parse_arguments()
    namespace = parser.parse_args(sys.argv[1:])  # 1-й параметр - расположение файла
    if namespace.outfile:
        if not check_outfile(namespace.outfile):
            return 'Outfile not csv or parquet format'
    if namespace.file:
        name_file = os.path.basename(namespace.file)
        format_file = os.path.splitext(name_file)[1]
        if format_file == '.csv':
            return parsing_csv_in_parquet(namespace.file, namespace.outfile)
        elif format_file == '.parquet':
            return parsing_parquet_in_csv(namespace.file, namespace.outfile)
        else:
            return 'Format file not csv or parquet'

    if namespace.schema:
        format_schema = os.path.splitext(namespace.schema)[-1]
        if format_schema == '.parquet':
            return get_parquet_schema(namespace.schema)
        else:
            return 'File not parquet format'


if __name__ == '__main__':
    main()
