import os
import pandas as pd
from pyarrow import parquet, Table


def find_name_file(file_path):
    """Return name file which is being processed """

    file = os.path.basename(file_path)
    name_file = os.path.splitext(file)[0]
    return name_file


def parsing_csv_in_parquet(file_path, outfile):
    """ Parsing csv file in parquet file """

    try:
        file_csv = pd.read_csv(file_path, index_col=False, header=0)
        table = Table.from_pandas(file_csv, preserve_index=True)
        if not outfile:
            outfile = find_name_file(file_path) + '.parquet'
        parquet.write_table(table, outfile)
    except Exception as e:
        raise e


def parsing_parquet_in_csv(file_path, outfile):
    """ Parsing parquet file in csv file"""

    try:

        file_parquet = parquet.read_table(file_path)
        table = file_parquet.to_pandas()
        if not outfile:
            outfile = find_name_file(file_path) + '.csv'
        table.to_csv(outfile, index=False)
    except BaseException as e:
        raise e


def get_parquet_schema(file_path):
    """ Get schema from parquet file"""
    try:
        parquet_schema = parquet.ParquetFile(file_path)
        return parquet_schema.schema
    except Exception as e:
        raise e
