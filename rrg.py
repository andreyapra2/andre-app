import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Pilih ticker sektor ETF & benchmark (SPY sebagai S&P 500) ---
tickers = ["XLK", "XLF", "XLE", "XLV", "XLY"]  # teknologi, finansial, energi, healthcare, consumer
benchmark = "SPY"

# --- 2. Unduh data harga (adjusted close) ---
data = yf.download(tickers + [benchmark], period="6mo",interval="1wk",auto_adjust=True)["Close"]

# --- 3. Hitung return harian ---
returns = data.pct_change().dropna()

# --- 4. Hitung relative strength (RS) terhadap benchmark ---
rs = returns[tickers].sub(returns[benchmark], axis=0)

# --- 5. Rolling mean untuk RS-Ratio & RS-Momentum ---
window = 20
rs_ratio = rs.rolling(window).mean()
rs_momentum = rs_ratio.diff()

# --- 6. Ambil nilai terakhir untuk plot RRG ---
latest_ratio = rs_ratio.iloc[-1]
latest_momentum = rs_momentum.iloc[-1]

# --- 7. Plot RRG ---
plt.figure(figsize=(10, 7))
for t in tickers:
    plt.scatter(latest_ratio[t], latest_momentum[t], label=t, s=120)
    plt.text(latest_ratio[t]+0.0001, latest_momentum[t], t, fontsize=10)

# Tambahkan garis sumbu
plt.axhline(0, color="gray", linestyle="--")
plt.axvline(0, color="gray", linestyle="--")

plt.title("Relative Rotation Graph (RRG) vs SPY")
plt.xlabel("RS-Ratio (Relative Strength)")
plt.ylabel("RS-Momentum")
plt.legend()
plt.show()
