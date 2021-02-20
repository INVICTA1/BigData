import sys
import argparse
import os
from converter import convert_parquet_to_csv, get_parquet_schema, convert_csv_to_parquet, get_file_name


def get_parser_arguments():
    """Create params command line"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')
    parser.add_argument('-o', '--outfile', default=None)
    parser.add_argument('-s', '--schema')

    return parser


def main():
    """Processing the command line and calling functions for the parsing file """

    dict_methods = {'.csv': convert_csv_to_parquet,
                    '.parquet': convert_parquet_to_csv}
    try:
        parser = get_parser_arguments()
        namespace = parser.parse_args(sys.argv[1:])
        if namespace.file:
            basename = os.path.basename(namespace.file)
            extension_infile = os.path.splitext(basename)[-1]
            dict_methods[extension_infile](namespace.file, namespace.outfile)
        elif namespace.schema:
            return get_parquet_schema(namespace.schema)
    except BaseException as e:
        raise e


if __name__ == '__main__':
    main()
