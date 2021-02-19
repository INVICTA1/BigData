import os
from view import parsing_parquet_in_csv, get_parquet_schema, parsing_csv_in_parquet


def check_outfile(outfile):
    """ Check outfile file on right format"""

    format_outfile = os.path.splitext(outfile)[1]
    if format_outfile in ['.csv', '.parquet']:
        return True
    else:
        return False


def check_file(path_file, outfile):
    """ Check input file file on right format"""

    name_file = os.path.basename(path_file)
    format_file = os.path.splitext(name_file)[1]
    if format_file == '.csv':
        return parsing_csv_in_parquet(path_file, outfile)
    elif format_file == '.parquet':
        return parsing_parquet_in_csv(path_file, outfile)
    else:
        return 'Format file not csv or parquet'


def check_schema(path_file):
    """ Check parquet file on right format"""

    format_schema = os.path.splitext(path_file)[-1]
    if format_schema == '.parquet':
        return get_parquet_schema(path_file)
    else:
        return 'File not parquet format'
