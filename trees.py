#############
# Trees App #
#############

import streamlit as st
import pandas as pd

st.title("SF Trees")
st.write('This app analyses the trees in San Francisco using'
           ' a dataset kindly provided by SG DPW')

trees_df = pd.read_csv('https://raw.githubusercontent.com/tylerjrichards/Streamlit-for-Data-Science/main/trees_app/trees.csv')

st.write(trees_df.head())