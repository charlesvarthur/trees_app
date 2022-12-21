#############
# Trees App #
#############

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from bokeh.plotting import figure

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

#Create dbh plotly chart
st.subheader('Plotly Charts')
fig = px.histogram(trees_df['dbh'])
st.plotly_chart(fig)

#Seaborn vis
tree_age_df = trees_df['age'] = (pd.to_datetime('today') - pd.to_datetime(trees_df['date'])). dt.days
st.subheader('Seaborn Chart')
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df['age'])
plt.xlabel('Age (Days)')
st.pyplot(fig_sb)

#Matplotlib vis
st.subheader('Matplotlib Chart')
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df['age'])
plt.xlabel('Age (Days)')
st.pyplot(fig_mpl)

#Bokeh vis
st.subheader('Bokeh Chart')
scatterplot = figure(title = 'Bokeh Scatterplot')
scatterplot.scatter(trees_df['dbh'],trees_df['site order'])
st.bokeh_chart(scatterplot)
scatterplot.xaxis.axis_label="dbh"