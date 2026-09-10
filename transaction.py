import json
import datetime as funcDate
from turtle import update

file_path = "accounts.json"


# this will insert -- apend the deposit transaction to transaction key:
#
def deposit_transaction(keyParm, keyAmount):
    type_C = "Deposit"
    dateNow = funcDate.datetime.now()
    strDate = str(dateNow)
    # format:
    transactionLoad = {
        "amount": keyAmount,
        "date": strDate,
        "type": type_C,
        "status": "successfull"
    }
    with open(file_path, "r") as readFile:
        readData = json.load(readFile)
    currentBalance = readData["accounts"][keyParm]["balance"]
    updatedBalance = currentBalance + keyAmount

    # balance updated
    readData["accounts"][keyParm]["balance"] = updatedBalance

    # log the transaction
    readData["accounts"][keyParm]["transactions"].append(transactionLoad)

    # re-write
    with open(file_path, mode="w") as reWriteFile:
        json.dump(readData, reWriteFile)

    return "Success"

# deposit_transaction(3,33)


############################################################################
def withdraw_transaction(keyParm, keyAmount):
    print("Withdraw function....")
    type_C = "Withdraw"
    dateNow = funcDate.datetime.now()
    strDate = str(dateNow)
# format:
    transactionLoad = {
        "amount": keyAmount,
        "date": strDate,
        "type": type_C,
        "status": "successfull"
    }

    # read file
    with open(file_path, mode="r") as readFile:
        dataLoad = json.load(readFile)
    print(dataLoad["accounts"][keyParm], "amount: ", keyAmount)
    # pull current balance
    currentBalance = dataLoad["accounts"][keyParm]["balance"]

    if (currentBalance - keyAmount) < 0:
        return ("Unsuccessful", "Current Balance not enough", currentBalance)
    else:
        updatedBalance = currentBalance - keyAmount
        dataLoad["accounts"][keyParm]["balance"] = updatedBalance

        # then append to transaction segment~ :)
        dataLoad["accounts"][keyParm]["transactions"].append(transactionLoad)
        with open(file_path, mode="w") as reWriteFile:
            json.dump(dataLoad, reWriteFile)
        return ("Success", "Balance Updated", updatedBalance)


# withdraw_transaction(0,1000)
############################################################################
# view Balance
def view_balance(keyParm):
    with open(file_path, "r") as readFile:
        dataLoad = json.load(readFile)

    viewBalance = dataLoad["accounts"][keyParm]["balance"]

    return viewBalance


# print(view_balance(2))
