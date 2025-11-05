# import the necessary packages
from datetime import datetime
import matplotlib.pyplot as plt
#import seaborn as sns
import yfinance as yf

import pandas as pd

# set the name of the ticker we want to download market data for
ticker = "NVDA"
tickers = ["XLK", "XLF", "XLE", "XLV", "XLY"]  # teknologi, finansial, energi, healthcare, consumer
benchmark = "SPY"


# set the start and end dates for our market data request
end_date = datetime(year=2025, month=3, day=1)
start_date = datetime(year=2023, month=1, day=1)

# download market data for a single ticker
df_single = yf.download(
    tickers=tickers,
    #start=start_date,
    #end=end_date,
    #interval="1d",
    period="6mo",
    group_by="ticker",
    auto_adjust=True,
    progress=False
)
print(df_single)


# --- 1. Pilih ticker sektor ETF & benchmark (SPY sebagai S&P 500) ---
tickers = ["XLK", "XLF", "XLE", "XLV", "XLY"]  # teknologi, finansial, energi, healthcare, consumer
benchmark = "SPY"

# --- 2. Unduh data harga (adjusted close) ---
data = yf.download(tickers + [benchmark], period="6mo",auto_adjust=True)

print(data)