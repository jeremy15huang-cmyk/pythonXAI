import streamlit as st
number = st.number_input("請輸入一個整數", step=1, min_value=1, max_value=9)
for a in range(1, number+1, 1):
    st.write(str(a)*a)