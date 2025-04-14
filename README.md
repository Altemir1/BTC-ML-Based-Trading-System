# BTC-ML-Based-Trading-System
Welcome to the repository of trading system that is based on machine learning approach. Here you will find notebooks for such neural network as LSTM and machine learning model XGBoost
trained on datasets with different transformations before fitting.

## Features
The following features are included in this repository, along with the details of their origins:
**Sentiment Features**
- `negative` – Sentiment: Negative sentiment score extracted from articles using the FinBERT model (imported from Hugging Face).
- `neutral` – Sentiment: Neutral sentiment score from the same set of articles.
- `positive` – Sentiment: Positive sentiment score provided by the FinBERT model.
  
**Bitcoin Price Data** (fetched via Binance API)
- `open` – Price: Opening price of Bitcoin for the given time period.
- `high` – Price: Highest price of Bitcoin during the period.
- `low` – Price: Lowest price of Bitcoin during the period.
- `close` – Price: Closing price of Bitcoin for the period.
- `volume` – Volume: Trading volume of Bitcoin over the period.
  
**Technical Indicators** (computed with the ta library)
- `ema_5` – Moving Average: Exponential moving average over 5 periods.
- `ema_20` – Moving Average: Exponential moving average over 20 periods.
- `ema_50` – Moving Average: Exponential moving average over 50 periods.
- `macd` – Momentum: Moving Average Convergence Divergence indicator.
- `signal` – Momentum: Signal line for MACD.
- `histogram` – Momentum: MACD histogram, representing the difference between MACD and the signal line.
- `bb_upper` – Bollinger Bands: Upper Bollinger Band value.
- `bb_middle` – Bollinger Bands: Middle line of the Bollinger Bands (usually a moving average).
- `bb_lower` – Bollinger Bands: Lower Bollinger Band value.
- `ATR` – Volatility: Average True Range, a measure of market volatility.
- `donchian_upper` – Channel: Upper boundary of the Donchian channel.
- `donchian_lower` – Channel: Lower boundary of the Donchian channel.
  
**Additional Market Data **(sourced using the yfinance library)
- `treasury_bond` – Market Indicator: Treasury bond yields used to assess economic conditions and risk-off sentiment.
- `dollar_index` – Market Indicator: U.S. Dollar Index, representing the strength of the dollar against a basket of major currencies.
- `gold` – Commodity: Price of gold, used as a safe-haven asset indicator.
- `sp500` – Equity Market: S&P 500 index value, reflecting U.S. stock market performance.
- `nasdaq` – Equity Market: NASDAQ composite index value, representing technology and growth stocks.
- `volatility_index` – Volatility: The VIX, or CBOE Volatility Index, indicating market sentiment and volatility.
- `wti` – Commodity: Price of West Texas Intermediate crude oil, a key indicator in the commodities market.

## Models

**LSTM Architecture**
![model](https://github.com/user-attachments/assets/a5cc6246-8ab8-47ec-bbd3-f475a2bbc4fb)

