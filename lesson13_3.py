##lesson13_3的 py檔案,程式參考C1120805.ipynb   
#py的檔案沒有diplay,需要改成print
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

t = np.arange(0.,1.0,0.05)
st.write(t)
y1 = np.sin(2 * np.pi * t)
y2 = np.cos(2 * np.pi * t)
st.write(y1)
st.write(y2)

figure1 = plt.figure(figsize=(8,4))
axes1 = figure1.add_subplot()
axes1.plot(y1)
axes1.plot(y2)
st.write(figure1)
#st.write()為上傳網頁使用
#在終端機輸入指令,streamlit run 檔名.py