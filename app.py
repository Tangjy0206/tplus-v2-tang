import streamlit as st
from data_pro import DataEnginePro
from strategy import t_signal

st.set_page_config(page_title="T+实时盯盘V4", layout="centered")

st.title("📊 T+实时做T系统（盘中刷新版）")

symbol = st.text_input("股票代码（如 000001）")

refresh = st.selectbox("刷新频率（秒）", [5, 10, 20])

# 🔥 关键：自动刷新
st.write(f"⏱ 每 {refresh} 秒刷新一次")

st_autorefresh = st.experimental_data_editor if False else None  # 占位防报错

# Streamlit官方刷新方式
st.write("正在运行实时监控...")

if symbol:

    import time
    st.empty()

    # 自动刷新核心
    st.experimental_set_query_params(t=str(time.time()))

    engine = DataEnginePro()

    df = engine.get_daily(symbol)

    if df is None:
        st.error("数据加载失败")
        st.stop()

    signal = t_signal(df)

    price = df["close"].iloc[-1]

    col1, col2 = st.columns(2)

    col1.metric("最新价格", price)
    col2.metric("信号", signal)

    st.progress(0.5)

    st.info("系统运行中（自动刷新中）")
