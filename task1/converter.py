import os
import pandas as pd
from pyarrow import parquet, Table


def get_file_name(infile):
    """Return file_name file which is being processed """

    basename = os.path.basename(infile)
    name_infile = os.path.splitext(basename)[0]

    return name_infile


def convert_csv_to_parquet(infile, outfile):
    """ Convert csv file in parquet file """

    try:
        csv_data = pd.read_csv(infile, index_col=False, header=0)
        csv_table = Table.from_pandas(csv_data, preserve_index=True)
        if not outfile:
            outfile = get_file_name(infile) + '.parquet'
        parquet.write_table(csv_table, outfile)
    except BaseException as e:
        raise e


def convert_parquet_to_csv(infile, outfile):
    """ Parsing parquet file in csv file"""

    try:
        parquet_file = parquet.read_table(infile)
        parquet_table = parquet_file.to_pandas()
        if not outfile:
            outfile = get_file_name(infile) + '.csv'
        parquet_table.to_csv(outfile, index=False)
    except BaseException as e:
        raise e


def get_parquet_schema(infile):
    """ Get schema from parquet file"""

    try:
        parquet_schema = parquet.ParquetFile(infile)
        return parquet_schema.schema
    except BaseException as e:
        raise e
