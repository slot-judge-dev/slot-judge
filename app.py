import streamlit as st

# 1. アプリの基本設定
st.set_page_config(page_title="Hokuto2 AI Advisor", layout="centered")
st.title("👊 北斗転生2：AI投資判断")
st.caption("プロトコル・ゼロ：ヤメ時解析＆VIPチャット統合 v7.2")

# 2. サイドバー：機種解析設定 (v6.2踏襲)
with st.sidebar:
    st.header("⚙️ 機種解析設定")
    limit_a = st.number_input("通常A天井", value=1536)
    limit_reset = st.number_input("朝イチ天井", value=1280)
    limit_b = st.number_input("通常B天井", value=896)
    limit_c = st.number_input("通常C天井", value=576)
    tengoku = st.number_input("天国天井", value=128)
    st.divider()
    base_border_a = st.number_input("通常A ボーダー", value=800)
    base_border_reset = st.number_input("朝イチ ボーダー", value=500)
    base_border_b = st.number_input("通常B ボーダー", value=400)

# 3. メイン画面：現場入力
st.subheader("📍 現在の戦況入力")

col_a, col_b = st.columns(2)
with col_a:
    current_abeshi = st.number_input("【現在のあべし数】", min_value=0, max_value=2000, value=0, step=10)
    is_reset = st.radio("🌅 朝イチ状態", ["いいえ", "はい（リセット濃厚）"])
with col_b:
    current_hour = st.slider("現在時刻（時）", min_value=9, max_value=23, value=12)
    # 🆕 上位AT終了後の項目を追加
    at_end_status = st.selectbox("🏁 前回AT終了後の状態", 
        ["不明 / 見ていない", "即通常ステージ", "伝承モード（天破）示唆あり", "★上位AT(天撃)終了後"])

st.markdown("---")
st.markdown("#### 🚨 特殊条件・前兆示唆")

col1, col2 = st.columns(2)
with col1:
    shutter_zone = st.selectbox("フェイク前兆発生ゾーン", ["なし / 不明", "1〜64", "129〜192", "257〜320", "385〜448", "449〜512"])
    mode_guess = st.selectbox("その他 モード示唆", ["不問", "通常B以上濃厚", "通常C以上濃厚", "天国濃厚"])
    top_lamp = st.selectbox("💡 上部ランプ示唆", ["デフォルト", "青 / 黄", "緑（B以上）", "赤（C以上）", "紫（天国）", "金（設定4以上＋B以上）"])
with col2:
    trophy = st.selectbox("🏆 設定示唆", ["なし", "銅（2以上）", "金（4以上）", "キリン（5以上）", "虹（6濃厚）"])
    investment = st.radio("投資状況", ["持ちメダル", "現金投資"])

# --- AI論理演算 (ロジック統合) ---
target_abeshi = base_border_reset if is_reset == "はい（リセット濃厚）" else base_border_a
mode_status = "通常A（不問）"
current_ceiling = limit_reset if is_reset == "はい（リセット濃厚）" else limit_a
judgment = "WAIT"

# モードB以上判定
if shutter_zone != "なし / 不明" or top_lamp in ["緑（B以上）", "金（設定4以上＋B以上）"] or mode_guess == "通常B以上濃厚":
    target_abeshi = base_border_b
    current_ceiling = limit_b
    mode_status = "通常B以上濃厚"

# 通常C以上判定
if mode_guess == "通常C以上濃厚" or top_lamp == "赤（C以上）":
    target_abeshi = 200
    current_ceiling = limit_c
    mode_status = "通常C以上濃厚"

# 天国判定
if mode_guess == "天国濃厚" or top_lamp == "紫（天国）":
    target_abeshi = 0
    current_ceiling = tengoku
    mode_status = "天国濃厚"

# ヤメ時ナビの動的生成（v7.2 強化）
if at_end_status == "★上位AT(天撃)終了後":
    quit_advice = "🔥【即ヤメ厳禁】上位AT終了後は引き戻し・天国移行率が別格です。128あべしまで絶対にフォロー！"
elif at_end_status == "伝承モード（天破）示唆あり":
    quit_advice = "🌪️ 伝承モード継続の可能性あり。天破ループが抜けるまで続行。"
else:
    quit_advice = "高確・前兆を確認して1あべし即ヤメ。天国追いは期待値マイナスです。"

# 4. タブ分割UI
st.divider()
tab1, tab2 = st.tabs(["🆓 無料版", "💎 VIP専用ハック"])

with tab1:
    raw_ev = (current_abeshi - target_abeshi) * 18
    if st.button("🔥 無料判定", type="primary"):
        st.metric(label="基本期待値", value=f"{max(0, raw_ev):+,} 円")
        st.info(f"🛑 ヤメ時: {quit_advice}")

with tab2:
    password = st.text_input("VIPパスワード", type="password")
    if password == "zero2026":
        st.success("VIPプロトコル起動中")
        diff_coins = st.slider("📊 推定差枚数", -3000, 2400, 0, 100)
        exchange_rate = st.number_input("💸 交換率", 5.0, 6.0, 5.0, 0.1)
        
        # 🆕 VIP限定：ツラヌキ時のヤメ時上書き
        if diff_coins >= 1200 and at_end_status not in ["★上位AT(天撃)終了後", "伝承モード（天破）示唆あり"]:
            quit_advice = "📈 差枚数プラスによる有利リセット濃厚。リセット恩恵（天国優遇）があるため128あべしまで回してください。"

        if st.button("💎 完璧な判定を出す"):
            vip_ev = raw_ev
            if diff_coins >= 1000: vip_ev += (diff_coins - 1000) * 3
            if investment == "現金投資": vip_ev = int(vip_ev * (5.0 / exchange_rate))
            
            st.metric(label="真の期待値", value=f"{max(0, vip_ev):+,} 円")
            st.info(f"🛑 VIPヤメ時指南: {quit_advice}")
            
        st.divider()
        st.markdown("💬 **AI Broに相談（VIPコンサル）**")
        user_msg = st.text_input("例：この展開で追うべき？ 収支報告など")
        if user_msg:
            st.chat_message("assistant").write("論理的に分析します。その状況は...")