#這檔案是上傳到網頁上
import pandas as pd
import streamlit as st

current_weather = pd.red_csv('目前天氣.csv')
st.write('目前泰灣天氣')
st.write(current_weather)