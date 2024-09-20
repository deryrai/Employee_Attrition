import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def run():
    st.title('Employee Attrition')

    st.subheader('Exploratory Data Analysis Employee Attrition')

    df = pd.read_csv('train.csv')
    st.dataframe(df)

    st.write(' ## Histogram Persebaran Data Berdasarkan input user')
    option = st.selectbox('Pilih column :' , ('Age', 'Years at Company', 'Monthly Income', 'Number of Promotions', 'Distance from Home', 'Number of Dependents', 'Company Tenure'))
    fig=plt.figure(figsize=(14,5))
    sns.histplot(df[option],bins=20,kde=True)
    st.pyplot(fig)