import requests
import pandas as pd
import time

BINANCE_URL = "https://api.binance.com/api/v3/klines"

def fetch_binance_candles(symbol, interval, max_limit=1000, save_csv=True):
    all_data = []
    end_time = None  # Start with most recent data

    while True:
        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": max_limit  # Fetch 1000 records at a time
        }
        if end_time:
            params["endTime"] = end_time  # Move backward in time

        response = requests.get(BINANCE_URL, params=params)
        data = response.json()

        if not data or len(data) == 0:
            break  # Stop fetching if no data is returned
        
        # Convert response to DataFrame
        df = pd.DataFrame(data, columns=[
            "Open Time", "Open", "High", "Low", "Close", "Volume",
            "Close Time", "Quote Asset Volume", "Number of Trades",
            "Taker Buy Base Asset Volume", "Taker Buy Quote Asset Volume", "Ignore"
        ])

        # Convert timestamps
        df["Open Time"] = pd.to_datetime(df["Open Time"], unit='ms')
        df["Close Time"] = pd.to_datetime(df["Close Time"], unit='ms')

        # Keep relevant columns
        df = df[["Open Time", "Open", "High", "Low", "Close", "Volume"]]

        # Append new data to list
        all_data.append(df)

        # Correctly update `end_time` to fetch older data
        end_time = int(df.iloc[0]["Open Time"].timestamp() * 1000)  # Take oldest record

        print(f"Fetched {len(df)} records from {df.iloc[0]['Open Time']} to {df.iloc[-1]['Open Time']} for interval {interval}")
        
        if len(df) < 2:
            break
        # Binance rate limit (to avoid getting blocked)
        time.sleep(0.5)


    # Merge all fetched data
    if all_data:
        final_df = pd.concat(all_data).drop_duplicates().sort_values("Open Time").reset_index(drop=True)

        # Save as CSV
        if save_csv:
            filename = f"{symbol}_{interval}_candlesticks.csv"
            final_df.to_csv(filename, index=False)
            print(f"Data saved as {filename}")

