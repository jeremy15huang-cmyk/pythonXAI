import streamlit as st
import os

# 設定網頁標題與圖示
st.set_page_config(page_title="購物平台", page_icon="🛒", layout="wide")

# 1. 初始化 Session State 儲存庫存與購買紀錄
if "inventory" not in st.session_state:
    st.session_state.inventory = {
        "apple": {
            "name": "Apple",
            "price": 10,
            "stock": 10,
            "img_path": "image/apple.png"
        },
        "banana": {
            "name": "Banana",
            "price": 10,
            "stock": 10,
            "img_path": "image/banana.png"
        },
        "bg": {
            "name": "bg",
            "price": 10,
            "stock": 10,
            "img_path": "image/bg.png"
        },
        "orange": {
            "name": "Orange",
            "price": 10,
            "stock": 10,
            "img_path": "image/orange.png"
        }
    }

if "purchase_history" not in st.session_state:
    st.session_state.purchase_history = []


# 2. 購買功能處理
def buy_product(prod_key):
    product = st.session_state.inventory[prod_key]
    if product["stock"] > 0:
        st.session_state.inventory[prod_key]["stock"] -= 1
        st.session_state.purchase_history.append(
            f"🛒 成功購買 1 個 {product['name']} (花費 NT$ {product['price']})"
        )
        st.toast(f"成功購買了 {product['name']}！", icon="✅")
    else:
        st.error("該商品已經售罄囉！")


# --- 網頁主要介面 ---
st.title("🛒 購物平台")
st.write("每樣商品均為 **NT$ 10 元**，初始庫存為 **10 件**。所有商品圖片皆載入自 `image` 資料夾。")
st.markdown("---")

# 3. 「＋ / －」大小設定欄位 (放在商品正上方)
col_size_control, _ = st.columns([1.5, 2.5])
with col_size_control:
    img_size = st.number_input(
        "📐 調整圖片顯示大小 (像素 px)：",
        min_value=50,
        max_value=600,
        value=200,  # 預設 200px
        step=10,
        help="點擊右側的 + 或 - 按鈕來放大或縮小下方的商品圖片"
    )

st.write("")  # 增加一點行高美觀度

# 4. 商品展示區 (四欄並排)
product_cols = st.columns(4)

for idx, (key, item) in enumerate(st.session_state.inventory.items()):
    with product_cols[idx]:
        with st.container(border=True):
            
            # --- 圖片顯示邏輯 ---
            if os.path.exists(item["img_path"]):
                st.image(item["img_path"], width=img_size)
            else:
                placeholder_html = f"""
                <div style='
                    width: {img_size}px;
                    height: {img_size}px;
                    background-color: #e6e9ef;
                    border-radius: 12px;
                    border: 2px dashed #bfc5d1;
                '></div>
                """
                st.markdown(placeholder_html, unsafe_allow_html=True)
                st.caption(f"⚠️ 未能讀取 {item['img_path']}")
            
            st.write("") # 增加圖片與標題間的空隙

            # --- 商品資訊 ---
            st.markdown(f"### {item['name']}")
            st.markdown(f"**價格：NT$ {item['price']}**")
            
            # 顯示庫存狀態與顏色
            stock = item["stock"]
            if stock > 3:
                st.markdown(f"庫存：`{stock}` 件")
            elif 0 < stock <= 3:
                st.markdown(f"庫存：:orange[**緊張！僅剩 {stock} 件**]")
            else:
                st.markdown("庫存：:red[**已售罄 (0)**]")
            
            st.write("")  # 留空
            
            # --- 購買按鈕 ---
            if stock > 0:
                st.button(
                    "購買 🛒",
                    key=f"buy_btn_{key}",
                    on_click=buy_product,
                    args=(key,),
                    type="primary",
                    use_container_width=True
                )
            else:
                st.button(
                    "已售罄 ❌",
                    key=f"buy_btn_{key}",
                    disabled=True,
                    use_container_width=True
                )

# --- 購買歷史紀錄 ---
if st.session_state.purchase_history:
    st.markdown("---")
    st.subheader("🔔 您的購買紀錄")
    for record in reversed(st.session_state.purchase_history):
        st.success(record)


# --- 底部：新增商品庫存區 ---
st.markdown("---")
st.title("📦 新增商品庫存")
st.write("後台管理：請選擇商品並輸入欲增加的庫存數量。")

# 建立兩個等寬、平行分各半的 columns
col_left, col_right = st.columns([1, 1])

# 準備下拉選單的選項對應 (顯示名字，回傳 key)
product_options = {item["name"]: key for key, item in st.session_state.inventory.items()}

# 左邊 Column: 選擇商品下拉選單 + 按鈕放在它下面
with col_left:
    selected_display_name = st.selectbox(
        "🏷️ 選擇商品：",
        options=list(product_options.keys()),
        help="點擊箭頭展開以選擇您要補貨的商品"
    )
    # 取得對應的商品 key (例如: 'apple')
    selected_key = product_options[selected_display_name]
    
    # 這裡放一個空的間隔，讓按鈕看起來更美觀
    st.write("") 
    
    # 點擊此按鈕，執行補貨
    add_clicked = st.button("新增庫存 ➕", type="primary", use_container_width=True)

# 右邊 Column: 設定增加的庫存數量 (可以用 + or - 調整)
with col_right:
    add_amount = st.number_input(
        "🔢 新增庫存數量：",
        min_value=1,
        max_value=100,
        value=5,  # 預設增加 5 個
        step=1,
        help="使用右側 + 或 - 按鈕來增減欲補充的數量"
    )

# 按鈕觸發後的補貨邏輯
if add_clicked:
    st.session_state.inventory[selected_key]["stock"] += add_amount
    st.toast(f"🔌 已成功為 {selected_display_name} 補貨 {add_amount} 件！")
    st.rerun()


# --- 最底部：即時顯示所有商品的現有數量 ---
st.markdown("---")
st.subheader("📊 當前商品即時庫存統計")

# 這裡用 4 個小卡片一排，顯示現在這四個東西各自的數量
info_cols = st.columns(4)
for idx, (key, item) in enumerate(st.session_state.inventory.items()):
    with info_cols[idx]:
        st.metric(
            label=f"{item['name']} 剩餘數量", 
            value=f"{item['stock']} 件"
        )