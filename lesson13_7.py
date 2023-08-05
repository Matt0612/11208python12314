#這檔案是上傳到網頁上
import pandas as pd
import streamlit as st

current_weather = pd.read_csv('目前天氣.csv')
st.write('目前台灣天氣')
st.write(current_weather)


#st.write()為上傳網頁使用
#在終端機輸入指令,streamlit run 檔名.py
#ctrl+C為中止功能