#############
# Trees App #
#############

import streamlit as st
import pandas as pd
import numpy as np

#Title and opening paragraph
st.title("SF Trees")
st.write('This app analyses the trees in San Francisco using'
           ' a dataset kindly provided by SG DPW')

#Import dataset
trees_df = pd.read_csv('https://raw.githubusercontent.com/tylerjrichards/Streamlit-for-Data-Science/main/trees_app/trees.csv')

#st.write(trees_df.head())

df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']
df_dbh_grouped['new_col'] = np.random.randn(len(df_dbh_grouped)) * 500


#Visualise easy to create graphs for simple data
st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)

#Visualise map data with st.map
map_df = trees_df.dropna(subset=['longitude','latitude'])
map_df = map_df.sample(n=1000)
st.map(map_df)
