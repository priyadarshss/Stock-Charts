import yfinance as yf
import streamlit as st

st.write("""
# Stock Price App
""")
st.sidebar.header("Select the options below to view the Chart")
ticker = st.sidebar.selectbox("Select Stock", ("BTC-USD", "AMZN", "GOOGL", "MSFT", "FB"))
tickerdata = yf.Ticker(ticker)
start = st.sidebar.text_input("Enter start of the time period (YYYY-MM-DD):")
end = st.sidebar.text_input("Enter end of the time period (YYYY-MM-DD):")
tickerdf = tickerdata.history(period="1h", start=start, end=end)
st.write("""
**Opening Price**""")
st.area_chart(tickerdf.Open)
st.write("""
**Volume Price**""")
st.area_chart(tickerdf.Volume)
st.write("""
**Closing Price**""")
st.area_chart(tickerdf.Close)