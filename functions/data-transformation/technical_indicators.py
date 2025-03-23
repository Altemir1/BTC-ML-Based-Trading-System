import pandas as pd
from ta.trend import EMAIndicator, MACD, ADXIndicator, PSARIndicator
from ta.volatility import BollingerBands, AverageTrueRange, KeltnerChannel
from ta.volume import OnBalanceVolumeIndicator, ChaikinMoneyFlowIndicator, AccDistIndexIndicator


def add_technical_indicators(df):
    # Normalize column names
    df = df.rename(columns={
        'Open Time': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low',
        'Close': 'close', 'Volume': 'volume'
    })
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    # Trend Indicators
    df['ema_5'] = EMAIndicator(close=df['close'], window=5).ema_indicator()
    df['ema_20'] = EMAIndicator(close=df['close'], window=20).ema_indicator()
    df['ema_50'] = EMAIndicator(close=df['close'], window=50).ema_indicator()

    macd = MACD(close=df['close'])
    df['macd'] = macd.macd()
    df['signal'] = macd.macd_signal()
    df['histogram'] = macd.macd_diff()

    adx = ADXIndicator(high=df['high'], low=df['low'], close=df['close'], window=14)
    df['adx'] = adx.adx()
    df['plus_di'] = adx.adx_pos()
    df['minus_di'] = adx.adx_neg()

    psar = PSARIndicator(high=df['high'], low=df['low'], close=df['close'], step=0.02, max_step=2)
    df['psar'] = psar.psar()
    df['psar_up'] = psar.psar_up()
    df['psar_down'] = psar.psar_down()

    # Volatility Indicators
    bb = BollingerBands(close=df['close'], window=20, window_dev=2)
    df['bb_upper'] = bb.bollinger_hband()
    df['bb_lower'] = bb.bollinger_lband()
    df['bb_middle'] = bb.bollinger_mavg()

    atr = AverageTrueRange(high=df['high'], low=df['low'], close=df['close'], window=14)
    df['ATR'] = atr.average_true_range()

    kc = KeltnerChannel(high=df['high'], low=df['low'], close=df['close'], window=20, window_atr=10)
    df['kc_upper'] = kc.keltner_channel_hband()
    df['kc_lower'] = kc.keltner_channel_lband()
    df['kc_middle'] = kc.keltner_channel_mband()

    # Donchian Channels (manual)
    df['donchian_upper'] = df['high'].rolling(window=20).max()
    df['donchian_lower'] = df['low'].rolling(window=20).min()
    df['donchian_middle'] = (df['donchian_upper'] + df['donchian_lower']) / 2

    # Volume Indicators
    df['obv'] = OnBalanceVolumeIndicator(close=df['close'], volume=df['volume']).on_balance_volume()

    df['vwap'] = (df['close'] * df['volume']).cumsum() / df['volume'].cumsum()

    cmf = ChaikinMoneyFlowIndicator(high=df['high'], low=df['low'], close=df['close'], volume=df['volume'], window=20)
    df['cmf'] = cmf.chaikin_money_flow()

    ad = AccDistIndexIndicator(high=df['high'], low=df['low'], close=df['close'], volume=df['volume'])
    df['ad_line'] = ad.acc_dist_index()

    return df
