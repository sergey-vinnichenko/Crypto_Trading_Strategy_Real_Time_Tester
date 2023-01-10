import sqlite3
from colorama import Style, Fore
from .convert_time import *

# This file contains all the functions for working with the STOP_LIST table.


# Creating a STOP_LIST table
def stop_list_create_table():
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute("""CREATE TABLE stop_list (
                      strategy integer,
                      coin text,
                      time real
                      )""")
    db.commit()
    db.close()
    print("STOP LIST table is created.")


# Creating a new record in the STOP_LIST table
def stop_list_add_record(strategy, coin, time):
    values = [strategy, coin, time]
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute('INSERT INTO stop_list VALUES (?, ?, ?)', values)
    db.commit()
    db.close()
    print(Fore.LIGHTMAGENTA_EX +
          "New STOP_LIST record is created." +
          Fore.BLACK)


# Deleting all records in tha STOP_LIST table
def stop_list_delete_all_records():
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute('DELETE FROM stop_list')
    db.commit()
    db.close()
    print('All records have been removed from the STOP LIST table')
    print()
    stop_list_print_all_records()


# УDeleting one strategy from the STOP_LIST table
def stop_list_delete_strategy(strategy):
    values = strategy,
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute('DELETE FROM stop_list '
                   'WHERE strategy = ?', values)
    db.commit()
    db.close()
    print(f"Strategy {strategy} have been removed from the SIGNALS table")
    print()
    stop_list_print_all_records()


# Reading all records in the STOP_LIST table
def stop_list_read_all_records():
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute('SELECT rowid, strategy, coin, time '
                   'FROM stop_list '
                   'ORDER BY time')
    db.commit()
    all_records = run_db.fetchall()
    db.close()
    return all_records


# Printing all records from the STOP_LIST table
def stop_list_print_all_records():
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute('SELECT rowid, strategy, coin, time '
                   'FROM stop_list '
                   'ORDER BY time')
    db.commit()
    all_records = run_db.fetchall()
    db.close()

    print("STOP LIST TABLE")
    stop_list_print_table(all_records)


# Printing STOP_LIST table records in a table format
def stop_list_print_table(records):
    print('-' * 34)
    print('id    '
          'str   '
          'coin      '
          'time')
    print('-' * 34)
    if records == []:
        print('No records')
    for item in records:
        print(f"{item[0]}{' '*(6-len(str(item[0])))}"
              f"{item[1]}{' '*(6-len(str(item[1])))}"
              f"{item[2]}{' '*(10-len(str(item[2])))}"
              f"{convert_time(item[3])}{' '*(14-len(str(convert_time(item[3]))))}")
    print()


# Getting time from the particular record from the STOP_LIST table
def stop_list_find_record_time(strategy, coin):
    try:
        values = [strategy, coin]
        db = sqlite3.connect('database.db')
        run_db = db.cursor()
        run_db.execute("""SELECT time FROM stop_list 
                          WHERE strategy = ? 
                          AND coin = ?""", values)
        time = run_db.fetchone()[0]
        db.commit()
        db.close()
        return time
    except TypeError:
        return False


# Getting particular record from the STOP_LIST table and setting a new time
def stop_list_change_record_time(strategy, coin, new_time):

    values = new_time, strategy, coin,
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute("""UPDATE stop_list 
                      SET time = ?   
                      WHERE strategy = ? 
                      AND coin = ?""", values)
    db.commit()
    values = strategy, coin
    run_db.execute("""SELECT rowid, strategy, coin, time
                      FROM stop_list 
                      WHERE strategy = ? 
                      AND coin = ?""", values)
    records = run_db.fetchall()
    db.commit()
    db.close()
    # stop_list_print_table(records)
