import streamlit as st

# --- 1. アプリ基本設定 ---
st.set_page_config(page_title="ZERO-PROTOCOL", layout="centered")

if 'vip' not in st.session_state:
    st.session_state.vip = False

# サイドバー：VIPログイン & ボーダー調整 (要件4)
with st.sidebar:
    st.title("🔑 VIP Access")
    pwd = st.text_input("Password", type="password")
    if pwd == "zero2026":
        st.session_state.vip = True
        st.success("VIP認証成功")
        st.divider()
        st.subheader("⚙️ VIPボーダー微調整")
        # 左側でのボーダー調整スライダーを追加
        border_adj = st.slider("ボーダー調整 (あべし)", -100, 100, 0, step=10)
        st.caption("※マイナスで強気、プラスで慎重に判定します")
    else:
        st.session_state.vip = False
        border_adj = 0
    st.divider()
    st.caption("ZERO-PROTOCOL v7.2.7 Final")

# メイン
st.title("🛡️ ZERO-PROTOCOL")
st.subheader("北斗の拳 転生2：AI軍師")

target_machine = st.selectbox("機種を選択", ["北斗の拳 転生2", "甲鉄城のカバネリ"])
st.divider()

if target_machine == "北斗の拳 転生2":
    col1, col2 = st.columns(2)
    with col1:
        current_abe = st.number_input("現在のあべし数", min_value=0, max_value=2000, value=0)
        is_reset = st.toggle("朝イチ (リセット判定)")
    with col2:
        last_status = st.selectbox("前回AT終了後の状態", ["通常", "伝承モード示唆", "★上位AT(天撃)終了後"])
        time_slider = st.slider("現在時刻", 9, 23, 12)

    mode_hint = st.selectbox("モード・前兆示唆", ["示唆なし", "通常B以上濃厚(256超前兆発生)", "通常C以上濃厚", "天国濃厚"])
    
    if st.button("軍師の最終判断を仰ぐ"):
        st.divider()
        
        # 内部ロジック計算
        max_ceiling = 1280 if is_reset else 1536
        base_border = 950 if not is_reset else 700
        # 時間補正 + VIP調整反映
        current_border = base_border + border_adj
        if time_slider >= 18: current_border += 100

        # --- 攻め時判定 ---
        if current_abe >= current_border:
            st.success(f"🔥 【判定】GO!! 天井まで残り{max_ceiling - current_abe}あべし。当たるまで続行してください。")
            in_ceiling_aim = True
        elif 480 <= current_abe <= 576 or mode_hint == "通常C以上濃厚":
            st.success("【判定】通常C天井(576)狙い!! 抜けたら即ヤメ。")
            in_ceiling_aim = False
        else:
            st.error(f"【判定】撤収。現在のボーダーは{current_border}あべしです。")
            in_ceiling_aim = False

        # --- ヤメ時ナビ (誤解を防ぐための条件分岐) ---
        st.subheader("🛑 ヤメ時ナビ")
        if in_ceiling_aim:
            st.warning("⚠️ 現在は天井狙い中につき、AT当選までヤメ厳禁です。")
        else:
            if last_status == "★上位AT(天撃)終了後":
                st.info("【最優先】天撃後：128あべしまで絶対フォロー！")
            elif last_status == "伝承モード示唆":
                st.info("【優先】伝承モード：ループ抜けまで続行。")
            else:
                st.info("【通常】高確・前兆を確認後、1あべし即ヤメ（天国追いは期待値マイナス）。")

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
