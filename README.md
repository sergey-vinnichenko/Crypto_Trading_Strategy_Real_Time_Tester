# Crypto Trading Strategy Real Time Tester #

## How To Run This Program ##
1. Instal Tradingview_TA module 
```python
pip install tradingview-ta
```
2. Instal Colorama module
```python
pip install colorama
```
3. Create telegram bot
- Go to BotFather
- Create a new Bot
- Copy Bot Token
4. Get telegram chat id
- Go to 'messages' folder
- Open chat_id_bot.py file
- Fill in new bot token here
```python
API_TOKEN = 'ххххх'
```
- Go to Telegram and write /start command to your new bot. Or add your bot to any telegram groups and write /start command there.
- Bot will send your current chat id. Copy this chat id to clipboard.
5. Put telegram chat id
- Go to 'tr_view' folder
- Open 'config.py' file
- Set telegram chat id to all strategies  
```python
'chat_id': 'ххххххх',
```
7. Run entry point point scanner
Run 'main.py' file
8. Strategy result analyser
Run 'run_report.py' file in main folder
## What Is The Main Function Of This Program ##
The task of this program was to check whether it is possible to create a trading strategy based on technical analysis that will give more profit than losses. For these purposes, everything necessary was created so that you can write any strategies based on multiple criteria. Then, if these criteria are met, create a virtual deal. Then track whether this trade reached its take profit or was closed by stop loss. And then analyse how many trades within each strategy gave a positive result, and how many trades gave a negative result. And also calculate the average duration of trades in each strategy.
## How to Build a Strategy List ##
The description of the strategies is contained in a 'config.py' file in the 'tr_view' folder. Here is a quote from that file with my comments. We can put in this file as many strategies as we want.
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
The scanning progress is displayed in the console as follows. The program starts with the last strategy and goes from the first coin in the list to the next one. And so it goes until she sorts out all the strategies and all the coins. After that, it pauses and begins the next cycle.
```
19:51:31. CYCLE 1. STRATEGY 57
---------------------------------------------------------
1W BTC Stoch.RSI more then 70
1W Stoch.RSI more then 70
3d Stoch.RSI more then 70
1d RSI more then 70
4h RSI more then 70
1h RSI more then 70
TP-15%, SL-15%
1INCHUSDT
AAVEUSDT
ADAUSDT
ALGOUSDT
ALICEUSDT
ALPHAUSDT
ANKRUSDT
ANTUSDT
APEUSDT
```
## Tradingview_ta Module
The whole project is built around Tradingview_ta module for Python. Here is an example of an 15 minutes time frame report for BNB coin. Based on this report, we can understand what kind of data is available to us with the help of this module. 
```python
{'exchange': 'BINANCE',
 'indicators': {'ADX': 12.86109451,
                'ADX+DI': 19.43210953,
                'ADX+DI[1]': 20.09220387,
                'ADX-DI': 17.3496121,
                'ADX-DI[1]': 17.93896556,
                'AO': 0.27764706,
                'AO[1]': 0.10764706,
                'AO[2]': -0.04617647,
                'BB.lower': 274.65994681,
                'BB.upper': 276.07005319,
                'BBPower': 0.86234504,
                'CCI20': 114.58333333,
                'CCI20[1]': 126.89705613,
                'EMA10': 275.41272414,
                'EMA100': 275.05131127,
                'EMA20': 275.29961131,
                'EMA200': 273.46362055,
                'EMA30': 275.22465874,
                'EMA5': 275.55900599,
                'EMA50': 275.15465737,
                'HullMA9': 275.71962963,
                'Ichimoku.BLine': 275.05,
                'MACD.macd': 0.12946541,
                'MACD.signal': 0.08080791,
                'Mom': 0.5,
                'Mom[1]': 0,
                'P.SAR': 274.830528,
                'Pivot.M.Camarilla.Middle': 275.8,
                'Pivot.M.Camarilla.R1': 273.71833333,
                'Pivot.M.Camarilla.R2': 274.83666667,
                'Pivot.M.Camarilla.R3': 275.955,
                'Pivot.M.Camarilla.S1': 271.48166667,
                'Pivot.M.Camarilla.S2': 270.36333333,
                'Pivot.M.Camarilla.S3': 269.245,
                'Pivot.M.Classic.Middle': 275.8,
                'Pivot.M.Classic.R1': 280.3,
                'Pivot.M.Classic.R2': 288,
                'Pivot.M.Classic.R3': 300.2,
                'Pivot.M.Classic.S1': 268.1,
                'Pivot.M.Classic.S2': 263.6,
                'Pivot.M.Classic.S3': 251.4,
                'Pivot.M.Demark.Middle': 274.675,
                'Pivot.M.Demark.R1': 278.05,
                'Pivot.M.Demark.S1': 265.85,
                'Pivot.M.Fibonacci.Middle': 275.8,
                'Pivot.M.Fibonacci.R1': 280.4604,
                'Pivot.M.Fibonacci.R2': 283.3396,
                'Pivot.M.Fibonacci.R3': 288,
                'Pivot.M.Fibonacci.S1': 271.1396,
                'Pivot.M.Fibonacci.S2': 268.2604,
                'Pivot.M.Fibonacci.S3': 263.6,
                'Pivot.M.Woodie.Middle': 275,
                'Pivot.M.Woodie.R1': 278.7,
                'Pivot.M.Woodie.R2': 287.2,
                'Pivot.M.Woodie.R3': 290.9,
                'Pivot.M.Woodie.S1': 266.5,
                'Pivot.M.Woodie.S2': 262.8,
                'Pivot.M.Woodie.S3': 254.3,
                'RSI': 56.99646012,
                'RSI[1]': 54.27482214,
                'Rec.BBPower': 0,
                'Rec.HullMA9': 1,
                'Rec.Ichimoku': 0,
                'Rec.Stoch.RSI': 0,
                'Rec.UO': 0,
                'Rec.VWMA': 1,
                'Rec.WR': 0,
                'Recommend.All': 0.51212121,
                'Recommend.MA': 0.93333333,
                'Recommend.Other': 0.09090909,
                'SMA10': 275.24,
                'SMA100': 274.804,
                'SMA20': 275.365,
                'SMA200': 275.437,
                'SMA30': 275.09,
                'SMA5': 275.48,
                'SMA50': 275.14,
                'Stoch.D': 55.95852867,
                'Stoch.D[1]': 51.79077128,
                'Stoch.K': 63.07798482,
                'Stoch.K[1]': 52.62368816,
                'Stoch.RSI.K': 81.92709541,
                'UO': 55.0922717,
                'VWMA': 275.3768523,
                'W.R': -23.80952381,
                'change': 0.10885341,
                'close': 275.9,
                'high': 276,
                'low': 275.6,
                'open': 275.7,
                'volume': 344.788},
 'interval': '15m',
 'moving_averages': {'BUY': 14,
                     'COMPUTE': {'EMA10': 'BUY',
                                 'EMA100': 'BUY',
                                 'EMA20': 'BUY',
                                 'EMA200': 'BUY',
                                 'EMA30': 'BUY',
                                 'EMA50': 'BUY',
                                 'HullMA': 'BUY',
                                 'Ichimoku': 'NEUTRAL',
                                 'SMA10': 'BUY',
                                 'SMA100': 'BUY',
                                 'SMA20': 'BUY',
                                 'SMA200': 'BUY',
                                 'SMA30': 'BUY',
                                 'SMA50': 'BUY',
                                 'VWMA': 'BUY'},
                     'NEUTRAL': 1,
                     'RECOMMENDATION': 'STRONG_BUY',
                     'SELL': 0},
 'oscillators': {'BUY': 2,
                 'COMPUTE': {'ADX': 'NEUTRAL',
                             'AO': 'NEUTRAL',
                             'BBP': 'NEUTRAL',
                             'CCI': 'SELL',
                             'MACD': 'BUY',
                             'Mom': 'BUY',
                             'RSI': 'NEUTRAL',
                             'STOCH.K': 'NEUTRAL',
                             'Stoch.RSI': 'NEUTRAL',
                             'UO': 'NEUTRAL',
                             'W%R': 'NEUTRAL'},
                 'NEUTRAL': 8,
                 'RECOMMENDATION': 'NEUTRAL',
                 'SELL': 1},
 'screener': 'crypto',
 'summary': {'BUY': 16,
             'NEUTRAL': 9,
             'RECOMMENDATION': 'STRONG_BUY',
             'SELL': 1},
 'symbol': 'BNBUSDT',
 'time': datetime.datetime(2023, 1, 10, 19, 48, 56, 429329)}
```
## Telegram Messages ##
Here is an example of a message that comes to Telegram if the search for matches brings a positive result.
```
#GRTUSDT
#Strategy_56
Signal – SELL
Price – 0.07 
Take profit – 0.0595 
Stop loss – 0.0805 

1W Stoch.RSI more then 70
3d Stoch.RSI more then 70
1d RSI more then 70
4h RSI more then 70
1h RSI more then 70
TP-15%, SL-15%

Criteria – 1
1W: Stoch.RSI.K > 70
79.39 > 70
True
Criteria – 2
3d: Stoch.RSI.K > 70
100 > 70
True
Criteria – 3
1d: RSI > 70
70.041 > 70
True
Criteria – 4
4h: RSI > 70
73.101 > 70
True
Criteria – 5
1h: RSI > 70
70.415 > 70
True

MAs
1W – SELL
1d – BUY
4h – STRONG_BUY
1h – STRONG_BUY
30m – STRONG_BUY
15m – STRONG_BUY
5m – STRONG_BUY

Indicators
1W – NEUTRAL
1d – NEUTRAL
4h – NEUTRAL
1h – BUY
30m – BUY
15m – NEUTRAL
5m – SELL
```
## Tradingview_TA Recommendations ##
```
 'interval': '15m',
 'moving_averages': {'BUY': 14,
                     'COMPUTE': {'EMA10': 'BUY',
                                 'EMA100': 'BUY',
                                 'EMA20': 'BUY',
                                 'EMA200': 'BUY',
                                 'EMA30': 'BUY',
                                 'EMA50': 'BUY',
                                 'HullMA': 'BUY',
                                 'Ichimoku': 'NEUTRAL',
                                 'SMA10': 'BUY',
                                 'SMA100': 'BUY',
                                 'SMA20': 'BUY',
                                 'SMA200': 'BUY',
                                 'SMA30': 'BUY',
                                 'SMA50': 'BUY',
                                 'VWMA': 'BUY'},
                     'NEUTRAL': 1,
                     'RECOMMENDATION': 'STRONG_BUY',
                     'SELL': 0},
 'oscillators': {'BUY': 2,
                 'COMPUTE': {'ADX': 'NEUTRAL',
                             'AO': 'NEUTRAL',
                             'BBP': 'NEUTRAL',
                             'CCI': 'NEUTRAL',
                             'MACD': 'BUY',
                             'Mom': 'BUY',
                             'RSI': 'NEUTRAL',
                             'STOCH.K': 'NEUTRAL',
                             'Stoch.RSI': 'NEUTRAL',
                             'UO': 'NEUTRAL',
                             'W%R': 'NEUTRAL'},
                 'NEUTRAL': 9,
                 'RECOMMENDATION': 'BUY',
                 'SELL': 0},
 'screener': 'crypto',
 'summary': {'BUY': 16,
             'NEUTRAL': 10,
             'RECOMMENDATION': 'STRONG_BUY',
             'SELL': 0},
```
## Strategy Reports ##

Here is an example of the report I ended up with for each strategy. In this strategy, I have 23 finished trails. Moreover, all 23 turned out to be unprofitable and met their stop loss. As well as 2 open positions that are already close to being also closed by stop loss.

![](https://drive.google.com/uc?export=download&id=1mJ-PW8GFQJeL2KZL1rdTnYfdOmljr1TB)

## Conclusion ##

I tested more than 50 strategies and in general did not come up with a positive result, because basically all strategies gave more losses than wins.

I also came to the conclusion that I have to build my strategies around 1 day, 3 days and 1 week frames using RSI and Stoch RSI indicators. But in order to test the effectiveness of such strategies, a lot of time is needed.
