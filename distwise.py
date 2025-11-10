import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

def distwise_analysis(df:pd.DataFrame,dist):
    st.markdown(f"<h1 class='centered-title'>Analysis of {dist} :</h1>", unsafe_allow_html=True)

    fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",color="Literate",size='Population',  zoom=5,size_max=25, mapbox_style="open-street-map",width=500,height=400,hover_name='District',color_continuous_scale="Viridis")

    st.plotly_chart(fig,width='stretch')
    st.markdown("_____________________________")
    #==============================================================================================

    col1, col2  = st.columns(2)
    with col1:
        st.markdown("## **Male & Female Population:**")
        male_fe = df[['Male','Female']].sum().reset_index()
        male_fe.columns = ['Sex','Pop']
        fig = px.pie(data_frame=male_fe,values='Pop',names='Sex',color_discrete_sequence=['#4cc9f0','#e0aaff']).update_traces(pull=[0.02, 0.02])
        st.plotly_chart(fig, width='stretch') 

    with col2:
        st.markdown("## **Male & Female Workers:**")
        male_fe = df[['Male_Workers','Female_Workers']].sum().reset_index()
        male_fe.columns = ['Workers','Pop']
        fig = px.pie(data_frame=male_fe,values='Pop',names='Workers',color_discrete_sequence=["#339e61","#d24b86"]).update_traces(pull=[0.02, 0.02])
        st.plotly_chart(fig, width='stretch')

    st.markdown("_____________________________")
    #================================================================================================
    st.markdown(f"## **Education-Distribution in {dist}:**")
    temp = df[['Below_Primary_Education', 'Primary_Education', 'Middle_Education',
       'Secondary_Education', 'Higher_Education', 'Graduate_Education',
       'Other_Education']].rename(columns={
           'Below_Primary_Education':"Below Primary", 
           'Primary_Education':"Primary", 
           'Middle_Education':"Middle Education",
       'Secondary_Education':"Secondary Education", 
       'Higher_Education':"Higher Education", 
       'Graduate_Education':"Graduate Education",
       'Other_Education':"Other Education"
       }).melt()
    
    fig = px.histogram(data_frame=temp,x='variable',y='value',text_auto=True,labels={'variable':'Education Type',"value":"Population"},color='variable')
    st.plotly_chart(fig, width='stretch')
    st.markdown("_____________________________")
    #================================================================================================
    st.markdown(f"## **Household-size Distribution in {dist}:**")
    size = df[['Household_size_1_person_Households',
       'Household_size_2_persons_Households', 'Household_size_1_to_2_persons',
       'Household_size_3_persons_Households',
       'Household_size_3_to_5_persons_Households',
       'Household_size_4_persons_Households',
       'Household_size_5_persons_Households',
       'Household_size_6_8_persons_Households',
       'Household_size_9_persons_and_above_Households']].rename(columns={
        'Household_size_1_person_Households':"Size-1",
       'Household_size_2_persons_Households':"Size-2", 'Household_size_1_to_2_persons':"Size-(1-2)",
       'Household_size_3_persons_Households':"Size-3",
       'Household_size_3_to_5_persons_Households':"Size-(3-5)",
       'Household_size_4_persons_Households':"Size-4",
       'Household_size_5_persons_Households':"Size-5",
       'Household_size_6_8_persons_Households':"Size-(6-8)",
       'Household_size_9_persons_and_above_Households':"Size-9+"
       }).melt()
    
    size.rename(columns={'variable':'Size of Household','value':'Population'},inplace=True)
    fig = px.bar(data_frame=size, x='Size of Household',y='Population',text_auto=True,color='Size of Household')
    st.plotly_chart(fig, width='stretch')

    st.markdown("_____________________________")
    #================================================================================================

    