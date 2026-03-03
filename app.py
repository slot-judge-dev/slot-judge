import streamlit as st

# --- 1. アプリ基本設定 ---
st.set_page_config(
    page_title="Protocol ZERO | Professional Ultimate", 
    page_icon="logo.jpg",
    layout="centered"
)

# カスタムCSS (視認性最大化)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; font-weight: bold; font-size: 1.1em; border: 2px solid #4A90E2; }
    .stMetric { background-color: #1e2130; padding: 20px; border-radius: 15px; border: 1px solid #333; }
    div.stSelectbox > div { background-color: #1e2130; }
    </style>
    """, unsafe_allow_html=True)

# セッション状態の初期化
if 'vip' not in st.session_state:
    st.session_state.vip = False

# --- 2. サイドバー：認証 & 投資環境詳細設定 ---
with st.sidebar:
    st.title("🔑 VIP STRATEGY ACCESS")
    pwd = st.text_input("認証キーを入力", type="password")
    if pwd == "zero2026":
        st.session_state.vip = True
        st.success("VIP UNLOCKED: 全プロトコル解放済み")
    else:
        st.session_state.vip = False
    
    st.divider()
    st.title("💵 ホール投資環境設定")
    rate = st.selectbox("交換率設定", ["5.0枚 (等価)", "5.6枚", "6.0枚", "その他（非等価）"])
    investment_type = st.radio("現在の投資ステータス", ["貯メダル/持ちメダル", "現金投資（追加投資）"])
    st.info("※現金投資時は換金ギャップを考慮し、自動的に期待値を下方補正、ボーダーを上方修正します。")
    st.divider()
    st.caption("ZERO-PROTOCOL v7.4.3")
    st.caption("© 2026 Protocol ZERO Development Team")

# --- 3. メイン画面レイアウト ---
# ロゴの表示（パスを直接指定）
st.image("logo.jpg", use_column_width=True) 
st.title("🎯 Protocol ZERO")
st.markdown("#### **Strategic Prediction Engine for Professional**")

# 機種選択スイッチ
target_machine = st.selectbox("🎯 ターゲット機種を選択してください", ["北斗の拳 転生2", "甲鉄城のカバネリ"])
st.divider()

if target_machine == "北斗の拳 転生2":
    st.subheader("👊 北斗の拳 転生2：解析モード")
    
    # 入力セクション
    col1, col2 = st.columns(2)
    with col1:
        current_abe = st.number_input("液晶現在のあべし数", min_value=0, max_value=2000, value=0, step=1)
        is_reset = st.toggle("朝イチ (リセット判定：天井1280あべし)")
    with col2:
        last_status = st.selectbox("前回AT終了後の状態", ["通常", "伝承モード示唆", "★上位AT(天撃)終了後"])
        time_slider = st.slider("現在の時刻 (閉店欠損計算用)", 9, 23, 12)

    # モードとフェイク前兆（シャッター）を独立して配置
    col3, col4 = st.columns(2)
    with col3:
        mode_hint = st.selectbox("モード示唆状況", ["示唆なし", "通常C以上濃厚", "天国濃厚"])
    with col4:
        shutter_hint = st.selectbox("フェイク前兆 (シャッター演出等)", ["発生なし", "特定区間で発生(1~64, 129~192等) ※B以上", "256超で前兆発生 ※B以上"])

    trophy = st.selectbox("サミートロフィー (設定判別)", ["なし", "銅", "金", "キリン", "虹"])

    # 💎 VIP専用：メイン画面プロハック
    diff_coins = 0
    border_adj = 0
    if st.session_state.vip:
        st.divider()
        st.markdown("### 💎 VIP PROFESSIONAL HACK")
        v_col1, v_col2 = st.columns(2)
        with v_col1:
            diff_coins = st.slider("有利区間差枚数 (ツラヌキ判定)", -5000, 5000, 0, step=100)
        with v_col2:
            border_adj = st.slider("手動ボーダー微調整 (あべし)", -100, 100, 0, step=10)
        
        # 動的な想定時給算出ロジック
        base_h = 4500 if current_abe > 1000 else (3000 if current_abe > 700 else 1500)
        if investment_type == "現金投資（追加投資）" and rate != "5.0枚 (等価)":
            base_h -= 1200 # 換金ギャップペナルティ
        
        st.metric(label="⏱️ 現状の想定時給予測", value=f"￥{max(0, base_h)}", delta=f"{investment_type} / {rate}")
        st.text_area("💬 AI Bro コンサル (現場の違和感・メモ)", placeholder="例：256抜けで前兆なし、特定キャラ出現など...")

    # --- 4. 判定ロジック実行 ---
    if st.button("軍師の最終判断を仰ぐ (Execute Analysis)"):
        st.divider()
        
        # 内部演算プロトコル
        max_ceiling = 1280 if is_reset else 1536
        base_border = 950 if not is_reset else 700
        
        # 有利区間つらぬき期待度判定
        is_tsuranuki_chance = st.session_state.vip and diff_coins >= 1000

        # 現金投資ペナルティ補正 (ボーダー引き上げ)
        cash_penalty = 150 if investment_type == "現金投資（追加投資）" and rate != "5.0枚 (等価)" else 0
        diff_bonus = -150 if is_tsuranuki_chance else 0
        
        current_border = base_border + border_adj + diff_bonus + cash_penalty
        if time_slider >= 18: current_border += 100 # 夜間補正
        if time_slider >= 21: st.error("🚨 【警告】閉店欠損リスク大！ 取り切れない可能性が極めて高い時間帯です。")

        st.markdown("### 📊 最終投資判断報告")
        
        # 期待値計算補正関数
        def calc_ev(base_ev):
            if investment_type == "現金投資（追加投資）" and rate != "5.0枚 (等価)":
                return int(base_ev * 0.65) # 換金ギャップをより厳しく算出
            return base_ev

        if trophy in ["虹", "キリン"]:
            st.balloons()
            st.success(f"🏆 RAINBOW/KIRIN DETECTED!! 💰推定期待値: ￥5,500+ (設定56確定・全ツッパ)")
        elif current_abe >= current_border or current_abe >= 1473:
            ev = calc_ev(4000 if current_abe > 1000 else 2000)
            tsuranuki_tag = " | 💎 つらぬき期待度:高" if is_tsuranuki_chance else ""
            st.success(f"🔥 【判定：GO】💰推定期待値: ￥{ev}前後{tsuranuki_tag} | 天井まで残り{max_ceiling - current_abe}あべし")
            if current_abe >= 1473: st.warning("⚠️ PREMIUM AREA: ATレベル3以上濃厚恩恵。")
        elif 480 <= current_abe <= 576 or mode_hint == "通常C以上濃厚":
            ev = calc_ev(1000)
            st.success(f"⚡ 【判定：ゾーン狙い】通常C(576あべし)天井ターゲット 💰期待値: ￥{ev}前後")
        elif (750 <= current_abe <= 896) or (shutter_hint != "発生なし" and current_abe >= 550):
            # モードB以上が確定している場合、550あべし付近から通常B天井(896)を狙うロジック
            ev = calc_ev(1400)
            st.success(f"⚡ 【判定：ゾーン狙い】通常B濃厚(896あべし)天井ターゲット 💰期待値: ￥{ev}前後")
        else:
            st.error(f"❄️ 【判定：撤収】💰期待値: マイナス圏内 | 次のボーダーライン: {current_border}あべし")

        # --- 5. ヤメ時プロトコル (聖域) ---
        st.markdown("---")
        st.markdown("#### 🛑 AT当選後のヤメ時プロトコル")
        if current_abe >= current_border:
            st.warning("🚨 現在は「天井期待値」を追っています。AT当選まで絶対にヤメてはいけません。")
        
        if last_status == "★上位AT(天撃)終了後":
            st.info("【最優先：天撃後】128あべしまでの前兆を確認。天国当選率大幅アップにつきヤメ厳禁。")
        elif is_tsuranuki_chance:
            st.warning(f"【重要：つらぬき期待】差枚プラス(+{diff_coins})状態。有利リセットによる恩恵が近いため、128あべしまで回すことを強く推奨。")
        elif last_status == "伝承モード示唆":
            st.info("【優先：伝承ループ】天破の刻がループする限り続行。抜け確認後ヤメ。")
        else:
            st.info("【通常】AT終了後、高確・前兆がないことを確認して1あべし即ヤメ。天国追いは不要。")

elif target_machine == "甲鉄城のカバネリ":
    st.subheader("🚂 甲鉄城のカバネリ：解析モード")
    status = st.selectbox("現在の天井短縮状況", ["通常 (1000G天井)", "設定変更 (650G天井)", "美馬ST後 (650G天井)", "駆け抜け後 (650G天井)"])
    g_count = st.number_input("現在のハマりゲーム数", min_value=0, value=0)
    if st.button("軍師の判断を仰ぐ"):
        is_short = "通常" not in status
        border_k = 280 if is_short else 590
        if g_count >= border_k: st.success(f"✅ 【判定：GO】💰期待値: ￥2,200以上。当たるまで続行。")
        elif 180 <= g_count <= 250: st.info("✅ 【判定：ゾーン狙い】250Gの予兆を確認してください。")
        else: st.error("❌ 【判定：待機】期待値が足りません。")

# 6. 注釈・法的リスク回避
st.markdown("---")
st.caption("⚠️ **DISCLAIMER**: 本アプリが表示する期待値は市場解析データに基づくシミュレーション値です。収益を保証するものではありません。")
st.caption("© 2026 Protocol ZERO | Daisuke Custom Build v7.4.3 Professional Ultimate")
