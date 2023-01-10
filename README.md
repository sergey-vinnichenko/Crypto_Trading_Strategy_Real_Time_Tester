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
## Tradingview_TA Module
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
## Strategy Reports ##

```
Strategy 56, sell
0%(0) Profit, 0%(0) Loss
1W Stoch.RSI  more then 70
3d Stoch.RSI  more then 70
1d RSI  more then 70
4h RSI  more then 70
1h RSI б more then 70
TP-15%, SL-15%
18 Open, 0 Finished, 18 Total
0 hours 0 min Average Time

Open Signals
OCEANUSDT   -21%     0.2089    68h 37m   cp 0.2089     ep 0.2024     tp 0.17204    sl 0.23276   
XMRUSDT     -4%      159.2     62h 27m   cp 159.2      ep 158.2      tp 134.47     sl 181.93    
OCEANUSDT   +9%      0.2089    54h 48m   cp 0.2089     ep 0.2119     tp 0.18011    sl 0.24368   
OCEANUSDT   +13%     0.2089    54h 19m   cp 0.2089     ep 0.2132     tp 0.18122    sl 0.24518   
OCEANUSDT   +64%     0.2089    46h 31m   cp 0.2089     ep 0.2312     tp 0.19652    sl 0.26588   
APEUSDT     -76%     4.871     45h 59m   cp 4.871      ep 4.371      tp 3.7154     sl 5.0267    
LDOUSDT     +9%      1.955     42h 41m   cp 1.955      ep 1.984      tp 1.6864     sl 2.2816    
OPUSDT      -4%      1.265     42h 39m   cp 1.265      ep 1.256      tp 1.0676     sl 1.4444    
WOOUSDT     –        0.1826    42h 36m   cp 0.1826     ep 0.1539     tp 0.13082    sl 0.17699   
LTCUSDT     –        80.94     41h 44m   cp 80.94      ep 81.04      tp 68.884     sl 93.196    
FTMUSDT     +12%     0.2426    40h 49m   cp 0.2426     ep 0.2474     tp 0.21029    sl 0.28451   
GRTUSDT     -3%      0.0704    40h 49m   cp 0.0704     ep 0.07       tp 0.0595     sl 0.0805    
OCEANUSDT   +67%     0.2089    37h 59m   cp 0.2089     ep 0.2326     tp 0.19771    sl 0.26749   
FTMUSDT     +12%     0.2426    33h 44m   cp 0.2426     ep 0.2472     tp 0.21012    sl 0.28428   
FTMUSDT     +16%     0.2426    33h 16m   cp 0.2426     ep 0.2489     tp 0.21157    sl 0.28624   
FTMUSDT     +14%     0.2426    32h 45m   cp 0.2426     ep 0.248      tp 0.2108     sl 0.2852    
DASHUSDT    +25%     48.39     32h 6m    cp 48.39      ep 50.29      tp 42.746     sl 57.833    
FTMUSDT     +15%     0.2426    32h 4m    cp 0.2426     ep 0.2485     tp 0.21122    sl 0.28578   
Average progress 8%
```

## Conclusion ##

