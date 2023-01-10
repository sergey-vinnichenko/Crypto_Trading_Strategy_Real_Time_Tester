from .get_tradingview_data import *
from .config import *

__all__ = ['recommendations']

# Creating recomendations message
def recommendations(coin):

    message_ma = ''
    message_os = ''
    for interval in intervals:
        test_ma = coin_ma_rec(coin, interval)
        test_os = coin_os_rec(coin, interval)
        message_ma = f'{message_ma}\n{interval} – {test_ma}'
        message_os = f'{message_os}\n{interval} – {test_os}'
    message = f'MAs{message_ma}\n\nIndicators{message_os}'

    return message
