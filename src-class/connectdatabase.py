# Notes: Replace password dengan password database mariadb
# Notes: Replace port dengan port yang sesuai

import mariadb
# import mysql.connector   

try:
    conn = mariadb.connect (
        user = 'root',
        password = '',
        host = 'localhost',
        port = 3306,
        database = 'myhotel'
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")