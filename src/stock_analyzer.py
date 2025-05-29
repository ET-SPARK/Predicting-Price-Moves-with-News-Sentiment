# src/stock_analyzer.py

import pandas as pd
import talib
import matplotlib.pyplot as plt
import os

class StockAnalyzer:
    def __init__(self, symbol: str, file_path: str):
        self.symbol = symbol
        self.file_path = file_path
        self.df = pd.DataFrame()

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path, parse_dates=['Date'])
            self.df.sort_values('Date', inplace=True)
            self.df.reset_index(drop=True, inplace=True)
            # Ensure columns exist
            required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
            for col in required_columns:
                if col not in self.df.columns:
                    raise ValueError(f"Missing required column: {col}")
            return True
        except Exception as e:
            print(f"[{self.symbol}] Error loading data: {e}")
            return False

    def calculate_indicators(self):
        try:
            self.df['SMA_20'] = talib.SMA(self.df['Close'], timeperiod=20)
            self.df['RSI_14'] = talib.RSI(self.df['Close'], timeperiod=14)
            macd, macd_signal, _ = talib.MACD(self.df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
            self.df['MACD'] = macd
            self.df['MACD_Signal'] = macd_signal
        except Exception as e:
            print(f"[{self.symbol}] Error calculating indicators: {e}")

    def visualize(self):
        try:
            plt.figure(figsize=(14, 6))
            plt.plot(self.df['Date'], self.df['Close'], label='Close')
            plt.plot(self.df['Date'], self.df['SMA_20'], label='SMA 20')
            plt.title(f"{self.symbol} - Closing Price & SMA")
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()
            plt.grid()
            plt.tight_layout()
            plt.show()

            plt.figure(figsize=(14, 3))
            plt.plot(self.df['Date'], self.df['RSI_14'], label='RSI 14', color='orange')
            plt.axhline(70, color='red', linestyle='--')
            plt.axhline(30, color='green', linestyle='--')
            plt.title(f"{self.symbol} - RSI")
            plt.grid()
            plt.tight_layout()
            plt.show()

            plt.figure(figsize=(14, 3))
            plt.plot(self.df['Date'], self.df['MACD'], label='MACD', color='blue')
            plt.plot(self.df['Date'], self.df['MACD_Signal'], label='MACD Signal', color='red')
            plt.title(f"{self.symbol} - MACD")
            plt.legend()
            plt.grid()
            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"[{self.symbol}] Error visualizing data: {e}")
