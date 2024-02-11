import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("electricity-stats")

def get_monthly_fee():
    """
    Ask user to enter monthly fee data
    """
    print("Please enter monthly fee data from electricity company.")
    print("Data should be a two digit number. Example 20.\n")

    # Check so exactly 2 digit number is entered.
    while True:
        data_str = input("Enter your data here:")
        if data_str.isdigit() and len(data_str) == 2:
            print("Data is valid.")
            return int(data_str)
        else:
            print("Invalid input, please enter a 2 digit number.\n")

            
      
def get_electricity_fee():
    """
    Ask user to enter electricity fee data
    """
    print("Please enter electricity fee data from electricity company.")
    print ("Data should be a number with 1 decimal. Example 1.5.\n")

    # Check if float number with 1 decimal is entered.
    while True:
        data_str = input("Enter your data here:")
        try:
            data = float(data_str)
            if data.is_integer():
                print("Invalid input, please enter a number with one decimal place\n")
            elif round(data, 1) == data: #check if number has one decimal
                print("Data is valid.")
                return data 
            else:
                print("Invalid input, please enter a number with one decimal place\n")
        except ValueError:
            print("Invalid input, please enter a number with one decimal place\n")

     

monthly_fee = get_monthly_fee()
electricity_fee = get_electricity_fee()
