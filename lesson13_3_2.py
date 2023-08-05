import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

value=st.slider("三角函式",min_value=0,max_value=10)#上方拉棒
t = np.arange(0.,value,0.05)
y1 = np.sin(2 * np.pi * t)
y2 = np.cos(2 * np.pi * t)
figure1 = plt.figure(figsize=(8,4))
axes1 = figure1.add_subplot()
axes1.plot(y1)
axes1.plot(y2)
st.write(figure1)

#st.write()為上傳網頁使用
#在終端機輸入指令,streamlit run 檔名.py
#ctrl+C為中止功能