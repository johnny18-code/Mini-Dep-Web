import streamlit as st
import functions

def refresh():
    # prolly for refresh -- just have a button?
    st.session_state["InputName"] = ""
  

#page setter length?
st.set_page_config(page_title="Mini Depositing System", page_icon="💶")




st.title("Mini Deposit System",text_alignment="left")
st.text_input(label="Enter Name", key="InputName")
st.text_input(label="Enter Amount", key="InputAmount")

st.divider()
st.write("<h6>ACTIONS</h6>", unsafe_allow_html=True) # workes ony in st.write?

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("Create Account", key="CreateAccount",)
   
with col2:
    st.button("Deposit", key="DepositAccount")

with col3:
    st.button("Withdraw", key="WithdrawAccount")

with col4:
    st.button("Delete Account", key="DeleteAccount")

user_name = st.session_state["InputName"]
user_amount = st.session_state["InputAmount"]

#save for the page?
# this with underscore can be use to other pages? 

st.session_state["_input_Name"] = user_name



#rather onClick
if st.session_state["CreateAccount"]:
        isExisting, isExistingKey = functions.create_account(user_name)
        print(isExisting,isExistingKey)
        if isExisting == "True":
            #popup?
            st.toast(f"The account is already existing: {user_name}", icon="ℹ️",duration=1)
        else:
            # go for checking amount if valid
            st.toast(f"Checking the amount for creation: {user_name}", icon="ℹ️",duration=3)
            isAmountValid, returnedAmount = functions.check_amount(user_amount)
            if isAmountValid == "Valid" and type(returnedAmount) is float:
                st.toast("Inserting...", icon="⚠️", duration=4)
                insertSuccess = functions.insert_new_account(user_name,returnedAmount)
                if insertSuccess == "Success":
                    st.toast(f"Account successfully created: {user_name}, initial deposit {returnedAmount}")
                else:
                    st.toast(f"Error account creation")
            else:
                st.toast(f"The amount entered is invalid {returnedAmount}", icon="⚠️",duration=2)

else:
    print("Other buttons to established")
st.session_state