from tradingview_ta import TA_Handler

__all__ = ['test_coin', 'coin_ma_rec', 'coin_os_rec']

# This file contains functions for working
# with the trailingview module and getting
# data from the tradingview.

def coin_dict(coin_, interval_):
    return TA_Handler(
        symbol=coin_,
        screener="crypto",
        exchange="BINANCE",
        interval=interval_
        ).get_analysis().__dict__


def test_coin(coin_, interval_, indicator_):
    # print(coin_, interval_, indicator_)
    return TA_Handler(
        symbol=coin_,
        screener="crypto",
        exchange="BINANCE",
        interval=interval_
        ).get_analysis().indicators[indicator_]

def coin_ma_rec(coin_, interval_):
    return TA_Handler(
        symbol=coin_,
        screener="crypto",
        exchange="BINANCE",
        interval=interval_
        ).get_analysis().moving_averages['RECOMMENDATION']

def coin_os_rec(coin_, interval_):
    return TA_Handler(
        symbol=coin_,
        screener="crypto",
        exchange="BINANCE",
        interval=interval_
        ).get_analysis().oscillators['RECOMMENDATION']


