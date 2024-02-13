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
print(SHEET.worksheets())

def get_monthly_fee():
    """
    Ask user to enter monthly fee data collected from the electricity company.
    Run a while loop to get the correct data, 2 digit number.
    """
    print("Please enter monthly fee data from electricity company.")
    print("Data should be a two digit number. Example 20.\n")

    # Check so exactly 2 digit number is entered.
    while True:
        data_str = input("Enter your data here:")
        if data_str.isdigit() and len(data_str) == 2:
            print("Data is valid.\n")
            return int(data_str)
        else:
            print("Invalid input, please enter a 2 digit number.\n")

            
      
def get_electricity_fee():
    """
    Ask user to enter electricity fee data collected from the electricity company.
    Run a while loop to get the correct data, number with 1 decimal place.
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
                print("Data is valid.\n")
                return data 
            else:
                print("Invalid input, please enter a number with one decimal place\n")
        except ValueError:
            print("Invalid input, please enter a number with one decimal place\n")


def get_subscription_fee():
    """
    Ask user to enter subscription fee data collected from the electricity company.
    Run a while loop to get the correct data, 3 digit number.
    """
    print("Please enter subscription fee data from electricity company.")
    print("Data should be a three digit number. Example 357.\n")

    # Check so exactly 3 digit number is entered.
    while True:
        data_str = input("Enter your data here:")
        if data_str.isdigit() and len(data_str) == 3:
            print("Data is valid.\n")
            return int(data_str)
        else:
            print("Invalid input, please enter a 3 digit number.\n")


def get_transfer_fee():
    """
    Ask user to enter transfer fee data collected from the electricity company.
    Run a while loop to get the correct data, number with 1 decimal place.
    """
    print("Please enter transfer fee data from electricity company.")
    print ("Data should be a number with 1 decimal. Example 1.9.\n")

    # Check if float number with 1 decimal is entered.
    while True:
        data_str = input("Enter your data here:")
        try:
            data = float(data_str)
            if data.is_integer():
                print("Invalid input, please enter a number with one decimal place\n")
            elif round(data, 1) == data: #check if number has one decimal
                print("Data is valid.\n")
                return data 
            else:
                print("Invalid input, please enter a number with one decimal place\n")
        except ValueError:
            print("Invalid input, please enter a number with one decimal place\n")


def get_total_consumption():
    """
    Ask user to enter total consumption from meeter.
    Run a while loop to get the correct data, 3 digit number.
    """
    print("Please enter total consumption from meeter.")
    print("Data should be a three digit number between 500 to 999.\n")

    # Check so exactly 3 digit number between 500 to 999 is entered.
    while True:
        data_str = input("Enter your data here, a number between 500 to 999:")
        if data_str.isdigit() and 500 <= int(data_str) <= 999:
            print("Data is valid.\n")
            return int(data_str)
        else:
            print("Invalid input, please enter a number between 500 to 999.\n")


def get_landlord_consumption():
    """
    Ask user to enter total consumption from meeter.
    Run a while loop to get the correct data, number 70 to 120.
    """
    print("Please enter total consumption from meeter.")
    print("Data should be a three digit number between 70 to 120.\n")

    # Check so exactly 3 digit number between 500 to 999 is entered.
    while True:
        data_str = input("Enter your data here, a number between 70 to 120:")
        if data_str.isdigit() and 70 <= int(data_str) <= 120:
            print("Data is valid.\n")
            return int(data_str)
        else:
            print("Invalid input, please enter a number between 70 to 120.\n")


def update_costs_sheet():
    """
    Update the costs sheet with the data from the functions get_monthly_fee
    get_electricity_fee, get_subscription_fee and get_transfer_fee
    and add a new row.
    """
    print("Uppdating costs worksheet...\n")
    costs_sheet = SHEET.worksheet("costs")
    
    
    # Collect user input for each function 
    monthly_fee = get_monthly_fee()
    electricity_fee = get_electricity_fee()
    subscription_fee = get_subscription_fee()
    transfer_fee = get_transfer_fee()

    # Append new row to cost sheet
    new_row_costs = [monthly_fee, electricity_fee, subscription_fee, transfer_fee]
    costs_sheet.append_row(new_row_costs)

    print("Costs sheet updated with the following data:")
    print("Monthly fee:", monthly_fee)
    print("Electricity fee:", electricity_fee)
    print("Subscription fee:", subscription_fee)
    print("Transfer fee:", transfer_fee)


def update_consumption_sheet():
    """
    Update the consumption sheet with the data from the functions
    get_total_consumption and get_landlord_consumption
    and add a new row.
    """
    print("Uppdating consumption worksheet...\n")
    consumption_sheet = SHEET.worksheet("consumption")
    
    # Collect user input for each function 
    total_consumption = get_total_consumption()
    landlord_consumption = get_landlord_consumption()

    # Append new row to consumption sheet
    new_row_consumption = [total_consumption, landlord_consumption]
    consumption_sheet.append_row(new_row_consumption)

    print("Costs sheet updated with the following data:")
    print("Consumption total:", total_consumption)
    print("Consumption landlord:", landlord_consumption)
    
    
# Call the functions to collect user input
monthly_fee = get_monthly_fee()
electricity_fee = get_electricity_fee()
subscription_fee = get_subscription_fee()
transfer_fee = get_transfer_fee()
total_consumption = get_total_consumption()
landlord_consumption = get_landlord_consumption()

# Call the update_costs_sheet function to update the worksheet
update_costs_sheet()

update_consumption_sheet()

