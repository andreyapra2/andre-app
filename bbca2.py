import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from datetime import date, timedelta

# --- Sidebar input ---
st.sidebar.header("Pengaturan Input")

# Pilihan ticker
tickers = st.sidebar.multiselect(
    "Pilih ticker:",
    ["BBCA.JK", "^JKSE"],
    default=["BBCA.JK", "^JKSE"]
)

# Pilihan tanggal
today = date.today()
default_start = today - timedelta(days=180)

date_range = st.sidebar.date_input(
    "Pilih rentang tanggal:",
    value=(default_start, today),
    min_value=date(2000, 1, 1),
    max_value=today
)

# Pastikan range valid
if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    st.error("Silakan pilih rentang tanggal yang valid.")
    st.stop()

# --- 1. Download data harga ---
if tickers:
    data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)["Close"]

    if data.empty:
        st.warning("Tidak ada data pada rentang tanggal tersebut.")
    else:
        # --- 2. Hitung RS hanya kalau pilih dua ticker ---
        if len(tickers) == 2:
            st.subheader("Data Harga")
            st.dataframe(data.tail())

            data['RS'] = data[tickers[0]] / data[tickers[1]]

            N, M = 14, 14
            data['RS_Ratio'] = 100 * data['RS'] / data['RS'].rolling(N).mean()
            data['RS_Momentum'] = 100 * data['RS_Ratio'] / data['RS_Ratio'].rolling(M).mean()

            # --- 3. Plot RRG sederhana ---
            fig, ax = plt.subplots(figsize=(8,6))
            ax.plot(data['RS_Ratio'], data['RS_Momentum'], marker='o', alpha=0.7)

            ax.axvline(100, color='gray', linestyle='--')
            ax.axhline(100, color='gray', linestyle='--')

            ax.set_xlabel("RS-Ratio")
            ax.set_ylabel("RS-Momentum")
            ax.set_title(f"Relative Rotation Graph (RRG): {tickers[0]} vs {tickers[1]}")

            # Anotasi tanggal terakhir
            last_date = data.dropna().index[-1].strftime('%Y-%m-%d')
            ax.annotate(last_date,
                        (data['RS_Ratio'].iloc[-1], data['RS_Momentum'].iloc[-1]),
                        textcoords="offset points", xytext=(5,5), fontsize=9)

            ax.grid(True, alpha=0.3)

            st.pyplot(fig)

        else:
            st.warning("Silakan pilih **2 ticker** untuk menghitung RRG.")
else:
    st.warning("Pilih minimal 1 ticker.")
