import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("最初の一歩")



JST = ZoneInfo("Asia/Tokyo")
now = datetime.now(JST)

# 今日の日付に、判断したい時刻を組み合わせた datetime を作る
start = now.replace(hour=9)
end = now.replace(hour=17)

if start <= now <= end:
    st.write("現在、勤務時間中です")
else :
    st.write("現在オフです。自由時間を楽しみましょう")
