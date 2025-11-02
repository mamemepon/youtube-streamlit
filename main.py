import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="お出かけ記録", layout="wide")

# --- CSVファイル設定 ---
CSV_FILE = "shops.csv"

# --- CSV読み込み ---
if os.path.exists(CSV_FILE):
    df = pd.read_csv(CSV_FILE)
else:
    st.error(f"{CSV_FILE} が見つかりません。ファイルを確認してください。")
    st.stop()

st.title("📍お出かけ記録アプリ")




# --- 検索ボックス ---
search_word = st.text_input("🔍 店名またはカテゴリーで検索", "")

if search_word:
    df_filtered = df[df["name"].str.contains(search_word, case=False, na=False) |
                     df["category"].str.contains(search_word, case=False, na=False)]
else:
    df_filtered = df

# --- マッピング ---
if not df_filtered.empty:
    st.map(df_filtered[["lat", "lon"]])
else:
    st.warning("該当するお店がありません。")

st.divider()

# --- 一覧表示 ---
st.subheader("🏠 行ったお店一覧")

if df_filtered.empty:
    st.info("登録されたお店はありません。")
else:
    for _, row in df_filtered.iterrows():
        with st.expander(f"{row['name']} | {row['category']} | ⭐ {row['rating']}"):
            st.write(row["comment"])
            if pd.notna(row["image_path"]) and os.path.exists(row["image_path"]):
                st.image(row["image_path"], use_container_width=True)
            else:
                st.caption("（画像なし）")

