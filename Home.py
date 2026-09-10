import streamlit as st
import functions
import time

# update transaction stem
import transaction



#####
def catch_temps():

    return (st.session_state["tempName"],st.session_state["tempAmount"])

# 

def delete_temps():
    
    del st.session_state["tempName"]
    del st.session_state["tempAmount"]
    
# 



def refresh():

    if "tempName" not in st.session_state:
        st.session_state["tempName"] = st.session_state["InputName"]
    else:
         st.session_state["tempName"] = st.session_state["InputName"]
    
    if "tempAmount" not in st.session_state:
        st.session_state["tempAmount"] = st.session_state["InputAmount"]
    else:
        st.session_state["tempAmount"] = st.session_state["InputAmount"]

    # st.session_state

    st.session_state["InputName"] = ""
    st.session_state["InputAmount"] = "0"

########################################################################
      

# page setter length?
st.set_page_config(page_title="Mini Depositing System", page_icon="💶")

st.title("Mini Deposit System", text_alignment="left")

st.text_input(label="Enter Name", key="InputName")
st.text_input(label="Enter Amount", key="InputAmount")


st.divider()
# workes ony in st.write?
st.write("<h6>ACTIONS</h6>", unsafe_allow_html=True)


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.button("Create Account", key="CreateAccount",on_click=refresh,use_container_width=True)

with col2:
    st.button("Deposit", key="DepositAccount",on_click=refresh,use_container_width=True)

with col3:
    st.button("View Balance", key="ViewBalance",on_click=refresh,use_container_width=True)

with col4:
    st.button("Withdraw", key="WithdrawAccount",on_click=refresh,use_container_width=True)

with col5:
    st.button("Delete Account", key="DeleteAccount",use_container_width=True)
    


# save for the page?
# this with underscore can be use to other pages?

# st.session_state["_input_Name"] = user_name

#--- catch temp ----------#




# rather onClick
if st.session_state["CreateAccount"]:
    
    user_name ,user_amount = catch_temps()
    
    isExisting, isExistingKey = functions.create_account(user_name)
    print(isExisting, isExistingKey)
    if isExisting == "True":
        # popup?
        st.toast(
            f"The account is already existing: {user_name}. Do you mean Deposit?", icon="ℹ️", duration=3)
        delete_temps()
    else:
        # go for checking amount if valid
        st.toast(
            f"Checking the amount for creation: {user_name}", icon="ℹ️", duration=2)
        isAmountValid, returnedAmount = functions.check_amount(user_amount)
        if isAmountValid == "Valid" and type(returnedAmount) is float:
            st.toast("Inserting...", icon="⚠️", duration=4)
            insertSuccess = functions.insert_new_account(
                user_name, returnedAmount)
            if insertSuccess == "Success":
                st.toast(
                    f"Account successfully created: {user_name}, initial deposit {returnedAmount}!", duration=4)
                delete_temps()
            else:
                st.toast(f"Error account creation")
                delete_temps()
        else:
            st.toast(
                f"The amount entered is invalid {returnedAmount}", icon="⚠️", duration=2)
            delete_temps()
########################################################################################################################
elif st.session_state["DepositAccount"]:
    
    user_name ,user_amount = catch_temps()
    
    
    
    isExisting, isExistingKey = functions.create_account(user_name)
    if isExisting == "True":
        # then check amount if valid
        isAmountValid, returnedAmount = functions.check_amount(user_amount)
        if isAmountValid == "Valid":
            # then go insert based also the key
            isSuccessDeposit = transaction.deposit_transaction(
                isExistingKey, returnedAmount)
            if isSuccessDeposit == "Success":
                st.success('Deposit Successful', icon="✅")
                st.balloons()
                time.sleep(1)
                delete_temps()

            else:
                print("Unsuccessful")
                delete_temps()
                

        else:
            st.toast(
                f"The amount entered is invalid {returnedAmount}", icon="⚠️", duration=2)
            delete_temps()
                

    else:
        st.toast(f"This user is not yet registered...{user_name}")
        delete_temps()
########################################################################################################################
elif st.session_state["ViewBalance"]:
    user_name, dummy_holder_amount = catch_temps()
    isExisting, isExistingKey = functions.create_account(user_name)
    if isExisting == "True":
        CurrentBalance = transaction.view_balance(isExistingKey)
        st.success(f"Current Balance for {user_name} is {CurrentBalance}")
        delete_temps()
    else:
        st.warning(f"Unable to view Balance for: {user_name}, un-registered name")
        delete_temps()


########################################################################################################################
    
elif st.session_state["WithdrawAccount"]:
    user_name,user_amount = catch_temps()
    isExisting, isExistingKey = functions.create_account(user_name)
    if isExisting == "True":
         isAmountValid, returnedAmount = functions.check_amount(user_amount)
         if isAmountValid == "Valid":
               isWithdrawSuccess, withdrawMessage, updatedAmount = transaction.withdraw_transaction(isExistingKey,returnedAmount)
               if isWithdrawSuccess == "Success":
                    st.success(f"Withdrawal successful for {user_name}.")
                    st.success(f"Current Balance is: {updatedAmount}.")
                    delete_temps()
               elif isWithdrawSuccess == "Unsuccessful":
                    st.warning(f"Withdrawal {isWithdrawSuccess} for {user_name}.")
                    st.warning(f"{withdrawMessage}")
                    st.warning(f"Current Balance is: {updatedAmount}.")
                    delete_temps()

         else:
            
            st.warning("Unable to withdraw due to amount is invalid")
            delete_temps()
    else:
        st.warning(f"Unable to withdraw due to un-registered {user_name}")
        delete_temps()

#######################################################################################################################
else:
    print("Other buttons to established")


