import streamlit as st #匯入streamlit模組並重新命名為 st

#st.number_input()可以讓使用者輸入數字，設step=1可以讓使用者只能輸入整數
#min_value=0可以設定最小值為0，max_value=100可以設定最大值為100
number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=100)
#st.markdown()可以讓使用者輸入markdown語法並顯示在網頁上
st.markdown(f"你輸入的數字是: {number}")

st.markdown("---")
st.markdown("### 練習")

number1 = st.number_input("請輸你的分數", step=1, min_value=0, max_value=100)
if(number1 >= 90):
    st.markdown("你的成績是: A")
elif(89>=number1 >= 80):
    st.markdown("你的成績是: B")
elif(79>=number1 >= 70):
    st.markdown("你的成績是: C")
elif(69>=number1 >= 60):
    st.markdown("你的成績是: D")
else:
    st.markdown("你的成績是: F")

st.markdown("---")
st.markdown("### 按鈕練習")
#st.button()可以在網站上顯示一個按鈕，使用者可以點擊按鈕
#key式按鈕的識別名稱，可以用來分區不同的按鈕
#如果使用者點擊按鈕，st.button()會回傳True，否則回傳False
st.button("按我一下", key="button1")
if st.button("按我一下", key="balloons"):
    st.balloons()
if st.button("按我一下", key="snow"):
    st.snow()
st.markdown("---")