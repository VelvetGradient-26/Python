import streamlit as st
import os

st.image(os.path.join(os.getcwd(), "static", "aura.jpg"))

# os.getcwd() fetches the current working directory