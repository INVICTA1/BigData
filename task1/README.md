<h3>This project is used for:</h3>

1. Parsing data between csv and parquet format.
1. You can also see the schema parquet files.


The installation instructions assume that Python is installed on your device.
If you don't have Python installed, follow the link and download it.
https://www.python.org/downloads/

<h3>Usage</h3>

main.py [-f] file [-o] outfile [-s] schema  

    -f --file      File for data processing
    -o --outfile   The name of the file to be created after processing
    -s --schema    Get the schema parquet file

<h3>Examples</h3>

    main.py -f resources\csv\username-password-recovery-code.csv
    main.py -s resources\parquet\example.parquet 
    main.py -f resources\parquet\example.parquet -o example.csv 
    
<h3>Library</h3>

    pip install -r requirements.txt

<h3>Notes</h3>

Files for testing are in the folder resources
