# LOGIN TEST WOOCOMMERCE WEBSITE (Pytest Framework)

This project contains an automation script for performing a login test on a WooCommerce website using Selenium and Python with the Pytest framework. The script follows the Page Object Model (POM) design pattern to organize the code efficiently.

## Description

The automation script performs the following steps:
1. Navigates to the 'My Account' page of the WooCommerce website.
2. Enters the username 'test_customer'.
3. Enters the password 'password'.
4. Clicks the login button.

## Prerequisites

Before you can run the script, you need to have the following installed:
- Python 3.x
- Pip (Python package installer)
- Selenium
- Pytest
- A web driver compatible with your browser (e.g., ChromeDriver for Google Chrome)
- PyCharm (latest version)

## Setup Instructions

1. **Install the Latest Version of PyCharm**

   You can download and install the latest version of PyCharm from the official [JetBrains website](https://www.jetbrains.com/pycharm/download/).

#Creating and activating virtual environment

python -m venv venv
venv\Scripts\activate

#Install the required packages

pip install -r requirements.txt

#Download and setup webdriver

C:\path\to\webdriver"

#Project structure

Pages/login_page.py: Contains the Page Object Model for the login page.
Tests/test_login.py: Contains the test script for performing the login test.

#Additional Information
The Tasks 1 and 2 are compressed to a single Zip file "POM."









