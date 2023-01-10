import sqlite3
from colorama import Fore
from .convert_time import convert_time

# This file contains all the functions for working with the Signals table.

# Creating SIGNALS table
def signals_create_table():
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute("""CREATE TABLE signals (
                      strategy integer,
                      coin text,
                      signal text,
                      price real,
                      take_profit real,
                      stop_loss real,
                      result text,
                      signal_time real,
                      result_time real,
                      strategy_doc text
                      )""")
    db.commit()
    db.close()
    print(f"SIGNALS table is created")


# Creating a new record in a SIGNALS table
def signals_add_record(strategy,
                       coin,
                       signal,
                       price,
                       take_profit,
                       stop_loss,
                       result,
                       signal_time,
                       result_time,
                       strategy_doc):
    values = [strategy,
              coin,
              signal,
              price,
              take_profit,
              stop_loss,
              result,
              signal_time,
              result_time,
              strategy_doc]
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute("""INSERT INTO signals 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", values)
    db.commit()
    db.close()
    print(Fore.LIGHTMAGENTA_EX +
          f"New SIGNAL record is created" +
          Fore.BLACK)


# Deleting all records from the SIGNALS table
def signals_delete_all_records():
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute('DELETE FROM signals')
    db.commit()
    db.close()
    print(f"All records have been removed from the SIGNALS table")
    print()
    signals_print_all_records()


# Deleting one record from the SIGNALS record
def signals_delete_one_record(rowid):
    values = rowid,
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute("""DELETE FROM signals
                   WHERE rowid = ?""", values)
    db.commit()
    db.close()
    print(f"One record have been removed from the SIGNALS table")
    print()
    signals_print_all_records()


# Deleting one strategy from the SIGNALS table
def signals_delete_one_strategy(strategy):
    values = strategy,
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute("""DELETE FROM signals
                   WHERE strategy = ?""", values)
    db.commit()
    db.close()
    print(f"Strategy {strategy} have been removed from the SIGNALS table")
    print()
    signals_print_all_records()


# Reading all records from the SIGNALS table
def signals_read_all_records():
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute("""SELECT rowid, * FROM signals""")
    db.commit()
    all_records = run_db.fetchall()

    # print(f"SIGNALS TABLE")
    # signals_print_table(all_records)

    db.close()
    return all_records


def signals_read_all_strategy_open_records(strategy):
    values = strategy,
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute("""SELECT rowid, * FROM signals
                      WHERE result = ''
                      AND strategy = ?""", values)
    db.commit()
    all_records = run_db.fetchall()

    # print(f"SIGNALS TABLE")
    # signals_print_table(all_records)

    db.close()
    return all_records


# Printing all records from the SIGNALS table
def signals_print_all_records():
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute("""SELECT rowid, * FROM signals""")
    db.commit()
    all_records = run_db.fetchall()

    print(f"SIGNALS TABLE")
    signals_print_table(all_records)

    db.close()


# Printing SIGNALS table records in a table format
def signals_print_table(records):

    print('-'*108)
    print('id   '
          'str  '
          'coin      '
          'signal  '
          'price       '
          'take prof   '
          'stop loss   '
          'result   '
          'signal time   '
          'result time   '
          'duration')
    print('-'*108)
    if records == []:
        print('No records')
    for item in records:

        # Calculating how long it took to execute the signal
        if item[9] != '':
            duration = f"{int((item[9] - item[8]) // 3600)}h " \
                       f"{int((item[9] - item[8]) % 3600 // 60)}m"
        else:
            duration = ''

        print(f"{item[0]}{' '*(5-len(str(item[0])))}"
              f"{item[1]}{' '*(5-len(str(item[1])))}"
              f"{item[2]}{' '*(10-len(str(item[2])))}"
              f"{item[3]}{' '*(8-len(str(item[3])))}"
              f"{item[4]}{' '*(12-len(str(item[4])))}"
              f"{item[5]}{' '*(12-len(str(item[5])))}"
              f"{item[6]}{' '*(12-len(str(item[6])))}"
              f"{item[7]}{' '*(9-len(str(item[7])))}"
              f"{convert_time(item[8])}{' '*(14-len(str(convert_time(item[8]))))}"
              f"{convert_time(item[9])}{' '*(14-len(str(convert_time(item[9]))))}"
              f'{duration}')
    print()


# Geting unfinished signals from the SIGNALS table
def signals_find_unfinished_records():
    try:
        db = sqlite3.connect('database.db')
        run_db = db.cursor()
        run_db.execute("""SELECT rowid, *
                          FROM signals 
                          WHERE result = ''""")
        records = run_db.fetchall()
        db.commit()
        db.close()
    except TypeError:
        records = False
    return records


# Getting the record we need from the SIGNALS table and update the result field
def signals_change_record_result(rowid, result, current_time):
    rowid = int(rowid)
    values = result, current_time, rowid
    db = sqlite3.connect('database.db')
    run_db = db.cursor()
    run_db.execute("""UPDATE signals 
                      SET result = ?,
                      result_time = ?   
                      WHERE rowid = ?""", values)
    db.commit()
    values = rowid,
    run_db.execute("""SELECT rowid, *
                      FROM signals 
                      WHERE rowid = ?""", values)
    # records = run_db.fetchall()
    db.commit()
    db.close()
    # signals_print_table(records)
