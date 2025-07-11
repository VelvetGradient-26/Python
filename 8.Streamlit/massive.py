import streamlit as st
import pandas as pd

df = pd.read_csv("worldstats.csv")
print(df)

st.subheader("Metrics")
st.metric(label="Number of Records", value=len(df['Population']))
st.metric(label="Mean population", value=df['Population'].mean())

st.title("World Statistics")
st.table(df)
