import streamlit as st
import os

st.title("Super simple Title")
st.header("This is a header")
st.subheader('Subheader')

st.markdown("This is _Markdown_")

st.caption("Small text")

st.caption("Large text")

# Render code in a webpage
code_example = '''
def greet(name): 
    return f"Hello, {name}"
'''

st.code(code_example, language="python")

st.divider()