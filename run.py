import gspread
from google.oauth2.service_account import Credentials
import pyfiglet
import os
import time
from colorama import Fore, Style
from datetime import datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("electricity-stats")


class ColoredText:  # Class for changing the color of texts
    """
    Class for changing the text color to green
    """

    def green(text):
        return f"{Fore.GREEN}{text}{Style.RESET_ALL}"  # Green text

    """
    Class for changing the text color to red
    """

    def red(text):
        return f"{Fore.RED}{text}{Style.RESET_ALL}"  # Red text

    """
    Class for changing the text color to blue
    """

    def blue(text):
        return f"{Fore.BLUE}{text}{Style.RESET_ALL}"  # Blue text

    """
    Class for changing the text color to yellow
    """

    def yellow(text):
        return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"  # Yellow text

    """
    Class for changing the text color to cyan
    """

    def cyan(text):
        return f"{Fore.CYAN}{text}{Style.RESET_ALL}"  # Cyan text


def get_monthly_fee():
    """
    Ask user to enter monthly fee data collected from the electricity supplier.
    Run a while loop to get the correct data, 2 digit number.
    """
    print("Please enter monthly fee data from electricity supplier.")
    print("Data should be a two digit number. Example 20.\n")

    # Check so exactly 2 digit number is entered.
    while True:
        data_str = input("Enter your data here:\n")
        if data_str.isdigit() and len(data_str) == 2:
            print(ColoredText.green("Data is valid.\n"))
            time.sleep(2)  # Wait for 2 seconds
            os.system('clear')  # Clear the terminal
            return int(data_str)
        else:
            print(ColoredText.red("Invalid input, please enter a 2 digit "
                  "number.\n"))


def get_electricity_fee():
    """
    Ask user to enter electricity fee data collected from the
    electricity supplier.
    Run a while loop to get the correct data, number with 1 decimal place.
    """

    print("Please enter electricity fee data from electricity supplier.")
    print("Data should be a number with 1 decimal. Example 1.5.\n")

    # Check if float number with 1 decimal is entered.
    while True:
        data_str = input("Enter your data here:\n")
        try:
            data = float(data_str)
            if data.is_integer():
                print(ColoredText.red("Invalid input, please enter a number "
                      "with one decimal place\n"))
            elif round(data, 1) == data:  # check if number has one decimal
                print(ColoredText.green("Data is valid.\n"))
                time.sleep(2)  # Wait for 2 seconds
                os.system('clear')  # Clear the terminal
                return data
            else:
                print(ColoredText.red("Invalid input, please enter a number "
                      "with one decimal place\n"))
        except ValueError:
            print(ColoredText.red("Invalid input, please enter a number "
                  "with one decimal place\n"))


def get_subscription_fee():
    """
    Ask user to enter subscription fee data collected from
    the electricity supplier.
    Run a while loop to get the correct data, 3 digit number.
    """

    print("Please enter subscription fee data from electricity supplier.")
    print("Data should be a three digit number. Example 357.\n")

    # Check so exactly 3 digit number is entered.
    while True:
        data_str = input("Enter your data here:\n")
        if data_str.isdigit() and len(data_str) == 3:
            print(ColoredText.green("Data is valid.\n"))
            time.sleep(2)  # Wait for 2 seconds
            os.system('clear')  # Clear the terminal
            return int(data_str)
        else:
            print(ColoredText.red("Invalid input, please enter a "
                  "3 digit number.\n"))


def get_transfer_fee():
    """
    Ask user to enter transfer fee data collected from the electricity
    supplier.
    Run a while loop to get the correct data, number with 1 decimal place.
    """

    print("Please enter transfer fee data from electricity supplier.")
    print("Data should be a number with 1 decimal. Example 1.9.\n")

    # Check if float number with 1 decimal is entered.
    while True:
        data_str = input("Enter your data here:\n")
        try:
            data = float(data_str)
            if data.is_integer():
                print(ColoredText.red("Invalid input, please enter a number "
                      "with one decimal place\n"))
            elif round(data, 1) == data:  # check if number has one decimal
                print(ColoredText.green("Data is valid.\n"))
                time.sleep(2)  # Wait for 2 seconds
                os.system('clear')  # Clear the terminal
                return data
            else:
                print(ColoredText.red("Invalid input, please enter a number "
                      "with one decimal place\n"))
        except ValueError:
            print(ColoredText.red("Invalid input, please enter a number "
                  "with one decimal place\n"))


def get_total_consumption():
    """
    Ask user to enter total consumption from meter.
    Run a while loop to get the correct data, 3 digit number.
    """
    print("Please enter total consumption from meter.")
    print("Data should be a three digit number between 500 to 999.\n")

    # Check so exactly 3 digit number between 500 to 999 is entered.
    while True:
        data_str = input("Enter your data here, a number "
                         "between 500 to 999:\n")
        if data_str.isdigit() and 500 <= int(data_str) <= 999:
            print(ColoredText.green("Data is valid.\n"))
            time.sleep(2)  # Wait for 2 seconds
            os.system('clear')  # Clear the terminal
            return int(data_str)
        else:
            print(ColoredText.red("Invalid input, please enter a number "
                  "between 500 to 999.\n"))


def get_landlord_consumption():
    """
    Ask user to enter landlords total consumption.
    Run a while loop to get the correct data, number 70 to 120.
    """
    print("Please enter landlords total consumption.")
    print("Data should be a three digit number between 70 to 120.\n")

    # Check so exactly 3 digit number between 500 to 999 is entered.
    while True:
        data_str = input("Enter your data here, a number between 70 to 120:\n")
        if data_str.isdigit() and 70 <= int(data_str) <= 120:
            print(ColoredText.green("Data is valid.\n"))
            time.sleep(2)  # Wait for 2 seconds
            os.system('clear')  # Clear the terminal
            return int(data_str)
        else:
            print(ColoredText.red("Invalid input, please enter a number "
                  "between 70 to 120.\n"))


def update_costs_sheet():
    """
    Update the costs sheet with the data from the functions get_monthly_fee
    get_electricity_fee, get_subscription_fee and get_transfer_fee
    and add a new row.
    """

    costs_sheet = SHEET.worksheet("costs")

    # Call the functions to collect user input
    monthly_fee = get_monthly_fee()
    electricity_fee = get_electricity_fee()
    subscription_fee = get_subscription_fee()
    transfer_fee = get_transfer_fee()
    print(ColoredText.yellow("Updating costs worksheet...\n"))

    # Append new row to cost sheet
    new_row_costs = ([monthly_fee, electricity_fee, subscription_fee,
                     transfer_fee])
    costs_sheet.append_row(new_row_costs)

    print("Costs sheet updated with the following data:")
    print("Monthly fee:", monthly_fee)
    print("Electricity fee:", electricity_fee)
    print("Subscription fee:", subscription_fee)
    print("Transfer fee:", transfer_fee, "\n")


def update_consumption_sheet():
    """
    Update the consumption sheet with the data from the functions
    get_total_consumption and get_landlord_consumption
    and add a new row.
    """

    consumption_sheet = SHEET.worksheet("consumption")

    # Call the functions to collect user input
    total_consumption = get_total_consumption()
    landlord_consumption = get_landlord_consumption()
    print(ColoredText.yellow("Updating consumption worksheet...\n"))

    # Append new row to consumption sheet
    new_row_consumption = [total_consumption, landlord_consumption]
    consumption_sheet.append_row(new_row_consumption)

    print("Costs sheet updated with the following data:")
    print("Consumption total:", total_consumption)
    print("Consumption landlord:", landlord_consumption, "\n")


def calculate_tenants_consumption():
    """
    Calculate tenants consumption by fetching the last user input.
    Stating the index of the cells so calculation can be added to correct cell.
    """
    print(ColoredText.yellow("Calculating tenants consumption...\n"))
    consumption_sheet = SHEET.worksheet("consumption")  # Get the worksheet
    consumption = consumption_sheet.get_all_values()
    consumption_row = consumption[-1]

    # Stating the index of the cells
    consumption_total_index = 0
    consumption_landlord_index = 1

    consumption_total = int(consumption_row[consumption_total_index])
    consumption_landlord = int(consumption_row[consumption_landlord_index])

    global consumption_tenant
    consumption_tenant = consumption_total - consumption_landlord

    # Update the cell in the same row
    consumption_sheet.update_cell(len(consumption), 3, consumption_tenant)
    print("Consumption is:", ColoredText.blue(str(consumption_tenant)
          + " kWh"), "\n")


def calculate_total_cost():
    """
    Calculate the total cost that tenant shall pay
    by fetching user input fees and consumption
    Stating index to cells to total cost pushes to correct cell.
    """
    print(ColoredText.yellow("Calculating tenants total cost...\n"))
    costs_sheet = SHEET.worksheet("costs")  # Get the worksheet
    costs = costs_sheet.get_all_values()
    costs_row = costs[- 1]

    # Stating the index of the cells
    monthly_fee_index = 0
    electricity_fee_index = 1
    subscription_fee_index = 2
    transfer_fee_index = 3

    monthly_fee = float(costs_row[monthly_fee_index])
    electricity_fee = float(costs_row[electricity_fee_index])
    subscription_fee = float(costs_row[subscription_fee_index])
    transfer_fee = float(costs_row[transfer_fee_index])

    cost_tenant = ((consumption_tenant * electricity_fee)
                   + (consumption_tenant * transfer_fee)
                   + monthly_fee + subscription_fee)

    costs_sheet.update_cell(len(costs), 5, cost_tenant)  # Update google sheet
    print("Total cost for the tenant for " + current_month + " is "
          + ColoredText.blue("{:.2f}".format(cost_tenant) + " SEK"), "\n")
    print(ColoredText.yellow("End of data collection."))


def main():
    # Call all functions
    update_costs_sheet()
    update_consumption_sheet()
    calculate_tenants_consumption()
    calculate_total_cost()


current_month = datetime.today().strftime('%B')  # get current month
ascii_art = pyfiglet.figlet_format("Electricity Calculation for "
                                   + current_month, font="digital")
colored_ascii_art = ColoredText.cyan(ascii_art)  # Color to cyan
print(colored_ascii_art)
print("Following data collection will inform what the tenant shall "
      "pay for the monthly usage.\n")
main()
