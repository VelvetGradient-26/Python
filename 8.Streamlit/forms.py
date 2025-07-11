import streamlit as st
from datetime import datetime

st.title("User Information Form")

form_values = {
    "name" : None, 
    "age": None, 
    "gender": None, 
    "dob": None, 
    "location": None
}

min_date = datetime(1925, 1, 1)
max_date = datetime.now()

# the code is written inside a with block to stop it from rerunning everytime
with st.form(key="user_info_form"): 
    form_values["name"] = st.text_input("Name: ")
    form_values["age"] = int(st.number_input("Age: "))
    form_values["gender"] = st.selectbox("Gender: ", ["Male", "Female"])
    form_values["dob"] = st.date_input("Date of Birth: ")
    form_values["location"] = st.text_input("City: ")

    # the script is run again only when the submit button is clicked
    submit = st.form_submit_button(label="Submit Form")

    if submit: 
        if not all(form_values.values()): 
            st.warning("Please fill in all of the fields")
        else: 
            st.balloons()
            st.write("### Info")
            for key, value in form_values.items(): 
                st.write(f"{key}:{value}")
            

print() 

for key, value in form_values.items(): 
    print(f"{key}:{value}")




