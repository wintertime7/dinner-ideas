import sqlite3

from dinner_ideas_main import logging

#connects to an database file, if it doesnt exist, then creates one, then makes an cursor
conn = sqlite3.connect('dinner_ideas_database.db')
c = conn.cursor()

#function to create tables, if an table by that name doesnt exist already
#gives the table collumns
def creating_tables(table_name):
    try :
        logging.info('Creating table ' + table_name + '...')
        c.execute("""CREATE TABLE IF NOT EXISTS """ + table_name + """ (
            name text,
            number integer
            )""")
    except :
        logging.warning('Ah, pickles! Something wrong with table creation!')
        print('Ah, pickles! Something wrong with table creation!')

#function to add values into an specified table, didnt use formating to avoid security issues
def adding_values(table_name, food_name, food_number):
    try :
        logging.info('Inserting values into ' + table_name + ' table...')
        with conn:
            c.execute("INSERT INTO " + table_name + " VALUES (?, ?)", (food_name, food_number))
    except :
        logging.warning('Ah, pickles! Something wrong with value insertion!')
        print('Ah, pickles! Something wrong with value insertion!')

#function to create an migration table in database
def create_migration_table() :
    try :
        logging.info('Creating migrations table...')
        c.execute("""CREATE TABLE IF NOT EXISTS migrations (
            name text,
            date text
            )""")
    except :
        logging.warning('Ah, pickles! Something wrong with migration table creation!')
        print('Ah, pickles! Something wrong with migration table creation!')

conn.close
