import streamlit as st
import numpy as np
import pandas as pd
import sys
import os

# from sklearn import datasets


def app():
    st.title('Data Overview')

    st.header('Table Description')
    field_df = pd.read_excel("../data/Field Descriptions.xlsx")
    st.write(field_df, width=1200)

    st.header('Here is sample data from the table')
    challenge_data_df = pd.read_csv(
        "../data/Week1_challenge_data_source(CSV).csv")
    st.write(challenge_data_df.head(10))

    st.header('Here is sample data from the cleaned table')
    clean_data_df = pd.read_csv("../data/clean_data.csv")
    st.write(clean_data_df.head(10))

    st.header('Detailed Information On the Dataset')
    st.markdown(
        '''
    The table below shows that:
    - Count of unique values in each columns
    - Persentage of unique values in each columns
    - Count of None values in each columns
    - Persentage of None values in each columns
    - Min, Max, and Median values in each columns
    ''')
    st.write(clean_data_df['Handset Type'].value_counts())
    st.bar_chart(
        clean_data_df['Handset Type'].value_counts().reset_index().head(10))

    # overview = DfOverview(df)
    # dfOverview = overview.getOverview()
    # st.write(dfOverview)

    # st.header('Outliers in the data')
    # df = loadPreprocessedData()
    # numeric_df = df[NUMERIC_COLUMNS].copy()
