import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time 

st.title("Streamlit 超入門")
st.write("プログレスバーの表示")

"start!!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!!!"

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.expander("問い合わせ")
expander1.write("問い合わせ回答１")
expander2 = st.expander("問い合わせ")
expander2.write("問い合わせ回答２")
expander3 = st.expander("問い合わせ")
expander3.write("問い合わせ回答３")
expander4 = st.expander("問い合わせ")
expander4.write("問い合わせ回答４")

# # テキストボックス
# text = st.text_input("あなたの趣味を教えてください。")
# "あなたの趣味は",text,"です。"
# # スライダー
# condition = st.slider("あなたの今の調子は？",0,100,50)
# "あなたの今の調子は",condition,"です。"

# "あなたの趣味:",text
# "コンディション:",condition

# セレクトボックス
# option = st.selectbox("あなたが好きな数字を教えてください",list(range(1,11)))
# "あなたの好きな数字は",option,"です。"

# チェックボックスチェック時に表示
# if st.checkbox("Show Image"):
#     img = Image.open("image.png")
#     st.image(img, caption="test", use_column_width=True)



