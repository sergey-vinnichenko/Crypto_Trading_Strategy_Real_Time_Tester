from .config import *


# Get a list of coins for each strategy
def strategy_coin_list(strategy_id):
    strategy = strategy_list[strategy_id]

    if type(strategy['coins']) == int:
        return coin_lists[strategy['coins']]

    else:
        return strategy['coins']
