import streamlit as st

# --- 1. アプリ基本設定 ---
st.set_page_config(
    page_title="Protocol ZERO | AI軍師", 
    page_icon="🎯", 
    layout="centered"
)

# カスタムCSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

if 'vip' not in st.session_state:
    st.session_state.vip = False

# サイドバー：認証
with st.sidebar:
    st.title("🔑 VIP ACCESS")
    pwd = st.text_input("認証キーを入力", type="password")
    if pwd == "zero2026":
        st.session_state.vip = True
        st.success("PROTOCOL ZERO: UNLOCKED")
    else:
        st.session_state.vip = False
    st.divider()
    st.caption("v7.3.3 | Secure Build")

# --- タイトル・ロゴセクション ---
# 指定のロゴを中央に配置
st.image("https://raw.githubusercontent.com/slot-judge-dev/slot-judge/main/logo.jpg", use_column_width=True) 
# ※GitHubに logo.jpg という名前で画像をアップロードして保存してください
st.title("🎯 Protocol ZERO")
st.caption("Strategic Pachislot Prediction Engine | v7.3.3")

target_machine = st.selectbox("🎯 ターゲット機種を選択", ["北斗の拳 転生2", "甲鉄城のカバネリ"])
st.divider()

if target_machine == "北斗の拳 転生2":
    st.subheader("👊 北斗の拳 転生2")
    
    col1, col2 = st.columns(2)
    with col1:
        current_abe = st.number_input("液晶あべし数", min_value=0, max_value=2000, value=0)
        is_reset = st.toggle("リセット状態 (天井1280)")
    with col2:
        last_status = st.selectbox("前回終了状態", ["通常", "伝承モード", "★天撃後(128フォロー)"])
        time_slider = st.slider("現在時刻", 9, 23, 12)

    mode_hint = st.selectbox("示唆・前兆", ["なし", "256超前兆(通常B期待)", "通常C濃厚", "天国濃厚"])
    trophy = st.selectbox("サミートロフィー", ["なし", "銅", "金", "キリン", "虹"])

    # 💎 VIPエリア
    diff_coins = 0
    border_adj = 0
    if st.session_state.vip:
        st.divider()
        st.markdown("### 💎 VIP PROFESSIONAL HACK")
        v_col1, v_col2 = st.columns(2)
        with v_col1:
            diff_coins = st.slider("有利区間差枚数", -5000, 5000, 0, step=100)
        with v_col2:
            border_adj = st.slider("手動ボーダー調整", -100, 100, 0, step=10)
        
        h_pay = 4000 if current_abe > 800 else 1500
        st.metric(label="⏱️ 推定想定時給", value=f"￥{h_pay}", delta="VIP Data")
        st.text_area("💬 AI Bro コンサル窓口", placeholder="現場の違和感を言語化してください...")

    if st.button("軍師の最終判断を仰ぐ"):
        st.divider()
        
        max_ceiling = 1280 if is_reset else 1536
        base_border = 950 if not is_reset else 700
        diff_bonus = -150 if st.session_state.vip and diff_coins >= 1000 else 0
        current_border = base_border + border_adj + diff_bonus
        if time_slider >= 18: current_border += 100

        st.markdown("### 📊 分析結果")
        if trophy in ["虹", "キリン"]:
            st.balloons()
            st.success(f"🏆 RAINBOW/KIRIN DETECTED!! 💰期待値: ￥5,000+ (極ツッパ)")
        elif current_abe >= current_border or current_abe >= 1473:
            val = 3800 if current_abe > 1000 else 1800
            st.success(f"🔥 GO!! 💰期待値: ￥{val}前後 | 天井まで残り{max_ceiling - current_abe}あべし")
            if current_abe >= 1473: st.warning("⚠️ PREMIUM AREA: ATレベル3以上濃厚")
        elif 480 <= current_abe <= 576 or mode_hint == "通常C濃厚":
            st.success(f"⚡ 通常C(576)天井狙い 💰期待値: ￥900前後 | 抜け即ヤメ")
        elif (750 <= current_abe <= 896) or (mode_hint == "256超前兆(通常B期待)" and current_abe >= 500):
            st.success(f"⚡ 通常B(896)天井狙い 💰期待値: ￥1,300前後")
        else:
            st.error(f"❄️ 撤収 💰期待値: MINUS | ボーダー: {current_border}あべし")

        st.markdown("---")
        st.markdown("#### 🛑 当選後のプロトコル")
        if current_abe >= current_border:
            st.warning("🚨 現在は天井狙い中。初当たりまでヤメ厳禁。")
        
        if last_status == "★天撃後(128フォロー)":
            st.info("【最優先】上位AT後：128あべしまで回して判断。")
        elif last_status == "伝承モード":
            st.info("【優先】伝承ループ：天破抜けまで続行。")
        elif st.session_state.vip and diff_coins >= 1000:
            st.warning(f"【有利区間】差枚プラス(+{diff_coins})：128フォローを推奨。")
        else:
            st.info("【通常】高確・前兆確認後、1あべし即ヤメ。")

elif target_machine == "甲鉄城のカバネリ":
    st.subheader("🚂 甲鉄城のカバネリ")
    status = st.selectbox("天井タイプ", ["通常 (1000G)", "設定変更 (650G)", "美馬/駆け抜け (650G)"])
    g_count = st.number_input("現在G数", min_value=0, value=0)
    if st.button("軍師の判断を聞く"):
        is_short = "通常" not in status
        border_k = 270 if is_short else 580
        if g_count >= border_k: st.success("✅ GO!! 💰期待値: ￥2,000+")
        else: st.error("❌ 待機 💰期待値: MINUS")

st.markdown("---")
st.caption("⚠️ **DISCLAIMER**: 期待値は概算です。投資は自己責任で。")
st.caption("© 2026 Protocol ZERO | Developed by Daisuke")
