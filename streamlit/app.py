import streamlit as st
import eda
import predict

page = st.sidebar.selectbox('Pilih Halaman:',('EDA','Predict'))

if page == 'EDA':
    eda.run()
else :
    predict.run()



