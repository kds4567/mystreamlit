import streamlit as st
import numpy as np
import panda as pd

st.title("Map")
df=pd.DataFrame(np.random.randn(500,2)/[50,50]+[37.26,-122.4],columns=['lat','lon'])
st.map(df)

x=st.slider('select a value')
st.write(x,'squared is',x*x)
