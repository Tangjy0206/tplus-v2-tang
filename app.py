import streamlit as st

st.set_page_config(page_title="T+系统")

st.title("📊 T+系统启动成功")

st.write("如果你看到这里，说明运行成功")

symbol = st.text_input("输入股票代码")

if symbol:
    st.success(f"输入：{symbol}")
