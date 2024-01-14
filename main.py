import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit 超入門")
st.write("Interactive widgets")

# スライダー
condition = st.slider("あなたの今の調子は？",0,100,50)
"あなたの今の調子は",condition,"です。"

# テキストボックス
# text = st.text_input("あなたの趣味を教えてください。")
# "あなたの趣味は",text,"です。"

# セレクトボックス
# option = st.selectbox("あなたが好きな数字を教えてください",list(range(1,11)))
# "あなたの好きな数字は",option,"です。"

# チェックボックスチェック時に表示
# if st.checkbox("Show Image"):
#     img = Image.open("image.png")
#     st.image(img, caption="test", use_column_width=True)



