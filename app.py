import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from overall import overall_analysis
from statewise import statewise_analysis
from distwise import distwise_analysis

#========================================================================================
st.set_page_config(layout='wide',page_title="India's Information")
#========================================================================================

df = pd.read_csv("./census_data/final_df.csv")
df['District']=df['District'] +"("+ df['District code'].astype('str')+ ")"
df["Sex_ratio"] = round((df['Female']/df['Male'])*100,2)
df['Illiterate_ratio'] = round((df['Illiterate_Education']/df['Literate_Education'])*100,2)

#=============================== UTILITY ================================================

state = list(df['State'].unique())
state.insert(0,"All India")

district = df['District'].unique().tolist()
district.insert(0,"All Districts")


st.sidebar.title("Analysis-Instruments")
summary = st.sidebar.button("Overall-Analysis")

st.sidebar.title("Detailed-Analysis")
analysis_type = st.sidebar.selectbox("Choose Analysis Type",["Statewise-Analysis","Districtwise-Analysis"])
if analysis_type == "Statewise-Analysis":
    selected_statewise = st.sidebar.selectbox("Select your state", list(df['State'].unique()))
                                              
if analysis_type == "Districtwise-Analysis":
    selected_statewise = st.sidebar.selectbox("Select your state",state)
    if selected_statewise == "All India":
        district_st = df['District'].unique().tolist()
        selected_district = st.sidebar.selectbox("Select your District",district_st)
    elif selected_statewise != "All India":
        df = df[df['State'] == selected_statewise]
        district_st = df['District'].unique().tolist()
        selected_district = st.sidebar.selectbox("Select your District",district_st)

show =st.sidebar.button("Show analysis")








## overall summary section-----------------------------------------------------------------------
if summary:
    df = pd.read_csv("./census_data/final_df.csv")
    df['District']=df['District'] +"("+ df['District code'].astype('str')+ ")"
    df["Sex_ratio"] = round((df['Female']/df['Male'])*100,2)
    df['Illiterate_ratio'] = round((df['Illiterate_Education']/df['Literate_Education'])*100,2)

    overall_analysis(df)

if show:
    if analysis_type == "Statewise-Analysis":
        state_df = df[df['State']==selected_statewise]
        statewise_analysis(state_df, selected_statewise)

    if analysis_type == "Districtwise-Analysis":

        if selected_statewise == "All India":
            dist_df = df[df['District']==selected_district]
            distwise_analysis(dist_df,selected_district)
        elif selected_statewise != "All India" :
            dist_df = df[(df['State']==selected_statewise) & (df['District']==selected_district)]
            distwise_analysis(dist_df,selected_district)


















