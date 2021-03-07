import mysql.connector
from mysql.connector import Error
import os
from config import config

ddl_db_script = r'db/ddl/'
dml_db_script = r'db/dml/'


def connect_to_database():
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except Error as e:
        conn.close()
        raise ("Can't connect to database", e)


def upload_files(ddl_db_script, cursor):
    list_files = os.listdir(ddl_db_script)
    for file in list_files:
        file = ddl_db_script + file
        with open(file) as sql_file:
            cursor.execute(sql_file.read())



def run_script_to_db():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.stored_results()
            upload_files(ddl_db_script, cursor)
            upload_files(dml_db_script, cursor)
            conn.commit()
            conn.close()
    except  (BaseException, Error) as e:
        raise ("Can't run script to db", e)


if __name__ == '__main__':
    run_script_to_db()
