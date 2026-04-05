import yfinance as yf
import pandas as pd

class QuantBrain:
    def get_market_trend(self, ticker="BTC-USD"):
        # 1. Pull last 7 days of data
        data = yf.download(ticker, period="7d", interval="1d")
        
        # 2. FIX: Flatten Multi-Index columns (yfinance 2026 fix)
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        # 3. Calculate 3-day Moving Average (MA)
        data['MA3'] = data['Close'].rolling(window=3).mean()
        
        # 4. Use .values[-1] to get the absolute raw number
        current_price = float(data['Close'].values[-1])
        ma3 = float(data['MA3'].values[-1])

        if current_price > ma3:
            return "BULLISH", current_price
        else:
            return "BEARISH", current_price

if __name__ == "__main__":
    # Make sure to import pandas for the fix
    import pandas as pd
    qb = QuantBrain()
    trend, price = qb.get_market_trend()
    print(f"Trend: {trend}, Price: {price}")