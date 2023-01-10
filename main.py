from time import sleep, perf_counter
from colorama import Style, Fore

from tr_view import *
from messages import *
from signals import *
from mytime import *

# This file starts checking cryptocurrencies for compliance with our strategies,
# which will be repeated in a circle

n = 0
# The number of repetitions
n_max = 300

while n < n_max:
    n += 1

    # We start testing strategies one by one
    for strategy_id in strategy_list:
        if strategy_list[strategy_id]['coins'] is not None:

            # Remembering the start time of the strategy execution
            time_start = perf_counter()

            print()
            print(Style.BRIGHT +
                  Fore.BLUE +
                  f"{time_now_hms()}. CYCLE {n}. STRATEGY {strategy_id}" +
                  Fore.BLACK +
                  Style.NORMAL)
            print('-' * 57)
            print(Fore.LIGHTCYAN_EX +
                  strategy_list[strategy_id]['doc'] +
                  Fore.BLACK)

            chat_id = strategy_list[strategy_id]['chat_id']

            # Getting a list of coins for the particular strategy
            coins = strategy_coin_list(strategy_id)

            # Checking each coin
            for coin in coins:
                print(coin)

                # Creating an exception in case we
                # do not receive a response from the server
                try:

                    # Creating a report for each coin
                    report = run_strategy(strategy_id, coin)

                    # Checking if there is a signal in the report
                    if report['signal'] is not None:

                        # Checking if the report is duplicate
                        if test_signal(report):

                            # Sending a message via Telegram
                            if chat_id is not None:
                                tg_message(chat_id, report['message'])
                                print(Fore.LIGHTMAGENTA_EX +
                                      f"Send signal message." +
                                      Fore.BLACK)

                except:
                    print(Fore.RED +
                          'Error' +
                          Fore.BLACK)

            # Calculate spent time
            time_finish = perf_counter()
            time_summary = round(time_finish - time_start, 1)
            print(Fore.LIGHTGREEN_EX +
                  f"Strategy is finished. Time spend {time_summary} sec." +
                  Fore.BLACK)

    # Delay between cycles
    sleep(60)

print('Program is finished')
