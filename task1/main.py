import os
import pandas as pd
from pyarrow import parquet, Table

# csv_path_file = 'resources/csv/userdata1.csv'
# parquet_path_file = 'resources/parquet/userdata5.parquet'

parquet_folder = 'resources/parquet/parsing-csv-files/'
csv_folder = 'resources/csv/parsing-parquet-files/'


def find_name_file(path_file):
    file = os.path.basename(path_file)
    name_file = os.path.splitext(file)[0]
    return name_file


def parsing_csv_in_parquet():
    """ Parsing csv file in parquet file """
    path_file = input('Enter path to file: ')
    file_csv = pd.read_csv(path_file, index_col=False)
    parquet_file = parquet_folder + find_name_file(path_file) + '.parquet'
    table = Table.from_pandas(file_csv, preserve_index=False)
    parquet.write_table(table, parquet_file)
    return 'File: ' + parquet_file


def parsing_parquet_in_csv():
    """ Parsing parquet file in csv file"""
    path_file = input('Enter path to file: ')
    file_parquet = parquet.read_table(path_file)
    csv_file = csv_folder + find_name_file(path_file) + '.csv'
    table = file_parquet.to_pandas()
    table.to_csv(csv_file)
    return 'File: ' + csv_file


def get_parquet_schema():
    """ Get schema from parquet file"""
    path_file = input('Enter path to file: ')
    parquet_schema = parquet.ParquetFile(path_file)
    return parquet_schema.schema


def main():
    methods = {1: parsing_csv_in_parquet,
               2: parsing_parquet_in_csv,
               3: get_parquet_schema}
    while True:
        try:
            num = int(input('1 : parsing csv in parquet\n'
                            '2 : parsing parquet in csv\n'
                            '3 : get parquet schema\n'
                            'Exit : any symbol'
                            'Enter number: '))
            print(methods[num]())
        except:
            break

if __name__=='__main__':
    main()
