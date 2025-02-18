import pandas as pd
import numpy as np
import ta 

def techincal_indicators(df, window=20):
    # Rename columns for convinience of use
    df.rename(columns={"Open Time": "date", "Open": "open", "High": "high", "Low": "low", "Close": "close", "Volume": "volume"}, inplace=True)

    df.drop(columns=['date'], inplace=True)

    # volume to volume in usd represantation
    df["volume_usd"] = df["volume"] * df["close"]

    # Trend indicators
    # Exponential moving average
    df["ema_20"] = ta.trend.ema_indicator(df["close"], window=window)

    # Moving average convergence divergence
    df["macd"] = ta.trend.macd(df["close"])

    # Momentum indicators
    # Relativae strength index
    df["rsi"] = ta.momentum.rsi(df["close"])

    # Stochaistic oscialtor
    df["stoch"] = ta.momentum.stoch(df["high"], df["low"], df["close"])

    # Volatility indicators
    # Bollinger bands
    bb = ta.volatility.BollingerBands(df['close'], window=20)
    df['bollinger_hband'] = bb.bollinger_hband()
    df['bollinger_lband'] = bb.bollinger_lband()

    # Average true range
    df["atr"] = ta.volatility.AverageTrueRange(df["high"], df["low"], df["close"]).average_true_range()

    # Volume based indicators
    # On-balance volume
    df["obv"] = ta.volume.on_balance_volume(df["close"], df["volume_usd"])

    # Drop null rows as some of TI creates them
    df.dropna(inplace=True)

    return df

    