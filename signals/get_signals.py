from time import time as current_time
from colorama import Style, Fore

from .stop_list_db import *
from .signals_db import *


# Checking if this signal is in the stop list table
def test_signal(report):

    # Retrieving all data from a report
    strategy = report['strategy']
    coin = report['coin']
    signal = report['signal']
    timeout = report['timeout']
    price = report['price']
    take_profit = report['take_profit']
    stop_loss = report['stop_loss']
    strategy_doc = report['strategy_doc']
    result = ''
    result_time = ''
    message = report['message']
    time = int(report['time'])

    # Performing a database search
    find_record = stop_list_find_record_time(strategy, coin)

    # If such a signal occurs for the first time,
    # then we make a new record in the STOP_LIST table
    if find_record is False:

        # Making a new record in the SIGNAL table
        signals_add_record(strategy,
                           coin,
                           signal,
                           price,
                           take_profit,
                           stop_loss,
                           result,
                           time,
                           result_time,
                           strategy_doc)

        # Making a new record in the STOP LIST table
        stop_list_add_record(strategy, coin, time)

        return True

    # Checking if timeout time has passed
    elif (find_record+(timeout * 3600)) < current_time():

        # Making a new record in the SIGNAL table
        signals_add_record(strategy,
                           coin,
                           signal,
                           price,
                           take_profit,
                           stop_loss,
                           result,
                           time,
                           result_time,
                           strategy_doc)

        return True

    # If timeout time has not passed
    else:

        stop_list_change_record_time(strategy, coin, current_time())
        print(Fore.LIGHTMAGENTA_EX +
              f"Duplicate signal. Signal message not sent" +
              Fore.BLACK)
        return False
