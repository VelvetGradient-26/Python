import streamlit as st
import pandas as pd

st.title("Streamlit Elements")

st.subheader("Family")
df = pd.DataFrame({ 
    'Name' : ["Deepak", "Bhanu", "Bhanu", "Ishanika", "Deepika"], 
    'Age' : [19, 20, 6, 3, 2], 
    'Occupation' : ["Engineeer", "Wife", 'Babygirl', "Babygirl", "Babygirl"]
}, index=[1,2,3,4,5])

st.dataframe(df)

# Data Editor section (Editable dataframe)
st.subheader("Data Editor")
editable_df = st.data_editor(df)

# Static Table
st.subheader("Static Table")
st.table(df)

# Metrics Section
st.subheader("Metrics")
st.metric(label="Total rows", value=len(df))
st.metric(label="Average Age", value=round(df["Age"].mean(), 2))