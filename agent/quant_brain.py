import yfinance as yf
import pandas as pd
import time

class QuantBrain:
    def get_market_trend(self, ticker="BTC-USD"):
        """Fetches data with a 3-attempt retry logic for professional stability"""
        for attempt in range(3):
            try:
                # 1. Pull data
                data = yf.download(ticker, period="7d", interval="1d", progress=False)
                
                if data.empty:
                    raise ValueError("No data returned from API")

                # 2. Fix Multi-Index (Standard yfinance 2026 fix)
                if isinstance(data.columns, pd.MultiIndex):
                    data.columns = data.columns.get_level_values(0)

                # 3. Calculate Math
                data['MA3'] = data['Close'].rolling(window=3).mean()
                current_price = float(data['Close'].values[-1])
                ma3 = float(data['MA3'].values[-1])

                trend = "BULLISH" if current_price > ma3 else "BEARISH"
                return trend, current_price

            except Exception as e:
                print(f"⚠️ Quant Error (Attempt {attempt+1}/3): {e}")
                if attempt < 2:
                    time.sleep(2) # Wait 2 seconds before retrying
                else:
                    # If all 3 fail, return a safe "NEUTRAL" state
                    return "NEUTRAL", 0.0

if __name__ == "__main__":
    qb = QuantBrain()
    trend, price = qb.get_market_trend()
    print(f"Trend: {trend}, Price: {price}")