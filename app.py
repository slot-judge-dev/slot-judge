import streamlit as st

# --- アプリ基本設定 ---
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
    st.caption("ZERO-PROTOCOL v7.2.5 Final")

# メイン
st.title("🛡️ ZERO-PROTOCOL")
st.subheader("スロット期待値・投資判断軍師")

target_machine = st.selectbox("機種を選択してください", ["北斗の拳 転生2", "甲鉄城のカバネリ"])
st.divider()

if target_machine == "北斗の拳 転生2":
    st.subheader("👊 北斗の拳 転生2 判断モード")
    
    col1, col2 = st.columns(2)
    with col1:
        current_abe = st.number_input("現在のあべし数 (液晶数値)", min_value=0, max_value=2000, value=0)
        is_reset = st.toggle("朝イチ (リセット判定: 天井1280短縮)")
    with col2:
        last_status = st.selectbox("前回AT終了後の状態", ["通常", "伝承モード示唆", "★上位AT(天撃)終了後"])
        time_slider = st.slider("現在時刻", 9, 23, 12)

    col3, col4 = st.columns(2)
    with col3:
        mode_hint = st.selectbox("モード・前兆示唆", ["示唆なし", "通常B以上濃厚(256超前兆発生)", "通常C以上濃厚", "天国濃厚"])
    with col4:
        trophy = st.selectbox("設定確定演出 (トロフィー)", ["なし", "銅", "金", "キリン", "虹"])

    if st.session_state.vip:
        st.divider()
        st.subheader("💎 VIP専用：プロハック")
        diff_coins = st.slider("現在の差枚数", -5000, 5000, 0)
        hourly_pay = 4000 if current_abe > 800 else 1500
        st.info(f"⏱️ 想定時給算出: およそ ￥{hourly_pay}")
        st.text_area("💬 VIPチャット (Broコンサル)", placeholder="現場の迷い、振り返りをご入力ください。")

    if st.button("軍師の最終判断を仰ぐ"):
        st.divider()
        if trophy in ["虹", "キリン"]:
            st.balloons()
            st.success("🏆 RAINBOW/KIRIN GO!! 設定456確定。全ツッパ。")
        else:
            max_ceiling = 1280 if is_reset else 1536
            if current_abe >= 1473: st.warning("🔥 PREMIUM GO!! ATレベル3以上恩恵あり。")
            if time_slider >= 21: st.error("🚨 閉店欠損アラート!! 21時以降は取りきれずリスク大。")

            st.subheader("🛑 ヤメ時ナビ")
            if last_status == "★上位AT(天撃)終了後": st.info("【最優先】天撃後：128あべしまで絶対フォロー！")
            elif last_status == "伝承モード示唆": st.info("【優先】伝承モード：ループ抜けまで続行。")
            elif st.session_state.vip and diff_coins >= 1000: st.info("【VIP限定】差枚プラス：有利リセット恩恵あり128推奨。")
            else: st.info("【通常】前兆確認後、1あべし即ヤメ。")

            st.subheader("📊 モード天井判定")
            if current_abe <= 128: st.success("【天国圏内】128まで。")
            elif 129 <= current_abe <= 576:
                if 480 <= current_abe <= 576 or mode_hint == "通常C以上濃厚": st.success("【判定】通常C天井(576)狙い!!")
                else: st.error("【判定】撤収。")
            elif 577 <= current_abe <= 896:
                if mode_hint == "通常B以上濃厚(256超前兆発生)" or current_abe >= 750: st.success("【判定】通常B天井(896)狙い!!")
                else: st.error("【判定】撤収。")
            else:
                border = 950 if not is_reset else 700
                if time_slider >= 18: border += 100
                if current_abe >= border: st.success(f"【判定】GO!! 最大天井{max_ceiling}狙い。")
                else: st.error(f"【判定】撤収。")

elif target_machine == "甲鉄城のカバネリ":
    st.subheader("🚂 甲鉄城のカバネリ 判断モード")
    status = st.selectbox("現在の状態", ["通常 (1000G天井)", "設定変更 (650G天井)", "美馬後 (650G天井)", "駆け抜け後 (650G天井)"])
    g_count = st.number_input("ハマりゲーム数", min_value=0, value=0)
    if st.button("軍師の判断を聞く"):
        is_short = "通常" not in status
        border_k = 270 if is_short else 580
        if g_count >= border_k: st.success("【判定】GO!! 当たるまで。")
        elif 180 <= g_count <= 250: st.info("【判定】250Gゾーン狙い。")
        else: st.error(f"【判定】待機。")

st.markdown("---")
st.caption("⚠️ **免責事項**: 本AIのボーダーは市場解析データに基づく概算です。自己責任での投資をお願いします。")
st.caption("Powered by ZERO-PROTOCOL / Developed by Daisuke")
