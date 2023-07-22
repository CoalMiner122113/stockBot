import mysql.connector as sql
from mysql.connector import errorcode
from dotenv import dotenv_values

config = dotenv_values(".env")

database = 'test'

def setup():
    try:
        cnx = sql.connect(host=config['MYSQL_HOST'], 
                          user=config['MYSQL_USER'], 
                          password=config['MYSQL_PASS'])
        if cnx.is_connected():
            print('Connected to MySQL database')
            cursor = cnx.cursor()
            cursor.execute('CREATE DATABASE IF NOT EXISTS ' + database)
            cursor.execute('USE '+ database)
            cursor.execute('CREATE TABLE IF NOT EXISTS testTable (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)')
            print('Database and table created successfully')
            cursor.close()
            cnx.close()
    except sql.Error as e:
        print('Error while connecting to MySQL', e)

#setup()