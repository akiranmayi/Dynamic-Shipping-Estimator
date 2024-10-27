# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:15:11 2023

@author: anupi
"""
import re
from urllib.request import urlopen  # b_soup_1.py
from bs4 import BeautifulSoup




def extract_and_return_max(s):
    numbers = re.findall(r'\b\d+\b', s)
    
    if numbers:
        numbers = [int(num) for num in numbers]
        return max(numbers)
    else:
        return None


def parcelchief(weight):

    
    html = urlopen('https://www.parcelchief.in/courier-to/usa-from-india/')

    bsyc = BeautifulSoup(html.read(), "lxml")
    
    fout = open('bsyc_temp.txt', 'wt',encoding='utf-8')
    
    fout.write(str(bsyc))
    
    fout.close()
    
    table_list = bsyc.findAll('table')

    # how many are there?

    
    # there is only one table, so get it
    table = table_list[0]
    
    # ... and get a list of all the rows
    rows = table.findAll('tr')


    # first row (sub-0 row) contains column headers
    headers = rows[0].findAll('th')

    
        
    parcel_chief_delivery_days = []
    parcel_chief_delivery_prices = []
    parcel_chief_delivery_types = []


    for idx, h in enumerate(headers):
        if idx!=0:
            parcel_chief_delivery_types.extend(h.contents)
        
    
    parcel_chief_delivery_days = [extract_and_return_max(str(col)) for col in rows[1].find_all('td')[1:]]
    
            
    for row in rows[3:]:

        columns = row.find_all('td')
    
        # Access data from each column
        if len(columns) >= 3:  # Make sure there are at least three columns
            column_1_data = columns[0].get_text(strip=True)
            column_2_data = columns[1].get_text(strip=True)
            column_3_data = columns[2].get_text(strip=True)
            
            if  weight > 50  and column_1_data == '50+ Kg':

                price1 = int(re.sub(r'[^\d.]', '', column_2_data))
                price2 = int(re.sub(r'[^\d.]', '', column_3_data))
                parcel_chief_delivery_prices.append(price1)
                parcel_chief_delivery_prices.append(price2)

                break
            elif weight > 30 and weight <= 50  and column_1_data == '30+ Kg':

                price1 = int(re.sub(r'[^\d.]', '', column_2_data)) * weight
                price2 = int(re.sub(r'[^\d.]', '', column_3_data)) * weight
                parcel_chief_delivery_prices.append(price1)
                parcel_chief_delivery_prices.append(price2)

                break
            elif weight == int(re.sub(r'[^\d.]', '', column_1_data)): 

                price1 = int(re.sub(r'[^\d.]', '', column_2_data))
                price2 = int(re.sub(r'[^\d.]', '', column_3_data))
                parcel_chief_delivery_prices.append(price1)
                parcel_chief_delivery_prices.append(price2)
                break

                    
    print(parcel_chief_delivery_prices)
    print(parcel_chief_delivery_days)
    print(parcel_chief_delivery_types)

    return parcel_chief_delivery_days, parcel_chief_delivery_prices, parcel_chief_delivery_types
    
#fedex_delivery_days, fedex_delivery_prices, fedex_delivery_types = parcelchief(32)
