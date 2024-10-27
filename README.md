# Dynamic-Shipping-Estimator

## Introduction

JetPack Shipmate offers a comprehensive solution for comparing shipping rates and options between FedEx and Parcel Chief for international student package deliveries
(currently only India to Pittsburgh). The project gathers and visualizes shipping data and customer reviews.

## Prerequisites
● Python 3.x (Tested on Python 3.11.x)
● Google Chrome Browser
● Chrome WebDriver
● BeautifulSoup4
● Selenium 3.141.0
● Matplotlib
● Numpy
● Pandas


## Installation

● Python Modules
Install the required Python modules if not already installed using pip: 
pip install selenium==3.141.0 matplotlib numpy pandas beautifulsoup4
● Chrome WebDriver
Download the Chrome WebDriver from this link: https://googlechromelabs.github.io/chrome-for-testing/
Make sure you are using the right selenium version (3.141.0) .
Ensure the WebDriver version matches your Chrome browser's version.


## Configuration
Update the chrome_driver_path in the script - FedEx1.py file (refer to the image below) to
the location where you've saved the Chrome WebDriver.
Example :
chrome_driver_path = "path/to/your/chromedriver"

Running the Main Script
In your chosen Python IDE, navigate to the unzipped project folder and run the Main.py
script. This script uses FedEx1, ParcelChief, and Reviews modules internally.

python Main.py

Process Flow
● The script prompts for the origin city and the weight of the parcel.
● It then retrieves and compares shipping data from FedEx and Parcel Chief.
● The script also scrapes customer reviews for these services from Trustpilot.
● Visualizations of delivery options and customer reviews are displayed using Matplotlib.

Usage
● Respond to the script's prompts regarding the origin city and parcel weight.
● Currently we are only shipping from Mumbai, Bengaluru and Chennai cities in India.
●The maximum weight that can be entered is 500 kgs / 1102.31 lbs
● The script will handle all data retrieval, processing, and visualization.

Additional Notes
● Ensure a stable internet connection for web scraping and data retrieval.
● Adjust file paths and configurations according to your system setup.
