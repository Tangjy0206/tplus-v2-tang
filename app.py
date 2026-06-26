import streamlit as st
from data_pro import DataEnginePro
from strategy import t_signal

st.title("📊 T+系统（稳定数据版V3）")

symbol = st.text_input("股票代码（如 000001）")

engine = DataEnginePro()

if symbol:

    df = engine.get_daily(symbol)

    if df is None:
        st.error("数据加载失败")
        st.stop()

    signal = t_signal(df)

    st.subheader("交易信号")
    st.write(signal)

    st.subheader("最新价格")
    st.write(df["close"].iloc[-1])
