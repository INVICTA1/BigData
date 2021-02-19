import os
import pandas as pd
from pyarrow import parquet, Table
import sys
import argparse


def find_name_file(path_file):
    """Return name file which is being processed """

    file = os.path.basename(path_file)
    name_file = os.path.splitext(file)[0]
    return name_file


def parsing_csv_in_parquet(file, outfile):
    """ Parsing csv file in parquet file """

    try:
        file_csv = pd.read_csv(file, index_col=False, header=0)
        table = Table.from_pandas(file_csv, preserve_index=True)
        if not outfile:
            outfile = find_name_file(file) + '.parquet'
        parquet.write_table(table, outfile)
        return 'File: ' + outfile
    except Exception as e:
        return e


def parsing_parquet_in_csv(file, outfile):
    """ Parsing parquet file in csv file"""

    try:

        file_parquet = parquet.read_table(file)
        table = file_parquet.to_pandas()
        if not outfile:
            outfile = find_name_file(file) + '.csv'
        table.to_csv(outfile,index=False)
        return 'File: ' + outfile
    except BaseException as e:
        return 'Error:', e


def get_parquet_schema(file):
    """ Get schema from parquet file"""
    try:
        parquet_schema = parquet.ParquetFile(file)
        return parquet_schema.schema
    except Exception as e:
        return e


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')
    parser.add_argument('-o', '--outfile', default=None)
    parser.add_argument('-s', '--schema')

    return parser


def main():
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])  # 1-й параметр - расположение файла
    if namespace.outfile:
        format_outfile = os.path.splitext(namespace.outfile)[1]
        if format_outfile not in ['.csv', '.parquet']:
            return 'Outfile not csv or parquet format'
    elif namespace.file:
        file = os.path.basename(namespace.file)
        format_file = os.path.splitext(file)[1]
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
    print(main())
