import os
from view import parsing_parquet_in_csv, get_parquet_schema, parsing_csv_in_parquet


def check_outfile(outfile):
    """ Check outfile file on right format"""

    format_outfile = os.path.splitext(outfile)[1]
    if format_outfile  in ['.csv', '.parquet']:
        return True
    else:
        return False


def check_file(file, outfile):
    """ Check input file file on right format"""

    name_file = os.path.basename(file)
    format_file = os.path.splitext(name_file)[1]
    if format_file == '.csv':
        return parsing_csv_in_parquet(file, outfile)
    elif format_file == '.parquet':
        return parsing_parquet_in_csv(file, outfile)
    else:
        return 'Format file not csv or parquet'


def check_schema(file):
    """ Check parquet file on right format"""

    format_schema = os.path.splitext(file)[-1]
    if format_schema == '.parquet':
        return get_parquet_schema(file)
    else:
        return 'File not parquet format'
