import streamlit as st

pressed = st.button("Press me")
print("First: ", pressed)

pressed2 = st.button("Second Button")
print("Second: ", pressed2)

# whenever there is a change streamlit reruns the entire python script from top to bottom
# even for actions in the webpage like pressing a button