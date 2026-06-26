import streamlit as st
from streamlit_autorefresh import st_autorefresh

from data_pro import DataEnginePro
from strategy import t_signal

st.set_page_config(page_title="T+实时系统", layout="centered")

st.title("📊 T+实时做T系统")

symbol = st.text_input("股票代码")

# 🔥 每5秒刷新一次
st_autorefresh(interval=5000, key="refresh")

if symbol:

    engine = DataEnginePro()
    df = engine.get_daily(symbol)

    if df is None:
        st.error("数据加载失败")
        st.stop()

    signal = t_signal(df)
    price = df["close"].iloc[-1]

    col1, col2 = st.columns(2)
    col1.metric("价格", price)
    col2.metric("信号", signal)
