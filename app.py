import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

#========================================================================================
st.set_page_config(layout='wide')
#========================================================================================

df = pd.read_csv("./census_data/final_df.csv")

#=============================== UTILITY ================================================

state = list(df['State'].unique())
state.insert(0,"Whole India")

#st.title("Detailed Information of INDIA")
st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='centered-title'>Detailed Information of INDIA</h1>", unsafe_allow_html=True)
st.sidebar.title("Choose Your Data")
selected_state = st.sidebar.selectbox("Select your state",state)



