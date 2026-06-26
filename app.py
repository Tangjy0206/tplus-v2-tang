import streamlit as st
from data import DataEngine
from strategy import t_signal

st.set_page_config(page_title="T+量化系统V3", layout="centered")

st.title("📊 T+量化做T系统 V3（架构版）")

symbol = st.text_input("输入股票代码（如 000001）")

period = st.selectbox("周期", ["5分钟", "15分钟", "60分钟"])

engine = DataEngine()

if symbol:

    df = engine.get_daily(symbol)

    signal = t_signal(df)

    st.subheader("📡 信号输出")
    st.write(signal)

    st.subheader("📊 最新价格")
    st.write(df["收盘"].iloc[-1])
