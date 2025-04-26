# BTC-price-direction-prediction
Welcome to the repository for BTC prediction of price direction. Here you will find notebooks with experiments on Long short term memory neural network and machine learning model XGBoost
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

Parameters that was used to find best model:
```
window_sizes = list(range(10, 101, 10))
batch_sizes = [64, 128]
```
**XGBOOST**

Paramters used in the grid search for the best model:
```
param_grid = {
      'max_depth': [3, 5, 7],
      'learning_rate': [0.01, 0.1, 0.2],
      'n_estimators': [100, 200, 300],
      'subsample': [0.8, 1.0]
  }
```

## Dataset transformation
Training of the models was done in using these 4 transformation:

1) Log transformation
2) Log transformation with normalization
3) Min max normalization
4) Standard scaling


## Results

**LSTM models**

| Transformation | Window Size | Batch Size | Test Accuracy |
|:---------------|:------------|:-----------|:--------------|
| Log |   100     | 128      | 52.5%   |
| Log-Norm  |20| 64    | 53.5%    |
| MinMax Norm| 20  | 128         | 53.5%         |
| Standard scale|20| 128| 54.8%|

**XGboost models**
| Transformation | Test Accuracy |
|:---------------|:--------------|
| Log | 52%   |
| Log-Norm  |52%|
| MinMax Norm| 51%|
| Standard scale| 51%|

## Conclusion
Between these two models better results was on LSTM model with accuracy of 54.8%,  2-3 percent better than xgboost model. However it's still not enough to use this model in trading strategies. 
From parameters in the lsmt models the window size in 20 ticks showed best performance in most of transformed datasets. In our case one tick is 1 day.




