# Crypto Trading Strategy Real Time Tester #

## How To Run This Program ##
1. Instal Tradingview_TA module 
2. Instal Colorama module
3. Create telegram bot
4. Get telegram chat id
5. Put telegram chat id
6. Run entry point point scanner
7. Strategy result analyser
## What Is The Main Function ##
## How to Build a Strategy List ##
```python
strategy_list = {

    # Strategy ID. We can write any number of strategies
    57: {

        # Stratedy description
        'doc': '1W BTC Stoch.RSI more then 70\n'
               '1W Stoch.RSI more then 70\n'
               '3d Stoch.RSI more then 70\n'
               '1d RSI more then 70\n'
               '4h RSI more then 70\n'
               '1h RSI more then 70\n'
               'TP-15%, SL-15%',

        # List of coins
        # It could be like this ['BTCUSDT']
        # or ['BTCUSDT', 'ETHUSDT']]
        'coins': 2,

        # Telegram chat id
        'chat_id': 'ххх',

        # Timeout in hours for each strategy
        'timeout': 6,

        # Criteria. We can write any number of criteria
        'criteria': {
            1: {
                # Main intervals are 1m, 5m, 15m, 30m, 1h, 6h, 12h,
                # 1d, 2d, 1W, !M
                'interval': '1W',

                # We can use another coin as one of the criteria
                'coin_1': None,

                # All the names should be taken from the Tradingview_ta module
                'name_1': 'Stoch.RSI.K',
                'operator': '>',

                # We can write particular value
                'value_2': 70,

                # We can write another coin for second value
                'coin_2': None,

                # We van use some indicator name
                'name_2': None,

                # We can use some coefficient to compare first and second value
                'coefficient': None
            },
            2: {
                'interval': '3d',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 70,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 70,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            4: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 70,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },

        # Signal type
        'signal': 'sell',

        # Take_profit persentage
        'take_profit': 0.85,

        # Stop Loss persentage
        'stop_loss': 1.15
    }, 
```
## Scan Process ##
## Telegram Messages ##
## Tradingview_TA Recommendations ##
## Strategy Reports ##
## Conclusion ##

