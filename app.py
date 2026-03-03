import streamlit as st

# --- 1. アプリ基本設定 ---
st.set_page_config(page_title="ZERO-PROTOCOL", layout="centered")

if 'vip' not in st.session_state:
    st.session_state.vip = False

# サイドバー：VIPログイン
with st.sidebar:
    st.title("🔑 VIP Access")
    pwd = st.text_input("Password", type="password")
    if pwd == "zero2026":
        st.session_state.vip = True
        st.success("VIP認証成功: 全機能解放")
    else:
        st.session_state.vip = False
    st.divider()
    st.caption("ZERO-PROTOCOL v7.2.6 Final")

# メイン
st.title("🛡️ ZERO-PROTOCOL")
st.subheader("👊 北斗の拳 転生の章2：AI投資判断軍師")

# 機種選択（カバネリ統合）
target_machine = st.selectbox("機種を選択してください", ["北斗の拳 転生2", "甲鉄城のカバネリ"])
st.divider()

if target_machine == "北斗の拳 転生2":
    # 📍 入力セクション
    col1, col2 = st.columns(2)
    with col1:
        current_abe = st.number_input("現在のあべし数 (液晶数値)", min_value=0, max_value=2000, value=0)
        is_reset = st.toggle("朝イチ (リセット判定)")
    with col2:
        last_status = st.selectbox("前回AT終了後の状態", ["通常", "伝承モード示唆", "★上位AT(天撃)終了後"])
        time_slider = st.slider("現在時刻", 9, 23, 12)

    col3, col4 = st.columns(2)
    with col3:
        mode_hint = st.selectbox("モード・前兆示唆", ["示唆なし", "通常B以上濃厚(256超前兆発生)", "通常C以上濃厚", "天国濃厚"])
    with col4:
        trophy = st.selectbox("設定確定演出", ["なし", "銅", "金", "キリン", "虹"])

    # VIP機能
    if st.session_state.vip:
        st.divider()
        st.subheader("💎 VIP専用：プロハック")
        diff_coins = st.slider("現在の差枚数", -5000, 5000, 0)
        st.info(f"⏱️ 想定時給算出: ￥{4500 if current_abe > 1000 else 1500}")
        st.text_area("💬 VIPチャット (Broコンサル)", placeholder="現場の状況を入力...")

    if st.button("軍師の最終判断を仰ぐ"):
        st.divider()
        
        # ロジック演算
        max_ceiling = 1280 if is_reset else 1536
        border = 950 if not is_reset else 700
        if time_slider >= 18: border += 100

        # 判断表示
        if trophy in ["虹", "キリン"]:
            st.balloons()
            st.success("🏆 RAINBOW/KIRIN GO!! 設定456確定。全ツッパ。")
        elif current_abe >= border or current_abe >= 1473:
            st.success(f"🔥 【判定】GO!! 天井まで残り{max_ceiling - current_abe}あべし。当たるまで続行。")
            if current_abe >= 1473: st.warning("⚠️ PREMIUM GO!! ATレベル3以上恩恵あり。")
        elif 480 <= current_abe <= 576 or mode_hint == "通常C以上濃厚":
            st.success("【判定】通常C天井(576)狙い!! 256抜け前兆等から判断。")
        elif (750 <= current_abe <= 896) or (mode_hint == "通常B以上濃厚(256超前兆発生)" and current_abe >= 500):
            st.success("【判定】通常B天井(896)狙い!! 当たるまで全ツッパ。")
        else:
            st.error(f"【判定】撤収。現在のボーダーラインは{border}あべしです。")

        # 🛑 ヤメ時ナビ（v7.2.6 改良版：天井狙い時は非表示）
        st.subheader("🛑 ヤメ時ナビ（※当選後の動き）")
        if last_status == "★上位AT(天撃)終了後":
            st.info("【最優先】天撃後：128あべしまで絶対フォロー！")
        elif last_status == "伝承モード示唆":
            st.info("【優先】伝承モード：ループ抜けまで続行。")
        elif current_abe >= border:
            st.warning("【特殊】現在は天井狙い中。当選するまでヤメ厳禁。")
        else:
            st.info("【通常】前兆確認後、1あべし即ヤメ。天国追いは不要。")

elif target_machine == "甲鉄城のカバネリ":
    st.subheader("🚂 甲鉄城のカバネリ 判断モード")
    status = st.selectbox("状態", ["通常 (1000G)", "設定変更 (650G)", "美馬後 (650G)", "駆け抜け後 (650G)"])
    g_count = st.number_input("ゲーム数", min_value=0, value=0)
    if st.button("軍師の判断を聞く"):
        is_short = "通常" not in status
        border_k = 270 if is_short else 580
        if g_count >= border_k: st.success("【判定】GO!! 当たるまで。")
        else: st.error("【判定】待機。")

st.markdown("---")
st.caption("⚠️ **免責事項**: 市場データに基づく概算です。自己責任で投資をお願いします。")
st.caption("Powered by ZERO-PROTOCOL / Developed by Daisuke")
