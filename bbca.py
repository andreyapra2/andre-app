import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Download data harga ---
# BBCA = BBCA.JK (Jakarta Stock Exchange), IHSG = ^JKSE
tickers = ["BBCA.JK", "^JKSE"]
#data = yf.download(tickers, start="2025-01-01", end="2025-09-28", auto_adjust=True)['Close']
data = yf.download(tickers, period="6mo", auto_adjust=True)['Close']


# --- 2. Hitung Relative Strength (RS) ---
data['RS'] = data["BBCA.JK"] / data["^JKSE"]

# --- 3. Hitung RS-Ratio & RS-Momentum ---
N = 21  # window smoothing untuk RS-Ratio
M = 21  # window smoothing untuk RS-Momentum

data['RS_Ratio'] = 100 * data['RS'] / data['RS'].rolling(N).mean()
data['RS_Momentum'] = 100 * data['RS_Ratio'] / data['RS_Ratio'].rolling(M).mean()

print(data)

# --- 4. Plot RRG sederhana ---
plt.figure(figsize=(8,6))
plt.plot(data['RS_Ratio'], data['RS_Momentum'], marker='o', alpha=0.7)

# Tambahkan garis netral 100
plt.axvline(100, color='gray', linestyle='--')
plt.axhline(100, color='gray', linestyle='--')

# Label
plt.xlabel("RS-Ratio")
plt.ylabel("RS-Momentum")
plt.title("Relative Rotation Graph (RRG): BBCA vs IHSG")

# Tambahkan anotasi tanggal terakhir
last_date = data.dropna().index[-1].strftime('%Y-%m-%d')
plt.annotate(last_date, 
             (data['RS_Ratio'].iloc[-1], data['RS_Momentum'].iloc[-1]),
             textcoords="offset points", xytext=(5,5), fontsize=9)

plt.grid(True, alpha=0.3)
plt.show()
