# Electricity data collection


## Table Of Contents

* [Introduction](#Introduction)
* [User demographic](#User-demographic)
	* [Site Goals](#Site-Goals)
    * [Target Audience](#Target-Audience)
* [Structure](#Structure)
	* [Planning](#Planning)
	* [Error handling](#Error-handling)
	* [Existing features](#Existing-features)
		* [API](#API)
		* [Data collection](#Data-collection)
		* [Calculation](#Calculation)
	* [Future features](#Future-features)
* [Testing](#Testing)
	* [Functional testing](#Functional-testing)
	* [Pep8 validation](#Pep8-validation)
* [Deployment](#Deployment)
	* [Github](#Github)
	* [Heroku](#Heroku)
* [Credits](#Credits)

## Introduction

This data collection aims for landlords in Sweden to calculate what the tenant shall pay for the monthly electricity usage. The data collection is a mix of information from the electricity supplier and the landlord's electricity meter. The data is stored in a Google sheet and also provided directly in the terminal.

The live link can be found here

## User demographic

### Site goals

To provide a simple data collection to calculate the cost of electricity monthly usage.

### Target audience

Landlords with one electricity meter and a tenant who wants to charge them for their electricity usage.

## Structure

### Planning

I used [Lucid.app](www.lucidchart.com) to plan the data collection.

#### Start

![LCstart](docs/screenshots/lucidchart_start.png)

#### User entries

![LCuserentries](docs/screenshots/lucidchart_user_entries.png)

#### Calculations

![LCcalculations](docs/screenshots/lucidchart_calculations.png)


### Error handling

Print messages were used throughout writing the code to ensure no errors occurred.

### Existing features

#### API

Google Sheets was used to store the data collection and was set up as below.

- At [Google Cloud](https://console.cloud.google.com/) Create a new project.
- Name the project.
- Select the project
- Go to APIs & Services and select library
- Search for Google Drive API, select it and press enable
- Then press create credentials
- Select as in the image below
- Then choose service role
- Next, click on the generated email address
- Add service key
- Choose json and create
- Go back to the library, search for Google Sheets API, and press enable.

I then uploaded the .json file to the IDE and renamed it creds. 

In the creds file, I copied the email address and shared my Google Sheets with that address.

#### Data collection

 - Below fees are retrieved from the invoice from the electricity supplier
	 - Monthly fee
	 - Electricity fee
	 - Subscription fee
	 - Transfer fee
	 - Total monthly usage

- Landlords monthly usage from meter

- Update costs sheet

- Update consumption sheet

#### Calculation

- Calculate the tenant's usage

- Calculate the tenant's monthly cost

### Future features 

- If more tenants are added implement the tenant's name and show costs for each tenant separately. 
- A weekly debit instead of monthly for weekly tenants.

## Testing 

All functions have been tested to ensure they work correctly and show valid user feedback.

![Test_1](docs/screenshots/testing/test_overview_1.png)

![Test_2](docs/screenshots/testing/test_overview_2.png)

### Functional testing

### Pep8 validation

Validation was done according to [PEP8](https://pep8ci.herokuapp.com/#) rules. Most warnings were due to redundant whitespace or whitespace missing which are all corrected.

### Unfixed Bugs

## Deployment

The app was created in Visual Studio Code editor desktop app. After some issues with the desktop app that could be linked to homebrew, I used Visual Studio Code in the browser.

### Github

The repository was created on GitHub.

### Heroku

The app was deployed on Heroku.

Even after running pip3 install -r requirements.txt some requirements were not added so an error message was shown when launching Heroku. The requirements for pyfiglet and colorama were added manually.

Configurations

## Credits 
- The app is inspired by Love Sandwiches 
- [Tutorials point](https://www.tutorialspoint.com/how-do-i-call-a-variable-from-another-function-in-python) - How to make a variable global
- [Geegs for geeks](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) - How to use pyfiglet for ASCII art
- [Scaler](https://www.scaler.com/topics/how-to-clear-screen-in-python/) - How to clear screen with os
- [Pypi](https://pypi.org/project/colorama/) - How to import colorama
- [Snyk Advisor](https://snyk.io/advisor/python/colorama/functions/colorama.Style.RESET_ALL) - How to use colorama
- [FreeCodeCamp](https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/#:~:text=You%20can%20use%20Python%27s%20sleep,time%20delay%20to%20your%20code) - How to use sleep function to show print message before clear function
- [Ask Python](https://www.askpython.com/python/string/decimal-formatting-0f-vs-1f) - How to show 2 decimals
- [Stack Overflow](https://stackoverflow.com/questions/6557553/get-month-name-from-number) - Ho to show the current month as string
- Thanks to fellow student Ben Gilbert for testing the app
- Thanks to my mentor Gareth McGirr