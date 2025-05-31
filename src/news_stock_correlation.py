# src/news_stock_correlation.py

import pandas as pd
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import os
import logging
from datetime import datetime, timedelta
from typing import Tuple, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class NewsStockCorrelation:
    """
    A class to analyze correlation between financial news sentiment and stock price movements.
    """
    
    def __init__(self, news_path: str, stock_path: str, symbol: str):
        """
        Initialize with paths to news and stock data, and the stock symbol.
        """
        self.news_path = news_path
        self.stock_path = stock_path
        self.symbol = symbol
        self.news_df = pd.DataFrame()
        self.stock_df = pd.DataFrame()
        self.merged_df = pd.DataFrame()
        
    def load_data(self) -> bool:
        """
        Load and validate news and stock data.
        Returns True if successful, False otherwise.
        """
        try:
            # Load news data
            self.news_df = pd.read_csv(self.news_path, parse_dates=['date'])
            required_news_cols = ['date', 'headline', 'publisher']
            if not all(col in self.news_df.columns for col in required_news_cols):
                logging.error(f"News data missing required columns. Needed: {required_news_cols}")
                return False
            
            # Load stock data
            self.stock_df = pd.read_csv(self.stock_path, parse_dates=['Date'])
            required_stock_cols = ['Date', 'Close']
            if not all(col in self.stock_df.columns for col in required_stock_cols):
                logging.error(f"Stock data missing required columns. Needed: {required_stock_cols}")
                return False
                
            return True
            
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            return False
    
    def align_dates(self) -> None:
        """
        Align news dates with trading days by adjusting news dates to the next trading day
        if they occur on non-trading days (weekends/holidays).
        """
        try:
            # Ensure we have trading days
            trading_days = self.stock_df['Date'].dt.date.unique()
            
            def adjust_to_trading_day(date):
                date = date.date()
                while date not in trading_days:
                    date += timedelta(days=1)
                return date
                
            self.news_df['aligned_date'] = self.news_df['date'].apply(adjust_to_trading_day)
            logging.info("Date alignment completed successfully.")
            
        except Exception as e:
            logging.error(f"Error in date alignment: {e}")
            raise
    
    def analyze_sentiment(self) -> None:
        """
        Perform sentiment analysis on news headlines using TextBlob.
        """
        try:
            def get_sentiment(text):
                analysis = TextBlob(str(text))
                return analysis.sentiment.polarity
                
            self.news_df['sentiment'] = self.news_df['headline'].apply(get_sentiment)
            logging.info("Sentiment analysis completed.")
            
        except Exception as e:
            logging.error(f"Error in sentiment analysis: {e}")
            raise
    
    def calculate_daily_metrics(self) -> None:
        """
        Calculate daily average sentiment and stock returns.
        """
        try:
            # Calculate daily average sentiment
            daily_sentiment = self.news_df.groupby('aligned_date')['sentiment'].agg(['mean', 'count'])
            daily_sentiment.columns = ['avg_sentiment', 'news_count']
            
            # Calculate daily stock returns
            self.stock_df['daily_return'] = self.stock_df['Close'].pct_change() * 100
            self.stock_df['date_only'] = self.stock_df['Date'].dt.date
            
            # Merge the data
            self.merged_df = pd.merge(
                daily_sentiment,
                self.stock_df[['date_only', 'daily_return', 'Close']],
                left_index=True,
                right_on='date_only',
                how='inner'
            )
            
            # Drop rows with NaN returns (first day)
            self.merged_df.dropna(subset=['daily_return'], inplace=True)
            logging.info("Daily metrics calculation completed.")
            
        except Exception as e:
            logging.error(f"Error calculating daily metrics: {e}")
            raise
    
    def calculate_correlation(self) -> Tuple[float, Optional[float]]:
        """
        Calculate Pearson correlation between sentiment and stock returns.
        Returns correlation coefficient and p-value.
        """
        try:
            from scipy.stats import pearsonr
            corr, p_value = pearsonr(
                self.merged_df['avg_sentiment'],
                self.merged_df['daily_return']
            )
            logging.info(f"Correlation between sentiment and returns: {corr:.3f} (p-value: {p_value:.3f})")
            return corr, p_value
            
        except Exception as e:
            logging.error(f"Error calculating correlation: {e}")
            raise
    
    def visualize_results(self, save_path: Optional[str] = None) -> None:
        """
        Visualize the correlation analysis results.
        """
        try:
            plt.figure(figsize=(14, 10))
            
            # Plot 1: Sentiment vs Returns Scatter
            plt.subplot(2, 2, 1)
            sns.regplot(
                x='avg_sentiment',
                y='daily_return',
                data=self.merged_df,
                scatter_kws={'alpha': 0.5},
                line_kws={'color': 'red'}
            )
            plt.title(f'Sentiment vs Daily Returns ({self.symbol})')
            plt.xlabel('Average Daily Sentiment Score')
            plt.ylabel('Daily Return (%)')
            
            # Plot 2: Sentiment Distribution
            plt.subplot(2, 2, 2)
            sns.histplot(self.news_df['sentiment'], bins=30, kde=True)
            plt.title('Sentiment Score Distribution')
            plt.xlabel('Sentiment Score')
            
            # Plot 3: Daily Returns Distribution
            plt.subplot(2, 2, 3)
            sns.histplot(self.merged_df['daily_return'], bins=30, kde=True)
            plt.title('Daily Returns Distribution')
            plt.xlabel('Daily Return (%)')
            
            # Plot 4: Time Series of Sentiment and Returns
            plt.subplot(2, 2, 4)
            ax1 = plt.gca()
            ax2 = ax1.twinx()
            
            sns.lineplot(
                x='date_only',
                y='avg_sentiment',
                data=self.merged_df,
                ax=ax1,
                color='blue',
                label='Sentiment'
            )
            sns.lineplot(
                x='date_only',
                y='daily_return',
                data=self.merged_df,
                ax=ax2,
                color='orange',
                label='Return'
            )
            plt.title('Sentiment and Returns Over Time')
            ax1.set_xlabel('Date')
            ax1.set_ylabel('Sentiment Score', color='blue')
            ax2.set_ylabel('Daily Return (%)', color='orange')
            
            plt.tight_layout()
            
            if save_path:
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                plt.savefig(save_path)
                logging.info(f"Visualization saved to {save_path}")
            plt.show()
            
        except Exception as e:
            logging.error(f"Error visualizing results: {e}")
            raise
    
    def run_analysis(self, output_dir: str = '../results') -> dict:
        """
        Run complete analysis pipeline.
        Returns dictionary with results.
        """
        try:
            os.makedirs(output_dir, exist_ok=True)
            
            if not self.load_data():
                return {"error": "Data loading failed"}
                
            self.align_dates()
            self.analyze_sentiment()
            self.calculate_daily_metrics()
            corr, p_value = self.calculate_correlation()
            
            # Save merged data
            merged_path = os.path.join(output_dir, f"{self.symbol}_news_stock_merged.csv")
            self.merged_df.to_csv(merged_path, index=False)
            
            # Save visualization
            viz_path = os.path.join(output_dir, f"{self.symbol}_correlation_plot.png")
            self.visualize_results(viz_path)
            
            return {
                "symbol": self.symbol,
                "correlation": corr,
                "p_value": p_value,
                "num_observations": len(self.merged_df),
                "merged_data_path": merged_path,
                "visualization_path": viz_path
            }
            
        except Exception as e:
            logging.error(f"Analysis failed: {e}")
            return {"error": str(e)}