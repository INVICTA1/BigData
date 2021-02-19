<h3>This project is used for:</h3>
<ol>
    <li>Parsing data between csv and parquet format.</li>
    <li>You can also see the schema parquet files.</li>
</ol>

<p>The installation instructions assume that Python is installed on your device.
If you don't have Python installed, follow the link and download it.
https://www.python.org/downloads/</p>

<h3>Usage</h3>
<p>main.py [-f] file [-o] outfile [-s] schema  </p>

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
<p>Files for testing are in the folder <b>resources</b> </p>
