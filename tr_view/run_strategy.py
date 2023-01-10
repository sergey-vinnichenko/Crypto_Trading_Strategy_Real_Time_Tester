from time import time

from .get_tradingview_data import *
from .config import *
from .round_price import *
from .get_recomendations import *


__all__ = ['run_strategy']


def run_strategy(strategy_id, coin):

    # Getting strategy discriotion from the strategy_list
    strategy = strategy_list[strategy_id]

    # Create a variable in which we will collect the text of the report
    report = dict()

    # Write the name of the coin in the report
    report['coin'] = coin

    # Write the current time to the report
    report['time'] = time()

    # Write the name of the strategy in the report
    report['strategy'] = strategy_id

    # Adding a description of this strategy to the report
    report['strategy_doc'] = strategy['doc']

    # Adding a timeout
    report['timeout'] = strategy['timeout']

    # Adding a current price of the coin to the report
    report['price'] = test_coin(coin, '1m', 'close')
    report['price'] = round_price(report['price'])

    # Adding signal. If at least one of the criteria is not met,
    # remove this value and replace it with None
    report['signal'] = strategy['signal']

    # filling in take_profit and stop_loss prices
    report['take_profit'] = report['price'] * strategy['take_profit']
    report['take_profit'] = round_price(report['take_profit'])
    report['stop_loss'] = report['price'] * strategy['stop_loss']
    report['stop_loss'] = round_price(report['stop_loss'])

    # Creating a dictionary to record the results of the check
    report['criteria'] = dict()

    # Starting checking each criterion
    criteria_no = 0
    for criteria in strategy['criteria']:
        criteria_no += 1

        interval = strategy['criteria'][criteria]['interval']

        # Getting the first value of the comparison
        coin_1 = strategy['criteria'][criteria]['coin_1']
        if coin_1 is None:
            coin_1 = coin
        name_1 = strategy['criteria'][criteria]['name_1']

        # Sending a request through the tradingview_ta module
        value_1 = test_coin(coin_1, interval, name_1)

        # Rounding the first value
        value_1 = round_price(value_1)

        # Getting second  value of the comparison
        value_2 = strategy['criteria'][criteria]['value_2']
        coin_2 = strategy['criteria'][criteria]['coin_2']
        name_2 = strategy['criteria'][criteria]['name_2']
        if coin_2 is None:
            coin_2 = coin
        if name_2 is not None:

            # Sending a request through the tradingview_ta module
            value_2 = test_coin(coin_2, interval, name_2)

        # Rounding the second value
        value_2 = round_price(value_2)

        # Comparing two values and geting the result of the comparison
        operator = strategy['criteria'][criteria]['operator']
        coefficient = strategy['criteria'][criteria]['coefficient']
        if coefficient is None:
            calculation = f'{value_1} {operator} {value_2}'
        else:
            calculation = f'{value_1} {operator} ({value_2}*{coefficient})'

        # Converting text expression to real
        result = eval(calculation)

        # Composing a text description for the first value
        if coin_1 != coin:
            text_value_1 = f'{interval}: {coin_1} {name_1}'
        else:
            text_value_1 = f'{interval}: {name_1}'

        # Compose a text description for the second value
        if coin_2 != coin:
            text_value_2 = f'{coin_2} '
        else:
            text_value_2 = ''
        if coefficient is not None:
            if name_2 is not None:
                text_value_2 = text_value_2 + f'({name_2}*{coefficient})'
            else:
                text_value_2 = text_value_2 + f'({value_2}*{coefficient})'
        else:
            if name_2 is not None:
                text_value_2 = text_value_2 + name_2
            else:
                text_value_2 = text_value_2 + f'{value_2}'

        # Putting the two parts of the description together
        text = f'{text_value_1} {operator} {text_value_2}'

        # Recording all data in a report
        report['criteria'][criteria_no] = dict()
        report['criteria'][criteria_no]['text'] = text
        report['criteria'][criteria_no]['calculation'] = calculation
        report['criteria'][criteria_no]['result'] = result

        # If the criterion of our strategy is not met,
        # we remove the signal and replace it with None
        if result is False:
            report['signal'] = None

    # Receiving recommendations from tradingview_ta
    # and writing them into a report
    text_recommendations = recommendations(coin)

    # We write two different messages,
    # 1. if there is a signal and,
    # 2. if there is no singal
    if report['signal'] is not None:
        # Collecting the message
        # introductory part of the message
        message = f'#{coin}\n' \
                  f"#Strategy_{strategy_id}\n" \
                  f"Signal – {report['signal'].upper()}\n" \
                  f"Price – {report['price']} \n" \
                  f"Take profit – {report['take_profit']} \n" \
                  f"Stop loss – {report['stop_loss']} \n" \
                  f'\n' \
                  f"{strategy['doc']}\n"
    else:
        # Collecting the message
        # introductory part of the message
        message = f'#{coin}\n' \
                  f"#Strategy_{strategy_id}\n" \
                  f"Signal – {report['signal']}\n" \
                  f"Price – {report['price']} \n" \
                  f'\n' \
                  f"{strategy['doc']}\n"

    # Adding a description of our check
    for criteria_no in report['criteria']:
        message = f"{message}\nCriteria – {criteria_no}"
        message = f"{message}\n{report['criteria'][criteria_no]['text']}"
        message = f"{message}\n{report['criteria'][criteria_no]['calculation']}"
        message = f"{message}\n{report['criteria'][criteria_no]['result']}"

    # Adding recommendations at the end of the message
    message = f"{message}\n\n{text_recommendations}"

    # Adding the message to the report
    report['message'] = message

    # Removing the criteria section from the report, which we no longer need
    del report['criteria']

    return report
