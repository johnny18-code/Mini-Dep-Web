# main function here :)
import json
from nt import error
import datetime as funcDate

file_path = "accounts.json"


def create_account(nameParm):
    print(nameParm)
    # check if exist -- if not -- go ahead
    with open(file_path, "r") as readFile:
        jsonData = json.load(readFile)

    # loop check
    for key, value in enumerate(jsonData["accounts"]):
        if nameParm == value["name"]:
            # once found then return~ aslso the key?
            return ("True", key)
        else:
            continue

    return ("False", None)

##############################################################################


def check_amount(amountParm):
    try:
        floatingAmount = float(amountParm)
        return ("Valid", floatingAmount)
    except ValueError as e:
        return ("Invalid", amountParm)


##############################################################################
def insert_new_account(nameParm, amountParm):
    
    type_C = "Creation"
    dateNow = funcDate.datetime.now()
    strDate = str(dateNow)

    formattedLoad = {"name": nameParm,
                     "balance": amountParm,
                     "accountStatus": "Active",
                     "transactions": [{
                         "amount": amountParm,
                         "date": strDate,
                         "type": type_C,
                         "status": "successfull"
                     }]}
   
    # open
    with open(file_path, mode="r") as readFile:
        dataLoad = json.load(readFile)
    # append
    dataLoad["accounts"].append(formattedLoad)

    # rewrite
    try: 
        with open(file_path, mode="w") as reWriteFile:
            json.dump(dataLoad,reWriteFile);
        return "Success"
    except error as e:
        print(f"{e}")
        return "Error"
##############################################################################
  


   







