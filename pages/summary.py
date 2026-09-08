import streamlit as st

st.set_page_config(page_title="Summary")
st.write("Summary Page")
try:
    st.session_state["_input_Name"]
except KeyError as e:
    st.write("Unintialize--go back to homePage--Enter Account Name")
    print(f"{e}")
   