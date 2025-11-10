import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

def statewise_analysis(df:pd.DataFrame,state):
    st.markdown(f"<h1 class='centered-title'>Analysis of {state} :</h1>", unsafe_allow_html=True)

    fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",color="Literate",size='Population',  zoom=6,size_max=35, mapbox_style="open-street-map",width=700,height=600,hover_name='District',color_continuous_scale="Viridis")

    st.plotly_chart(fig, width='stretch')
    st.markdown("_____________________________")
    #==============================================================================================

    col1, col2  = st.columns(2)
    with col1:
        sort_df = df[['District','Sex_ratio']].sort_values(by='Sex_ratio',ascending=False).head(10)
        st.markdown(f"### **Top 10 Districts in {state} with higher sex-ratio**")

        st.dataframe(sort_df,hide_index=True)
    with col2:
        st.markdown("### **Population of these Districts**")
        df1=df[df['District'].isin(sort_df['District'].tolist())]
        fig = px.bar(data_frame=df1,x='District',y='Population',color='District').update_layout(xaxis={'categoryorder':'total descending'})
        st.plotly_chart(fig, width='stretch')
    st.markdown("_____________________________")
    #================================================================================================

    col1, col2  = st.columns(2)
    with col1:
        sort_df = df[['District','Illiterate_ratio']].sort_values(by='Illiterate_ratio',ascending=True).head(10)
        st.markdown(f"### **Top 10 Districts in {state} with lowest Illiterate-ratio**")

        st.dataframe(sort_df,hide_index=True)
    with col2:
        st.markdown("### **Total Literate People in these districts**")
        df1=df[df['District'].isin(sort_df['District'].tolist())]
        fig = px.bar(data_frame=df1,x='District',y='Literate_Education',color='District').update_layout(xaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, width='stretch')
    st.markdown("_____________________________")
    #======================================================================================================
    col1, col2  = st.columns(2)
    with col1:
        temp_df = df[['Hindus', 'Muslims', 'Christians', 'Sikhs','Buddhists', 'Jains',]].sum().reset_index()
        temp_df.columns = ['Religion', 'Population']
        fig = px.pie(data_frame=temp_df, values='Population',names='Religion',color_discrete_sequence=px.colors.qualitative.Pastel).update_traces(pull=[0.03, 0.03])

        st.markdown(f"### **Distribution of religions in {state}**")
        st.plotly_chart(fig, width='stretch')
    
    with col2:
        st.markdown(f"### **Distribution of Age in {state}**")
        age = df[['Age_Group_0_29', 'Age_Group_30_49', 'Age_Group_50']]
        age.rename(columns={'Age_Group_0_29':'Below 29','Age_Group_30_49':'Between 30-49','Age_Group_50':'More than 50'},inplace=True)
        age = age.sum().reset_index()
        age.columns=['Age_group','Pop']
        fig = px.bar(data_frame=age, x='Age_group',y='Pop',text_auto=True,color='Age_group')

        
        st.plotly_chart(fig, width='stretch')
    st.markdown("_____________________________")

    #==============================================================================================
    st.subheader(f"Household Analysis of {state}:")
    st.markdown("**(Based on top-10 districts having highest population)**")

    top_10_pop = df.sort_values(by=['Population'],ascending=False).head(10)
        

    temp = df.groupby(by=['District'])[['Population','Housholds_with_Electric_Lighting',
    'Households_with_Internet', 'Households_with_Computer',
    'Rural_Households', 'Urban_Households', 'Households','Households_with_Television', 'Ownership_Owned_Households',
    'Ownership_Rented_Households']].sum().reset_index()
    
    temp.rename(columns={"Housholds_with_Electric_Lighting":"With Electrcity",
                    "Households_with_Internet":"With Internet",
                    "Households_with_Computer":"With Computers",
                    "Rural_Households": "Rural Households",
                    "Urban_Households":"Urban Households",	
                    "Households":"Total Households",
                    "Households_with_Television":"With Television",
                    "Ownership_Owned_Households":"Owned Households",
                    "Ownership_Rented_Households":"Rented Households"},inplace=True)
    
    temp_head = temp[temp['District'].isin(top_10_pop['District'].tolist())]
    temp_head = temp_head.sort_values(by=['Population'],ascending=False)

    

    st.markdown("#### A) Distribution of Electricity & Television")

    
    fig1 = px.bar(data_frame=temp_head,x='District',y=['With Electrcity','With Television'],barmode='group',text_auto=True,hover_data='Population'
    ,labels={
        'variable':'Facility',
        'value':'Total households'
    })
    # makes bars thicker
    fig1.update_layout(
        bargap=0.2,         
        bargroupgap=0.05,    
        width=1300,          
        height=600,          
        xaxis_tickangle=40   
    )
    st.plotly_chart(fig1, width='stretch')

    #-------------------------------------------------------------
    
    st.markdown("#### B) Distribution of Internet & Computers")
    fig2 = px.bar(data_frame=temp_head,x='District',y=['With Internet','With Computers'],barmode='group',text_auto=True,hover_data='Population'
    ,labels={
        'variable':'Facility',
        'value':'Total households'
    },color_discrete_sequence=['pink','orange'])
    # makes bars thicker
    fig2.update_layout(
        bargap=0.2,         
        bargroupgap=0.05,    
        width=1300,          
        height=600,          
        xaxis_tickangle=40   
    )
    st.plotly_chart(fig2, width='stretch')  # width='content'
    st.markdown("_____________________________")
    #==================================================================================================
    
    col1, col2,col3,col4 = st.columns(4)
    with col1:
        st.markdown("**Top-5 districts having electricity:**")
        temp_elec = df[['District','Housholds_with_Electric_Lighting']].sort_values(by='Housholds_with_Electric_Lighting',ascending=False).head(5)

        temp_elec.rename(columns={
            'Housholds_with_Electric_Lighting':"Total Households"
        },inplace=True)

        st.dataframe(temp_elec,hide_index=True)

    with col2:
        st.markdown("**Top-5 districts used Television most:**")
        temp_elec = df[['District','Households_with_Television']].sort_values(by='Households_with_Television',ascending=False).head(5)

        temp_elec.rename(columns={
            'Households_with_Television':"Total Households"
        },inplace=True)

        st.dataframe(temp_elec,hide_index=True)

    with col3:
        st.markdown("**Top-5 districts having Internet most:**")
        temp_elec = df[['District','Households_with_Internet']].sort_values(by='Households_with_Internet',ascending=False).head(5)

        temp_elec.rename(columns={
            'Households_with_Internet':"Total Households"
        },inplace=True)

        st.dataframe(temp_elec,hide_index=True)

    with col4:
        st.markdown("**Top-5 districts used Computer most:**")
        temp_elec = df[['District','Households_with_Computer']].sort_values(by='Households_with_Computer',ascending=False).head(5)

        temp_elec.rename(columns={
            'Households_with_Computer':"Total Households"
        },inplace=True)

        st.dataframe(temp_elec,hide_index=True)
    st.markdown("_____________________________")

    col1,col2,col3=st.columns(3)
    
    with col1:
        st.markdown(f"#### **Pie-chart of Rural & Urban in {state}**")
        rural_urb = df[['Rural_Households','Urban_Households']].sum().reset_index()
        rural_urb.columns = ['Type','Pop']
        fig = px.pie(data_frame=rural_urb, values='Pop',names='Type').update_traces(pull=[0.03, 0.03])
        st.plotly_chart(fig, width='stretch')
    
    with col2:
        st.markdown(f"#### **top-5 districts with most Rural Households:**")
        rul_df = df[['District','Rural_Households']].sort_values(by='Rural_Households',ascending=False).head(5)
        fig = px.bar(data_frame=rul_df,x='District',y='Rural_Households', color_discrete_sequence=['#90be6d'])
        st.plotly_chart(fig, width='stretch')


    with col3:
        st.markdown(f"#### **top-5 districts with most Urban Households:**")
        rul_df = df[['District','Urban_Households']].sort_values(by='Urban_Households',ascending=False).head(5)
        fig = px.bar(data_frame=rul_df,x='District',y='Urban_Households', color_discrete_sequence=['#83c5be'])
        st.plotly_chart(fig, width='stretch')

    st.markdown("_____________________________")

    col1,col2,col3=st.columns(3)

    with col1:
        st.markdown(f"#### **top-5 districts with most Owned Households:**")
        rul_df = df[['District','Ownership_Owned_Households']].sort_values(by='Ownership_Owned_Households',ascending=False).head(5)
        fig = px.bar(data_frame=rul_df,x='District',y='Ownership_Owned_Households', color_discrete_sequence=['#83c5be'])
        st.plotly_chart(fig, width='stretch')

    with col2:
        st.markdown(f"#### **top-5 districts with most Rented Households:**")
        rul_df = df[['District','Ownership_Rented_Households']].sort_values(by='Ownership_Rented_Households',ascending=False).head(5)
        fig = px.bar(data_frame=rul_df,x='District',y='Ownership_Rented_Households', color_discrete_sequence=['#168aad'])
        st.plotly_chart(fig, width='stretch')



    with col3:
        st.markdown(f"#### **Pie-chart of Owned & Rented in {state}:**")
        rural_urb = df[['Ownership_Owned_Households','Ownership_Rented_Households']]
        rural_urb.rename(columns={'Ownership_Owned_Households':'Owned Households','Ownership_Rented_Households':'Rented Household'},inplace=True)
        rural_urb = rural_urb.sum().reset_index()
        rural_urb.columns = ['Type','Pop']
        fig = px.pie(data_frame=rural_urb, values='Pop',names='Type',color_discrete_sequence=['#7678ed','green']).update_traces(pull=[0.03, 0.03])
        st.plotly_chart(fig, width='stretch')

    st.markdown("_____________________________")



    




