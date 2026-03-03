import streamlit as st

# --- 1. アプリ基本設定 ---
st.set_page_config(page_title="ZERO-PROTOCOL", layout="centered")

# VIP状態の保持
if 'vip' not in st.session_state:
    st.session_state.vip = False

# サイドバー：パスワード入力のみ（ここで zero2026 と入力）
with st.sidebar:
    st.title("🔑 VIP Access")
    pwd = st.text_input("Password (zero2026)", type="password")
    if pwd == "zero2026":
        st.session_state.vip = True
        st.success("VIP認証成功：プロハック全解放")
    else:
        st.session_state.vip = False
    st.divider()
    st.caption("ZERO-PROTOCOL v7.3.1")

# メインコンテンツ
st.title("🛡️ ZERO-PROTOCOL")
st.subheader("👊 北斗の拳 転生2：AI軍師")

target_machine = st.selectbox("機種を選択してください", ["北斗の拳 転生2", "甲鉄城のカバネリ"])
st.divider()

if target_machine == "北斗の拳 転生2":
    # --- 📍 現場最速入力 ---
    st.subheader("📍 現場最速入力")
    col1, col2 = st.columns(2)
    with col1:
        current_abe = st.number_input("現在のあべし数 (液晶数値)", min_value=0, max_value=2000, value=0)
        is_reset = st.toggle("朝イチ (設定変更/リセット判定)")
    with col2:
        last_status = st.selectbox("前回AT終了後の状態", ["通常", "伝承モード示唆", "★上位AT(天撃)終了後"])
        time_slider = st.slider("現在時刻", 9, 23, 12)

    mode_hint = st.selectbox("モード・前兆示唆", ["示唆なし", "通常B以上濃厚(256超前兆発生)", "通常C以上濃厚", "天国濃厚"])
    trophy = st.selectbox("設定確定演出 (トロフィー)", ["なし", "銅", "金", "キリン", "虹"])

    # --- 💎 VIP専用：メイン画面に直接表示 (差枚・時給・チャット) ---
    diff_coins = 0
    border_adj = 0
    if st.session_state.vip:
        st.divider()
        st.subheader("💎 VIP専用：プロハック")
        v_col1, v_col2 = st.columns(2)
        with v_col1:
            diff_coins = st.slider("現在の差枚数 (有利区間ツラヌキ判定)", -5000, 5000, 0, step=100)
        with v_col2:
            border_adj = st.slider("ボーダー微調整 (あべし)", -100, 100, 0, step=10)
        
        # ⏱️ 想定時給の表示
        h_pay = 4000 if current_abe > 800 else 1500
        st.info(f"⏱️ **想定時給算出**: およそ ￥{h_pay} (残りあべし数から換算)")
        
        # 💬 VIPチャット
        st.text_area("💬 VIPチャット (Broコンサル)", placeholder="現場の迷いを入力してください。AI軍師が回答します。")

    # --- 判定実行 ---
    if st.button("軍師の最終判断を仰ぐ"):
        st.divider()
        
        # 内部演算ロジック
        max_ceiling = 1280 if is_reset else 1536
        base_border = 950 if not is_reset else 700
        
        # 差枚数によるボーダー優遇
        diff_bonus = -150 if st.session_state.vip and diff_coins >= 1000 else 0
        current_border = base_border + border_adj + diff_bonus
        if time_slider >= 18: current_border += 100

        # --- 判断セクション (💰期待値を金額で表示) ---
        st.subheader("📊 投資判断")
        
        if trophy in ["虹", "キリン"]:
            st.balloons()
            st.success(f"🏆 RAINBOW/KIRIN GO!! 💰期待値: ￥5,000 Over (全ツッパ指示)")
        elif current_abe >= current_border or current_abe >= 1473:
            val = 3800 if current_abe > 1000 else 1800
            st.success(f"🔥 【判定】GO!! 💰期待値: ￥{val}前後。天井まで残り{max_ceiling - current_abe}あべし。")
            if current_abe >= 1473: st.warning("⚠️ PREMIUM GO!! ATレベル3以上確定恩恵。")
        elif 480 <= current_abe <= 576 or mode_hint == "通常C以上濃厚":
            st.success(f"【判定】通常C天井(576)狙い!! 💰期待値: ￥900前後。抜ければ即ヤメ。")
        elif (750 <= current_abe <= 896) or (mode_hint == "通常B以上濃厚(256超前兆発生)" and current_abe >= 500):
            st.success(f"【判定】通常B天井(896)狙い!! 💰期待値: ￥1,300前後。")
        else:
            st.error(f"【判定】撤収。💰期待値: マイナス。現在のボーダーは{current_border}あべしです。")

        # --- ヤメ時ナビ (天井狙い保護ロジック) ---
        st.subheader("🛑 当選後のヤメ時")
        if current_abe >= current_border:
            st.warning("⚠️ 現在は天井狙い中につき、AT当選までヤメ厳禁。")
        
        if last_status == "★上位AT(天撃)終了後":
            st.info("【最優先】上位AT後：128あべしまで絶対にフォロー！")
        elif last_status == "伝承モード示唆":
            st.info("【優先】伝承モード：ループが抜けるまで続行。")
        elif st.session_state.vip and diff_coins >= 1000:
            st.warning(f"【VIP限定】差枚プラス(+{diff_coins})：有利リセット恩恵あり。128フォロー推奨。")
        else:
            st.info("【通常】高確・前兆確認後、1あべし即ヤメ（天国追いは不要）。")

elif target_machine == "甲鉄城のカバネリ":
    st.subheader("🚂 甲鉄城のカバネリ 判断モード")
    status = st.selectbox("現在の状態", ["通常 (1000G)", "設定変更 (650G)", "美馬後 (650G)", "駆け抜け後 (650G)"])
    g_count = st.number_input("ゲーム数", min_value=0, value=0)
    if st.button("軍師の判断を聞く"):
        is_short = "通常" not in status
        border_k = 270 if is_short else 580
        if g_count >= border_k: st.success("【判定】GO!! 💰期待値: ￥2,000 Over。")
        else: st.error("【判定】待機。💰期待値: マイナス。")

# --- 注釈・免責事項 ---
st.markdown("---")
st.caption("⚠️ **免責事項**: 市場データに基づく概算です。自己責任で投資をお願いします。")
st.caption("Powered by ZERO-PROTOCOL / Developed by Daisuke")
