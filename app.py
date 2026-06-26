import streamlit as st
from data_pro import DataEnginePro
from strategy import t_signal

st.set_page_config(page_title="T+系统", layout="centered")

st.title("📊 T+做T系统")

symbol = st.text_input("输入股票代码")

# ✅ 关键：必须实例化
engine = DataEnginePro()

if symbol:

    df = engine.get_daily(symbol)

    if df is None or len(df) == 0:
        st.error("数据加载失败")
        st.stop()

    signal = t_signal(df)
    price = df["close"].iloc[-1]

    st.metric("价格", price)
    st.write("信号：", signal)
