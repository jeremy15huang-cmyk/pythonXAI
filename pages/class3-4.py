import streamlit as st
import random

# --- 網頁的「記憶功能」 ---
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.feedback = ""
    st.session_state.min_val = 1
    st.session_state.max_val = 100

# --- 網頁畫面設計 ---
st.title("🎉 網頁版猜數字遊戲！ 🎉")

# --- 遊戲進行中 ---
if not st.session_state.game_over:
    # 🆕 把範圍直接放進請輸入的提示文字（Label）裡！
    input_label = f"請輸入你猜的數字 ({st.session_state.min_val} ~ {st.session_state.max_val})："
    
    guess = st.number_input(
        label=input_label,  # 🆕 動態更新提示文字
        min_value=st.session_state.min_val,  
        max_value=st.session_state.max_val,  
        value=int((st.session_state.min_val + st.session_state.max_val) / 2), # 預設正中間的值
        step=1,
        key="current_guess"
    )
    
    # 按鈕觸發判斷
    if st.button("我猜這個數字！", type="primary"):
        st.session_state.attempts += 1 # 累計次數
        
        if guess < st.session_state.secret_number:
            st.session_state.feedback = f"📈 數字 {guess} 太低了！再往上猜猜看。"
            st.session_state.min_val = guess + 1
            st.rerun() # ⚡ 立即重新整理，刷新提示文字中的範圍！
            
        elif guess > st.session_state.secret_number:
            st.session_state.feedback = f"📉 數字 {guess} 太高了！再往下猜猜看。"
            st.session_state.max_val = guess - 1
            st.rerun() # ⚡ 立即重新整理，刷新提示文字中的範圍！
            
        else:
            st.session_state.feedback = "🎉 答對了！"
            st.session_state.game_over = True
            st.rerun()

# --- 顯示結果與放氣球 ---
if st.session_state.game_over:
    st.success(f"🎊 恭喜你答對了！答案就是 {st.session_state.secret_number}！")
    st.write(f"🏆 你總共花了 {st.session_state.attempts} 次嘗試。")
    st.balloons() # 噴氣球！
    
    if st.button("再玩一次"):
        del st.session_state.secret_number
        del st.session_state.attempts
        del st.session_state.game_over
        del st.session_state.feedback
        del st.session_state.min_val
        del st.session_state.max_val
        st.rerun()
else:
    if st.session_state.feedback != "":
        st.info(st.session_state.feedback)