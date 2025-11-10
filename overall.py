import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st




def overall_analysis(df):


    st.markdown("<h1 class='centered-title'>Summary of India</h1>", unsafe_allow_html=True)       
    fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",color="Literate",size='Population',  zoom=4,size_max=35, mapbox_style="carto-positron",width=1200,height=700,hover_name='District',color_continuous_scale="Viridis")

    st.plotly_chart(fig, width='stretch')
    #_________________________________________________________________________________________
    col1, col2  = st.columns(2)
    with col1:
        sort_df = df[['State','District','Sex_ratio']].sort_values(by='Sex_ratio',ascending=False).head(10)
        st.markdown("### **Top 10 Districts with higher sex-ratio**")

        st.dataframe(sort_df,hide_index=True)
    with col2:
        #st.markdown("### **Visualization with bar-graph**")
        fig = px.bar(data_frame=sort_df,x='District',y='Sex_ratio',color='State').update_layout(xaxis={'categoryorder':'total descending'})
        st.plotly_chart(fig, width='stretch')

    #_________________________________________________________________________________________
    col1, col2  = st.columns(2)
    with col1:
        sort_df = df[['State','District','Illiterate_ratio']].sort_values(by='Illiterate_ratio',ascending=True).head(10)
        st.markdown("### **Top 10 Districts with lowest Illiterate-ratio**")

        st.dataframe(sort_df,hide_index=True)
    with col2:
        #st.markdown("### **Visualization with bar-graph**")
        fig = px.bar(data_frame=sort_df,x='District',y='Illiterate_ratio',color='State').update_layout(xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, width='stretch')
    #_________________________________________________________________________________________
    col1, col2  = st.columns(2)
    with col1:
        temp_df = df[['Hindus', 'Muslims', 'Christians', 'Sikhs','Buddhists', 'Jains',]].sum().reset_index()
        temp_df.columns = ['Religion', 'Population']
        fig = px.pie(data_frame=temp_df, values='Population',names='Religion',color_discrete_sequence=px.colors.qualitative.Pastel)

        st.markdown("### **Distribution of religions all over India**")
        st.plotly_chart(fig, width='stretch')
    
    with col2:
        age = df[['Age_Group_0_29', 'Age_Group_30_49', 'Age_Group_50']]
        age.rename(columns={'Age_Group_0_29':'Below 29','Age_Group_30_49':'Between 30-49','Age_Group_50':'More than 50'},inplace=True)
        age = age.sum().reset_index()
        age.columns=['Age_group','Pop']
        fig = px.bar(data_frame=age, x='Age_group',y='Pop',color_discrete_sequence=['green'],text_auto=True,color='Age_group')

        st.markdown("### **Distribution of Age-group**")
        st.plotly_chart(fig, width='stretch')
    