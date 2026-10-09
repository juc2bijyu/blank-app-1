import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import numpy as np
import altair as alt
import pandas as pd

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

# "Say hello"というキャプションのボタンを作成する
if st.button('Say hello'):
    # ボタンが押されればこちらが表示される
    st.write('Why hello there')
else:
    # ボタンが押されなければこちらが表示される
    st.write('Goodbye')




# ランダムなデータを挿入したデータフレームを生成する(3次元の点×200点)
df_random = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
# Altairでチャートを生成する
c = alt.Chart(df_random).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# 生成したチャートを表示
st.write('Chart:', c)

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))

