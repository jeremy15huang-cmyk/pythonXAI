import streamlit as st
import time

if st.button("重新整理", key="button1"):  # 如果按鈕被按下
    st.success("準備重新整理")  # 顯示綠色訊息
    time.sleep(3)  # 等待3秒
    st.rerun()  # 重新整理整個頁面

if 'itemsa' not in st.session_state:
    st.session_state.itemsa = []  # 如果session_state中沒有items，則初始化為空列表

st.title("點餐機")
col1, col2 = st.columns(2)
with col1:
    food = st.text_input("請輸入餐點")
    st.title("購物籃")
with col2:
    if st.button("加入",key="button2"):
        st.write(st.session_state.itemsa.append(food))  # 將輸入的餐點加入session_state中的items列表中
        
    

for idx, i in enumerate(st.session_state.itemsa):
    col_item, col_btn = st.columns([4, 1])
    with col_item:
        st.write(i)
    with col_btn:
        if st.button("刪除", key=f"delete_{idx}"):
            st.session_state.itemsa.pop(idx)
            st.rerun()