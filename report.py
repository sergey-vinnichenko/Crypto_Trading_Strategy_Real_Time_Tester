from time import perf_counter

from signals import *
from tr_view import *


def strategy_report():
    time_start = perf_counter()

    # Getting all records from the SIGNALS table
    all_records_from_signal_table = signals_read_all_records()

    # Creating a new dictionary for future report
    strategy_report = dict()

    # Iterate over each signal from SIGNALS table
    for item in all_records_from_signal_table:
        strategy = item[1]

        # If such a strategy is not in strategy_report yet,
        # create a new strategy_report record
        if strategy not in strategy_report:

            # Create empty fields for all required parameters
            strategy_report[strategy] = {'signal': item[3],
                                         'profit': 0,
                                         'loss': 0,
                                         'open': 0,
                                         'count': 0,
                                         'av_time': list()}

        # Filling in the 'profit' field
        if item[7] == 'Profit':
            strategy_report[strategy]['profit'] += 1
            strategy_report[strategy]['av_time'].append(item[9] - item[8])

        # Filling in the 'loss' field
        elif item[7] == 'Loss':
            strategy_report[strategy]['loss'] += 1
            strategy_report[strategy]['av_time'].append(item[9] - item[8])

        # Filling in the 'open' field
        elif item[7] == '':
            strategy_report[strategy]['open'] += 1

        # Counting the number of signals belonging to this strategy
        strategy_report[strategy]['count'] += 1

    print(Style.BRIGHT +
          Fore.BLUE +
          'STRATEGY REPORT' +
          Fore.BLACK +
          Style.NORMAL)

    for strategy in strategy_report:
        print('1', strategy_report[strategy]['av_time'])

        if strategy_report[strategy]['av_time'] == []:
            strategy_report[strategy]['av_time'] = 0
        else:
            strategy_report[strategy]['av_time'] =   \
                sum(strategy_report[strategy]['av_time'])/   \
                len(strategy_report[strategy]['av_time'])
            strategy_report[strategy]['av_time'] = \
                int(strategy_report[strategy]['av_time'])
        print('2', strategy_report[strategy]['av_time'])

        # Sorting strategy_report dictionary
    sorted_strategy_report = dict(sorted(strategy_report.items()))

    # Compiling a report based on a strategy_report dictionary
    for strategy in sorted_strategy_report:

        # Getting all the variables that are needed for the report
        signal = strategy_report[strategy]['signal']
        doc = strategy_list[strategy]['doc']
        profit = strategy_report[strategy]['profit']
        loss = strategy_report[strategy]['loss']
        open = strategy_report[strategy]['open']
        count = strategy_report[strategy]['count']
        finished = profit + loss
        av_time = strategy_report[strategy]['av_time']

        # Calculating the percentage for profitable and
        # unprofitable closed positions
        if (profit + loss) != 0:
            success = int(round(profit / (profit + loss), 2) * 100)
            failure = int(round(loss / (profit + loss), 2) * 100)
        else:
            success = 0
            failure = 0

        # Making easy to read time format for duration
        av_time = f"{int(av_time // 3600)} hours {int(av_time % 3600 // 60)} min"

        # Printing report
        print('-' * 100)
        print(Style.BRIGHT +
              Fore.BLUE +
              f'Strategy {strategy}, {signal}' +
              Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX +
              f"{success}%({profit}) Profit, " +
              f"{failure}%({loss}) Loss" +
              Style.RESET_ALL)
        print(Fore.CYAN +
              doc +
              Style.RESET_ALL)
        print(f"{open} Open, "
              f"{finished} Finished, "
              f"{count} Total")
        print(f'{av_time} Average Time')

        # Getting all open signals for this strategy from the database
        signals = signals_read_all_strategy_open_records(strategy)

        # Printing a subtitle for the list of open signals
        print()
        if signals:
            print(Fore.BLUE +
                  'Open Signals' +
                  Style.RESET_ALL)
        else:
            print(Fore.CYAN +
                  'No open signals' +
                  Style.RESET_ALL)

        progress_sum = list()
        n = 0

        for record in signals:

            rowid = record[0]
            coin = record[2]
            signal = record[3]
            enter_price = record[4]
            take_profit = record[5]
            stop_loss = record[6]
            current_time_ = round(time(), 0)

            # Create an exception in case the
            # connection to the server fails
            try:
                n += 1

                # Making easy to read time format for duration
                # from the position opening moment

                # Calculating the number of hours
                duration = (current_time_ - record[8]) // 3600

                # If hours = 0, then write only minutes
                if duration == 0:
                    duration = f"{int((current_time_ - record[8]) % 3600 // 60)}m"
                else:
                    duration = f"{int((current_time_ - record[8]) // 3600)}h " \
                               f"{int((current_time_ - record[8]) % 3600 // 60)}m"

                result = None
                progress = 0

                current_price = test_coin(coin, '1m', 'close')

                # Looking for a finished signals
                if signal == 'buy' and current_price > take_profit:
                    result = 'Profit'
                elif signal == 'buy' and current_price < stop_loss:
                    result = 'Loss'
                elif signal == 'sell' and current_price < take_profit:
                    result = 'Profit'
                elif signal == 'sell' and current_price > stop_loss:
                    result = 'Loss'

                # Calculating progress for each signal
                elif signal == 'buy' and current_price > enter_price:
                    progress = int((current_price - enter_price)
                                   / (take_profit - enter_price) * 100)
                elif signal == 'buy' and current_price < enter_price:
                    progress = -int((enter_price - current_price)
                                    / (enter_price - stop_loss) * 100)
                elif signal == 'sell' and current_price < enter_price:
                    progress = int((enter_price - current_price)
                                   / (enter_price - take_profit) * 100)
                elif signal == 'sell' and current_price > enter_price:
                    progress = -int((current_price - enter_price)
                                    / (stop_loss - enter_price) * 100)
                else:
                    progress = 0

                # Adding progress to a progress_sum list to calculate
                # average progress all open signals for each strategy
                progress_sum.append(progress)

                if progress == 0:
                    text_progress = '–'
                elif progress > 0:
                    text_progress = f'+{str(progress)}%'
                else:
                    text_progress = f'{str(progress)}%'

                # Print signal state
                if progress is not None:
                    print(f"{coin}{' ' * (12 - len(coin))}"
                          f"{text_progress}{' ' * (9 - len(text_progress))}"
                          f"{current_price}{' ' * (10 - len(str(current_price)))}"
                          f"{duration}{' ' * (9 - len(duration))}" +
                          Fore.LIGHTCYAN_EX +
                          f" cp {current_price}{' '* (10 -len(str(current_price)))}"
                          f" ep {enter_price}{' '* (10 -len(str(enter_price)))}"
                          f" tp {take_profit}{' '* (10 -len(str(take_profit)))}"
                          f" sl {stop_loss}{' '* (10 -len(str(stop_loss)))}" +
                          Style.RESET_ALL)

                if result is not None:
                    signals_change_record_result(rowid, result, current_time_)

            except:
                print(Fore.RED + coin + ' Error' + Style.RESET_ALL)

        if progress_sum:
            print(Fore.CYAN +
                  f'Average progress {int(sum(progress_sum) / len(progress_sum))}%' +
                  Style.RESET_ALL)

        print()

    # Calculate time spent
    time_finish = perf_counter()
    time_summary = round(time_finish - time_start, 1)
    print(Fore.LIGHTGREEN_EX +
          f"Strategy is finished. Time spend {time_summary} sec." +
          Style.RESET_ALL)
