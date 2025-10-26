import streamlit as st
import pandas as pd
import datetime
import os
from PIL import Image

# CSVファイルの保存場所
DATA_FILE = "trip_data.csv"
IMAGE_DIR = "images"  # 保存用フォルダ

# 初回実行時：フォルダ作成
os.makedirs(IMAGE_DIR, exist_ok=True)

# CSVデータの読み込み（なければ新規作成）
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=["date", "place", "comment", "rating", "latitude", "longitude", "image_path"])


st.title("📖 お出かけ記録アプリ")

st.sidebar.header("新規記録を追加")

# 入力フォーム
with st.sidebar.form("record_form"):
    date = st.date_input("訪問日", datetime.date.today())
    place = st.text_input("場所・店名")
    comment = st.text_area("感想・メモ")
    rating = st.slider("評価（★）", 1, 5, 3)
    latitude = st.number_input("緯度（Latitude）", format="%.6f")
    longitude = st.number_input("経度（Longitude）", format="%.6f")
    image = st.file_uploader("写真をアップロード", type=["jpg", "jpeg", "png"])

    submitted = st.form_submit_button("保存")

if submitted:
    # 画像保存処理
    image_path = ""
    if image:
        image_filename = f"{IMAGE_DIR}/{date}_{place}.jpg".replace(" ", "_")
        with open(image_filename, "wb") as f:
            f.write(image.getbuffer())
        image_path = image_filename

    # CSV用にデータ追加
    new_data = pd.DataFrame([{
        "date": date,
        "place": place,
        "comment": comment,
        "rating": rating,
        "latitude": latitude,
        "longitude": longitude,
        "image_path": image_path
    }])

    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
    st.success("✅ 記録を保存しました！")

# --- データ表示 ---
st.subheader("📚 記録一覧")

if df.empty:
    st.info("まだ記録がありません。左のフォームから追加してください。")
else:
    for i, row in df.iterrows():
        with st.expander(f"{row['date']} - {row['place']}（★{row['rating']}）"):
            st.write(f"🗓 日付：{row['date']}")
            st.write(f"💬 感想：{row['comment']}")
            st.write(f"📍 位置情報：緯度 {row['latitude']} / 経度 {row['longitude']}")
            
            # 画像表示
            if row["image_path"] and os.path.exists(row["image_path"]):
                st.image(row["image_path"], width=400)

            # 地図表示
            if not pd.isna(row["latitude"]) and not pd.isna(row["longitude"]):
                st.map(pd.DataFrame([{"lat": row["latitude"], "lon": row["longitude"]}]))

