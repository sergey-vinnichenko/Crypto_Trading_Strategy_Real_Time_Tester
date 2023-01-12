# Main Tragingview intervals. Used for recomendations.
intervals = ['1W', '1d', '4h', '1h', '30m', '15m', '5m']

coin_lists = {

    # Most important coins. Short list
    1: ['BTCUSDT', 'ETHUSDT', 'BNBUSDT',
        'EGLDUSDT', 'NEARUSDT', 'SOLUSDT',
        'DOGEUSDT', 'LUNCUSDT'],

    # All Binance Futures. Large list
    2: ['1INCHUSDT',
        'AAVEUSDT', 'ADAUSDT', 'ALGOUSDT', 'ALICEUSDT', 'ALPHAUSDT', 'ANKRUSDT',
        'ANTUSDT', 'APEUSDT', 'API3USDT', 'APTUSDT', 'ARPAUSDT', 'ARUSDT',
        'ATAUSDT', 'ATOMUSDT', 'AUDIOUSDT', 'AVAXUSDT', 'AXSUSDT',
        'BAKEUSDT', 'BALUSDT', 'BANDUSDT', 'BATUSDT', 'BCHUSDT', 'BELUSDT',
        'BLUEBIRDUSDT', 'BLZUSDT', 'BNBUSDT', 'BNXUSDT', 'BTCDOMUSDT',
        'BTCUSDT', 'BTCUSDT',
        'C98USDT', 'CELOUSDT', 'CELRUSDT', 'CHRUSDT', 'CHZUSDT', 'COMPUSDT',
        'COTIUSDT', 'CRVUSDT', 'CTKUSDT', 'CTSIUSDT', 'CVXUSDT',
        'DARUSDT', 'DASHUSDT', 'DEFIUSDT', 'DENTUSDT', 'DGBUSDT', 'DOGEUSDT',
        'DOTUSDT', 'DUSKUSDT', 'DYDXUSDT',
        'EGLDUSDT', 'ENJUSDT', 'ENSUSDT', 'EOSUSDT', 'ETCUSDT', 'ETHUSDT',
        'ETHUSDT',
        'FILUSDT', 'FLMUSDT', 'FLOWUSDT', 'FOOTBALLUSDT', 'FTMUSDT',
        'GALAUSDT', 'GALUSDT', 'GMTUSDT', 'GRTUSDT', 'GTCUSDT',
        'HBARUSDT', 'HNTUSDT', 'HOTUSDT',
        'ICPUSDT', 'ICXUSDT', 'IMXUSDT', 'INJUSDT',
        'IOSTUSDT', 'IOTAUSDT', 'IOTXUSDT',
        'JASMYUSDT',
        'KAVAUSDT', 'KLAYUSDT', 'KNCUSDT', 'KSMUSDT',
        'LDOUSDT', 'LINAUSDT', 'LINKUSDT', 'LITUSDT', 'LPTUSDT', 'LRCUSDT',
        'LTCUSDT', 'LUNCUSDT', 'LUNA2USDT',
        'MANAUSDT', 'MASKUSDT', 'MATICUSDT', 'MKRUSDT', 'MTLUSDT',
        'NEARUSDT', 'NEOUSDT', 'NKNUSDT',
        'OCEANUSDT', 'OGNUSDT', 'OMGUSDT', 'ONEUSDT', 'ONTUSDT', 'OPUSDT',
        'PEOPLEUSDT',
        'QNTUSDT', 'QTUMUSDT',
        'REEFUSDT', 'RENUSDT', 'RLCUSDT', 'ROSEUSDT', 'RSRUSDT', 'RUNEUSDT',
        'RVNUSDT',
        'SANDUSDT', 'SHIBUSDT', 'SFPUSDT', 'SKLUSDT', 'SNXUSDT', 'SOLUSDT',
        'SPELLUSDT', 'STGUSDT', 'STMXUSDT', 'STORJUSDT', 'SUSHIUSDT',
        'SXPUSDT',
        'THETAUSDT', 'TOMOUSDT', 'TRBUSDT', 'TRXUSDT',
        'UNFIUSDT', 'UNIUSDT',
        'VETUSDT',
        'WAVESUSDT', 'WOOUSDT',
        'XECUSDT', 'XEMUSDT', 'XLMUSDT', 'XMRUSDT', 'XRPUSDT', 'XTZUSDT',
        'YFIUSDT',
        'ZECUSDT', 'ZENUSDT', 'ZILUSDT', 'ZRXUSDT'],

    # Selected coing. Middle list
    3: ['ARUSDT', 'ATAUSDT', 'ATOMUSDT', 'AVAXUSDT',
        'BATUSDT', 'BLZUSDT', 'BNBUSDT',
        'COTIUSDT', 'DOGEUSDT', 'DYDXUSDT',
        'EGLDUSDT', 'ETCUSDT', 'ETHUSDT',
        'FLMUSDT', 'FLOWUSDT',
        'GALAUSDT',
        'HBARUSDT',
        'KLAYUSDT', 'KNCUSDT', 'KSMUSDT',
        'LINKUSDT', 'LTCUSDT', 'LUNCUSDT',
        'MKRUSDT',
        'NEARUSDT',
        'REEFUSDT', 'RLCUSDT', 'RUNEUSDT', 'RVNUSDT',
        'SHIBUSDT', 'SNXUSDT', 'SOLUSDT', 'STORJUSDT', 'SUSHIUSDT',
        'UNFIUSDT',
        'XRPUSDT'],

    # Selected coins. Middle list. Excluding LUNC
    4: ['ARUSDT', 'ATAUSDT', 'ATOMUSDT', 'AVAXUSDT',
        'BATUSDT', 'BLZUSDT', 'BNBUSDT',
        'COTIUSDT', 'DOGEUSDT', 'DYDXUSDT',
        'EGLDUSDT', 'ETCUSDT', 'ETHUSDT',
        'FLMUSDT', 'FLOWUSDT',
        'GALAUSDT',
        'HBARUSDT',
        'KLAYUSDT', 'KNCUSDT', 'KSMUSDT',
        'LINKUSDT', 'LTCUSDT',
        'MKRUSDT',
        'NEARUSDT',
        'REEFUSDT', 'RLCUSDT', 'RUNEUSDT', 'RVNUSDT',
        'SHIBUSDT', 'SNXUSDT', 'SOLUSDT', 'STORJUSDT', 'SUSHIUSDT',
        'UNFIUSDT',
        'XRPUSDT']
}

strategy_list = {

    # Strategy ID. We can write any number of strategies
    57: {

        # Stratedy description
        'doc': '1W BTC Stoch.RSI more than 70\n'
               '1W Stoch.RSI more than 70\n'
               '3d Stoch.RSI more than 70\n'
               '1d RSI more than 70\n'
               '4h RSI more than 70\n'
               '1h RSI more than 70\n'
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
            5: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 70,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            6: {
                'interval': '1W',
                'coin_1': 'BTCUSDT',
                'name_1': 'Stoch.RSI.K',
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
    },  # 1W, 3d Stoch RSI, 1d, 4h, 1h RSI + BTC (sell)

    56: {
        'doc': '1W Stoch.RSI more than 70\n'
               '3d Stoch.RSI more than 70\n'
               '1d RSI more than 70\n'
               '4h RSI more than 70\n'
               '1h RSI more than 70\n'
               'TP-15%, SL-15%',
        'coins': 2,
        'chat_id': '-801544985',
        'timeout': 6,
        'criteria': {
            1: {
                'interval': '1W',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 70,
                'coin_2': None,
                'name_2': None,
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
            5: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 70,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },

        },  # criteria
        'signal': 'sell',
        'take_profit': 0.85,
        'stop_loss': 1.15
    },  # 1W, 3d Stoch RSI, 1d, 4h, 1h RSI (sell)
    44: {
        'doc': '1d Stoch RSI less than 20\n'
               'TP-20%, SL-10%',
        'coins': 2,
        'chat_id': '-801544985',
        'timeout': 6,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '<',
                'value_2': 20,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.2,
        'stop_loss': 0.9
    },  # 1d Stoch.RSI less than 20 (buy)

    55: {
        'doc': '1d RSI more than  65, 4h Stoch RSI more than 93\n'
               'TP-15%, SL-30%',
        'coins': None,
        'chat_id': None,
        'timeout': 6,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 65,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 93,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.85,
        'stop_loss': 1.3
    },  # STOP – RLC (sell)
    54: {
        'doc': '1d RSI less than 35, 4h Stoch RSI less than 10\n'
               'TP-15%, SL-30%',
        'coins': None,
        'chat_id': None,
        'timeout': 6,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 35,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '<',
                'value_2': 7,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.15,
        'stop_loss': 0.7
    },  # STOP – RLC (buy)
    53: {
        'doc': '3d, 1d, 1h Stoch RSI more than 93\n'
               'TP-14%, SL-7%',
        'coins': None,
        'chat_id': None,
        'timeout': 12,
        'criteria': {
            1: {
                'interval': '3d',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 93,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 93,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 93,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.86,
        'stop_loss': 1.07
    },  # STOP – 1d, 1h Stoch RSI more than 93 (sell)
    52: {
        'doc': '1d, 1h Stoch RSI more than 93\n'
               'TP-14%, SL-7%',
        'coins': None,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 93,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 93,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.86,
        'stop_loss': 1.07
    },  # STOP – 1d, 1h Stoch RSI more than 93 (sell)
    49: {
        'doc': '1d, 4h Stoch RSI more than 93\n'
               'TP-14%, SL-7%',
        'coins': None,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 93,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 93,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.86,
        'stop_loss': 1.07
    },  # STOP – 1d, 4h Stoch RSI more than 93 (sell)
    48: {
        'doc': '1d, 4h, 1h Stoch RSI more than 90\n'
               'TP-14%, SL-7%',
        'coins': None,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 90,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 90,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 90,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.86,
        'stop_loss': 1.07
    },  # STOP – 1d, 4h, 1h Stoch RSI more than 90 (sell)
    47: {
        'doc': '1d Stoch RSI more than 93\n'
               'TP-20%, SL-10%',
        'coins': None,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 93,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.8,
        'stop_loss': 1.1
    },  # STOP – 1d Stoch.RSI more than 93 (sell)
    46: {
        'doc': '1w, 1d, 4h, 1h Stoch RSI more than 90\n'
               'TP-14%, SL-7%',
        'coins': None,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1W',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 90,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 90,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 90,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            4: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 90,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.86,
        'stop_loss': 1.07
    },  # STOP – 1w, 1d, 4h, 1h Stoch RSI more than 90 (sell)
    45: {
        'doc': '1d Stoch RSI more than 80\n'
               'TP-20%, SL-10%',
        'coins': None,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 80,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.8,
        'stop_loss': 1.1
    },  # STOP – 1d Stoch.RSI more than 80 (sell)
    42: {
        'doc': '1w, 1d, 4h, 1h Stoch RSI more than 78\n'
               'TP-14%, SL-7%',
        'coins': None,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1W',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 78,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 78,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 78,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            4: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '>',
                'value_2': 78,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.86,
        'stop_loss': 1.07
    },  # STOP – 1w, 1d, 4h, 1h Stoch RSI more than 78 (sell)
    41: {
        'doc': '4h RSI more than 80\n'
               'TP-20%, SL-10%',
        'coins': None,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 80,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.8,
        'stop_loss': 1.1
    },  # STOP – 4h RSI more than 80 (sell)
    37: {
        'doc': '5m MACD less than SIGNAL\n'
               '15m MACD less than SIGNAL\n'
               '30m MACD less than SIGNAL\n'
               '1h MACD less than SIGNAL\n'
               '4h MACD less than SIGNAL\n'
               '4h RSI less than 60\n'
               'TP-3%, SL-1,5%',
        'coins': None,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '5m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            2: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            3: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            4: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            5: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            6: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 60,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.97,
        'stop_loss': 1.015
    },  # STOP – MACD, 5m, 15m, 30m, 1h, 4h, 4h RSI more than 60 (sell)
    35: {
        'doc': '4h RSI more than 72\n'
               'TP-20%, SL-10%',
        'coins': None,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 72,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.8,
        'stop_loss': 1.1
    },  # STOP – 4h RSI more than 72 (sell)

}  # Final

archive_strategy_list = {
    53: {
        'doc': '1d, 1h Stoch RSI more than 7\n'
               'TP-14%, SL-7%',
        'coins': None,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '<',
                'value_2': 7,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '<',
                'value_2': 7,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 0.86,
        'stop_loss': 1.07
    },  # STOP – 1d, 4h Stoch RSI less than 7 (buy)
    51: {
        'doc': '1d, 4h Stoch RSI less than 7\n'
               'TP-14%, SL-7%',
        'coins': None,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '<',
                'value_2': 7,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '<',
                'value_2': 7,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 0.86,
        'stop_loss': 1.07
    },  # STOP – 1d, 4h Stoch RSI less than 7 (buy)
    50: {
        'doc': '1d, 4h, 1h Stoch RSI less than 10\n'
               'TP-14%, SL-7%',
        'coins': None,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '<',
                'value_2': 10,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '<',
                'value_2': 10,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'Stoch.RSI.K',
                'operator': '<',
                'value_2': 10,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 0.86,
        'stop_loss': 1.07
    },  # STOP – 1d, 4h, 1h Stoch RSI less than 10 (buy)
    38: {
        'doc': '5m MACD more than SIGNAL\n'
               '15m MACD more than SIGNAL\n'
               '30m MACD more than SIGNAL\n'
               '1h MACD more than SIGNAL\n'
               '4h MACD more than SIGNAL\n'
               '4h RSI less than 40\n'
               'TP-3%, SL-1,5%',
        'coins': None,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '5m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            2: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            3: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            4: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            5: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            6: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.03,
        'stop_loss': 0.985
    },  # STOP – MACD, 5m, 15m, 30m, 1h, 4h, 4h RSI less than 40 (buy)
    15: {
        'doc': '#good_strategy\n'
               '5m MACD less than SIGNAL\n'
               '15m RSI more than 70\n'
               'TP-1,5%, SL-0,75%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '5m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            2: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 70,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.985,
        'stop_loss': 1.0075
    },  # 5m MACD less than signal, 15m RSI more than 70 (sell) – STOP
    # 71%(5) Profit, 28%(2) Loss, 0 Open, 7 Finished, 7 Total
    # 1 hours 48 min Average Time

    43: {
        'doc': '1d RSI more than 80\n'
               'TP-20%, SL-10%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 80,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.8,
        'stop_loss': 1.1
    },  # 1d RSI more than 80 (sell) – STOP
    40: {
        'doc': '5m MACD more than SIGNAL\n'
               '15m MACD more than SIGNAL\n'
               '30m MACD more than SIGNAL\n'
               '1h MACD more than SIGNAL\n'
               '4h RSI меньше 40\n'
               'TP-1%, SL-0,5%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '5m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            2: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            3: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            4: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            5: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.01,
        'stop_loss': 0.995
    },  # Только MACD, 5m, 15m, 30m, 1h, TP-1%, SL-0,5% (buy)
    39: {
        'doc': '#good_strategy\n'
               '5m MACD меньше SIGNAL\n'
               '15m MACD меньше SIGNAL\n'
               '30m MACD меньше SIGNAL\n'
               '1h MACD меньше SIGNAL\n'
               '4h RSI more than 60\n'
               'TP-1%, SL-0,5%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '5m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            2: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            3: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            4: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            6: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 60,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.99,
        'stop_loss': 1.005
    },  # Только MACD, 5m, 15m, 30m, 1h, TP-1%, SL-0,5% (sell)
    # 32%(6) Profit, 68%(13) Loss, 2 Open, 19 Finished, 21 Total
    # 0 hours 21 min. Average Time

    36: {
        'doc': '4h RSI 40-50\n'
               'MACD up\n'
               'TP-5%, SL-2,5%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 50,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.05,
        'stop_loss': 0.975
    },  # 4h RSI 40-50, MACD растет (buy)
    # 0%(0) Profit, 100%(15) Loss, 11 Open, 15 Finished, 26 Total
    # 12 hours 42 min Average Time

    34: {
        'doc': '4h RSI меньше 17\n'
               'TP-20%, SL-10%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 20,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.2,
        'stop_loss': 0.9
    },  # 4h RSI less than 17 (buy) – STOP
    33: {
        'doc': '1d RSI more than 72\n'
               'TP-40%, SL-20%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 72,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.6,
        'stop_loss': 1.2
    },  # 1d RSI more than 72 (sell) – STOP
    32: {
        'doc': '1d RSI less than 17\n'
               'TP-40%, SL-20%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 20,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.4,
        'stop_loss': 0.8
    },  # 1d RSI less than 17 (buy) – STOP
    25: {
        'doc': 'RSI is on top\n'
               '1d RSI more than 72\n'
               '4h RSI more than 72\n'
               '1h RSI more than 72\n'
               '30m RSI more than 72\n'
               '15m RSI more than 72\n'
               'TP-10%, SL-5%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 72,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 72,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 72,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            4: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 72,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            5: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 72,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.90,
        'stop_loss': 1.05
    },  # RSI is on top, 15m – 1d (sell) – STOP
    24: {
        'doc': 'Все RSI on buttom\n'
               '1d RSI less than 28\n'
               '4h RSI less than 28\n'
               '1h RSI less than 28\n'
               '30m RSI less than 28\n'
               '15m RSI less than 28\n'
               'TP-10%, SL-5%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 28,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 28,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 28,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            4: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 28,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            5: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 28,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.10,
        'stop_loss': 0.95
    },  # Все RSI на дне, 15m – 1d (buy) – STOP
    31: {
        'doc': '1h MACD less than SIGNAL\n'
               '2h RSI more than 70\n'
               'TP-4%, SL-2%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            2: {
                'interval': '2h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 70,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.96,
        'stop_loss': 1.02
    },  # 1h MACD less than signal, 2h RSI more than 70 (sell)
    30: {
        'doc': '1h MACD more than SIGNAL\n'
               '2h RSI less than 70\n'
               'TP-4%, SL-2%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            2: {
                'interval': '2h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 24,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.04,
        'stop_loss': 0.98
    },  # 1h MACD more than signal, 2h RSI less than 70 (buy)
    29: {
        'doc': '30m MACD less than SIGNAL\n'
               '1h RSI more than 70\n'
               'TP-3%, SL-1,5%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            2: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 70,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.97,
        'stop_loss': 1.015
    },  # 30m MACD less than signal, 1h RSI more than 70 (sell)
    28: {
        'doc': '30m MACD more than SIGNAL\n'
               '1h RSI less than 70\n'
               'TP-3%, SL-1,5%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '5m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            2: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 24,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.03,
        'stop_loss': 0.985
    },  # 30m MACD more than signal, 1h RSI less than 70 (buy)
    27: {
        'doc': 'Четыре MACD + 1h RSI\n'
               '5m MACD more than SIGNAL\n'
               '15m MACD more than SIGNAL\n'
               '30m MACD more than SIGNAL\n'
               '1h MACD more than SIGNAL\n'
               '4h RSI less than 40\n'
               'TP-3%, SL-1,5%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '5m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            2: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            3: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            4: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            5: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.03,
        'stop_loss': 0.985
    },  # Только MACD, 5m, 15m, 30m, 1h (buy)
    26: {
        'doc': 'Только MACD\n'
               '5m MACD less than SIGNAL\n'
               '15m MACD less than SIGNAL\n'
               '30m MACD less than SIGNAL\n'
               '1h MACD less than SIGNAL\n'
               '4h RSI more than 60\n'
               'TP-3%, SL-1,5%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '5m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            2: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            3: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            4: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            6: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 60,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.97,
        'stop_loss': 1.015
    },  # Только MACD, 5m, 15m, 30m, 1h (sell)
    # 4%(1) Profit, 96%(22) Loss,
    # 0 Open, 23 Finished, 23 Total,
    # 8 hours 5 min. Average Time

    21: {
        'doc': 'Только RSI 1h\n'
               '1h RSI more than 80\n'
               '1d MACD less than SIGNAL\n'
               'TP-3%, SL-1,5%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 80,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.97,
        'stop_loss': 1.015
    },  # 1h RSI + 1d MACD (sell)
    # 0%(0) Profit, 100%(1) Loss, 0 Open, 1 Finished, 1 Total
    # 19 hours 26 min. Average Time

    20: {
        'doc': 'Только RSI 1h\n'
               '1h RSI less than 20\n'
               '1d MACD more than SIGNAL\n'
               'TP-3%, SL-1,5%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 20,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.03,
        'stop_loss': 0.985
    },  # 1h RSI + 1d MACD (buy)
    23: {
        'doc': 'Только RSI 1h\n'
               '1h RSI less than 80\n'
               '1h RSI more than 60\n'
               '1d MACD.macd < MACD.signal',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 80,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 60,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.97,
        'stop_loss': 1.015
    },  # 1h RSI 60-80 + 1d MACD (sell)
    22: {
        'doc': 'Только RSI 1h\n'
               '1h RSI less than 40\n'
               '1h RSI more than 20\n'
               '1d MACD.macd < MACD.signal',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 20,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.03,
        'stop_loss': 0.985
    },  # 1h RSI 20-40 + 1d MACD (buy)
    19: {
        'doc': '#good_strategy\n'
               '5m MACD less than SIGNAL\n'
               '15m RSI more than 70\n'
               '1d MACD less than SIGNAL\n'
               'TP-1,5%, SL-0,75%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '5m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            2: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 70,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.985,
        'stop_loss': 1.0075
    },  # 5m MACD less than signal, 15m RSI more than 70 (sell)
    # 100%(2) Profit, 0%(0) Loss, 0 Open, 2 Finished, 2 Total
    # 14 hours 18 min. Average Time
    # Dublicates 15 strategy

    18: {
        'doc': '5m MACD more than SIGNAL\n'
               '15m RSI less than 24\n'
               '1d MACD less than SIGNAL\n'
               'TP-1,5%, SL-0,75%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '5m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            2: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 24,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.015,
        'stop_loss': 0.9925
    },  # 5m MACD more than signal, 15m RSI less than 30 (buy)
    17: {
        'doc': 'Только RSI 1h\n'
               '1h RSI more than 80\n'
               'TP-3%, SL-1,5%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 80,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.97,
        'stop_loss': 1.015
    },  # 1h RSI more than 80 (sell)
    # 10% Success, 90% Failure, 1 Profit, 9 Loss,
    # 10 Finished, 0 Open, 10 Total, 4 hours 4 min. Average Time

    16: {
        'doc': 'Tолько RSI 1h\n'
               '1h RSI less than 20\n'
               'TP-3%, SL-1,5%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 20,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.03,
        'stop_loss': 0.985
    },  # 1h RSI less than 20 (buy)
    # No one trade 17

    14: {
        'doc': '5m MACD more than SIGNAL\n'
               '15m RSI less than 70\n'
               'TP-1,5%, SL-0,75%',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '5m',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            2: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 24,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.015,
        'stop_loss': 0.9925
    },  # 5m MACD more than signal, 15m RSI less than 70 (buy)
    12: {
        'doc': 'Ловим подскоки\n'
               'В нижней половине\n'
               '1. 1w MACD.macd more than MACD.signal\n'
               '2. 1d RSI less than 27\n'
               '3. 4h RSI less than 20\n'
               '4. 1h RSI less than 20',
        'coins': 3,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1W',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            2: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 27,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 20,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            4: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 20,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.25,
        'stop_loss': 0.9
    },  
    11: {
        'doc': '1d MACD.macd less than 0\n'
               '1d RSI less than 50\n'
               '4h RSI more than 70\n'
               '4h RSI more than 65\n'
               '1d MACD.macd less than MACD.signal\n'
               '15m RSI more than 50',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': 0,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 50,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 70,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            4: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 65,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            5: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            6: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 50,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.9,
        'stop_loss': 1.05
    },  
    10: {
        'doc': '1d RSI less than 35,\n'
               '4h RSI more than 50,\n'
               '1h RSI more than 60',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 35,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 50,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 60,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.98,
        'stop_loss': 1.01
    },  # Стратегия 6 перевернутая и доработанная
    9: {
        'doc': '1. 1W MACD.macd less than 0\n'
               '2. 1W RSI less than 40\n'
               '3. 1d MACD.macd less than 0\n'
               '4. 1d MACD.macd less than MACD.signal\n'
               '5. 1h RSI more than 60\n'
               '6. 30m RSI more than 60',
        'coins': 3,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1W',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': 0,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '1W',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': 0,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            4: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            5: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 60,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            6: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 60,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.8,
        'stop_loss': 1.1
    },  
    8: {
        'doc': '1d RSI less than 35,\n'
               '4h RSI more than 40,\n'
               '1h RSI more than 50',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 35,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 50,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.98,
        'stop_loss': 1.01
    },  # Стратегия 6 перевернутая
    7: {
        'doc': '1.  1W MACD.macd < -1\n'
               '2.  1W MACD.macd < MACD.signal\n'
               '3.  1W RSI < 40\n'
               '4.  1d MACD.macd < 0\n'
               '5.  1d MACD.macd < MACD.signal\n'
               'Растущие\n'
               '6.  4h RSI  > 70\n'
               '7.  4h close > EMA 200\n'
               '8.  1h RSI > 70\n'
               '9.  1h MACD.macd > 55\n'
               '10. 30m RSI > 60\n',
        'coins': 3,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1W',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': -1,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '1W',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            3: {
                'interval': '1W',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            4: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': 0,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            5: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'MACD.signal',
                'coefficient': None
            },
            6: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 70,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            7: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'close',
                'operator': '>',
                'value_2': None,
                'coin_2': None,
                'name_2': 'EMA200',
                'coefficient': None
            },
            8: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 70,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            9: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'MACD.macd',
                'operator': '>',
                'value_2': 55,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            10: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 60,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.8,
        'stop_loss': 1.1
    },  
    6: {
        'doc': 'RSI(1d) less than 35,\n'
               'RSI(4h) more than 40,\n'
               'RSI(1h) more than 50\n',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '1d',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 35,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 50,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.02,
        'stop_loss': 0.99
    },  # strategy
    5: {
        'doc': 'RSI(4h) more than 40,\n'
               'RSI(1h) more than 40,\n'
               'RSI(30m) less than 40,\n'
               'RSI(15m) less than 40,\n'
               'RSI(5m) more than 80',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '5m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 80,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            4: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            5: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.98,
        'stop_loss': 1.01
    },  # strategy
    4: {
        'doc': 'RSI(1h) more than 90,\n'
               'RSI(15m) more than 95.',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 95,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '1h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 90,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # Criteria
        'signal': 'sell',
        'take_profit': 0.98,
        'stop_loss': 1.01
    },  # Strategy
    3: {
        'doc': 'RSI(4h) less than 40,\n'
               'RSI(30m) 30–40,\n'
               'RSI(15m) 40–50.',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 50,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            4: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 30,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            5: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'sell',
        'take_profit': 0.98,
        'stop_loss': 1.01
    },  # strategy
    2: {
        'doc': 'RSI(4h) more than 40,\n'
               'RSI(30m) 30–40,\n'
               'RSI(15m) 40–50.\n',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 50,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            2: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            3: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            4: {
                'interval': '30m',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '<',
                'value_2': 30,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
            5: {
                'interval': '4h',
                'coin_1': None,
                'name_1': 'RSI',
                'operator': '>',
                'value_2': 40,
                'coin_2': None,
                'name_2': None,
                'coefficient': None
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.02,
        'stop_loss': 0.99
    },  # strategy
    1: {
        'doc': 'на 15m цена отклонилась\n'
               'от EMA20 вниз на 3%.',
        'coins': 2,
        'chat_id': None,
        'criteria': {
            1: {
                'interval': '15m',
                'coin_1': None,
                'name_1': 'close',
                'operator': '<',
                'value_2': None,
                'coin_2': None,
                'name_2': 'EMA20',
                'coefficient': 0.97
            },
        },  # criteria
        'signal': 'buy',
        'take_profit': 1.02,
        'stop_loss': 0.99
    }, 
}  # Final
