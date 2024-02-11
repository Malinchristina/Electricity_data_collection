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
    print ("Data should be a two digit number. Example 20.\n")

    data_str = input("Enter your data here:")
    print(f"You provided: {data_str}\n")

get_monthly_fee()