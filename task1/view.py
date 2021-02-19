import os
import pandas as pd
from pyarrow import parquet, Table


def find_name_file(path_file):
    """Return name file which is being processed """

    file = os.path.basename(path_file)
    name_file = os.path.splitext(file)[0]
    return name_file


def parsing_csv_in_parquet(path_file, outfile):
    """ Parsing csv file in parquet file """

    try:
        file_csv = pd.read_csv(path_file, index_col=False, header=0)
        table = Table.from_pandas(file_csv, preserve_index=True)
        if not outfile:
            outfile = find_name_file(path_file) + '.parquet'
        parquet.write_table(table, outfile)
        return 'File: ' + outfile
    except Exception as e:
        raise e


def parsing_parquet_in_csv(path_file, outfile):
    """ Parsing parquet file in csv file"""

    try:

        file_parquet = parquet.read_table(path_file)
        table = file_parquet.to_pandas()
        if not outfile:
            outfile = find_name_file(path_file) + '.csv'
        table.to_csv(outfile, index=False)
        return 'File: ' + outfile
    except BaseException as e:
        raise e


def get_parquet_schema(path_file):
    """ Get schema from parquet file"""
    try:
        parquet_schema = parquet.ParquetFile(path_file)
        return parquet_schema.schema
    except Exception as e:
        raise e
