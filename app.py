import streamlit as st
import akshare as ak

st.set_page_config(page_title="T+分钟级做T系统V3", layout="centered")

st.title("📊 T+分钟级做T系统（盘中版）")

symbol = st.text_input("输入股票代码（如 000001）")

period_map = {
    "1分钟": "1",
    "5分钟": "5",
    "15分钟": "15",
    "30分钟": "30",
    "60分钟": "60"
}

period = st.selectbox("选择K线周期", list(period_map.keys()))

if symbol:

    try:
        # ===== 分钟级数据 =====
        df = ak.stock_zh_a_hist_min_em(
            symbol=symbol,
            period=period_map[period],
            adjust="qfq"
        )

        df = df.tail(100)

        close = df["收盘"]
        high = df["最高"]
        low = df["最低"]
        vol = df["成交量"]

        price = close.iloc[-1]

        # ===== 区间模型（核心）=====
        day_high = high.max()
        day_low = low.min()

        position = (price - day_low) / (day_high - day_low + 1e-9)

        ma5 = close.rolling(5).mean().iloc[-1]
        ma10 = close.rolling(10).mean().iloc[-1]

        st.write("当前价格：", price)
        st.write("区间高点：", day_high)
        st.write("区间低点：", day_low)
        st.write("当前区间位置：", round(position, 2))
        st.write("MA5：", ma5)
        st.write("MA10：", ma10)

        # ===== 做T信号引擎（升级核心）=====

        if position < 0.25:
            st.success("🟢 低位区 → 适合低吸做T")

        elif position > 0.75:
            st.error("🔴 高位区 → 适合高抛做T")

        elif ma5 > ma10:
            st.warning("🟡 上升趋势中 → 回踩低吸")

        else:
            st.warning("🟡 震荡中 → 等机会")

    except Exception as e:
        st.error("数据加载失败（可能是分钟数据接口限制）")
        st.write(e)
