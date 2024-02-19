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

### Existing features

#### Data collection

 - Invoice from the electricity supplier
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

If more tenants are added implement tenants name and list all data per tenant

## Testing 

### Functional testing

### Pep8 validation

white spaces
characters

### Unfixed Bugs

## Deployment

### Github

### Heroku

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