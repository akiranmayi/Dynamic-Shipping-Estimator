from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime



def select_dimensions(browser, formcontrolname_length, length, formcontrolname_width, width, formcontrolname_height, height):
    
    length_field = browser.find_element_by_css_selector("[formcontrolname='" + formcontrolname_length + "']")
    length_field.send_keys(length)
    
    width_field = browser.find_element_by_css_selector("[formcontrolname='" + formcontrolname_width + "']")
    width_field.send_keys(width)
    
    height_field = browser.find_element_by_css_selector("[formcontrolname='" + formcontrolname_height + "']")
    height_field.send_keys(height)

    

def select_weight(browser, weight_id, weight):
    input_field = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.ID, weight_id)))
    input_field.send_keys(weight)
    

def select_address_from_autocomplete(browser, address_id, address_text, dropdown_id):

    input_field = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.ID, address_id)))
    input_field.send_keys(address_text)

    option_xpath = f".//*[text()='{address_text}']"
    WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.XPATH, option_xpath)))
    
    select_from_dropdown(browser, dropdown_id, address_text)
    


def select_from_dropdown(browser, dropdown_id, value_to_select):
    # Find the dropdown by ID
    dropdown = browser.find_element(By.ID, dropdown_id)
    
    time.sleep(5)

    # Click the dropdown to open the options
    #browser.execute_script("arguments[0].click();", dropdown)

    dropdown.click()
    

def fedex(from_address_text, to_address_text, weight):


    chrome_driver_path = "C:/Users/anupi/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
    

    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get("https://www.fedex.com/en-us/online/rating.html#") 
    
    
    
    from_address_id = "fromGoogleAddress"
    to_address_id = "toGoogleAddress"
    weight_id = "package-details__weight-0"
    button_id = "e2ePackageDetailsSubmitButtonRates"
    
    dropdown_id = "e2eGoogleAddressSuggestionList" 
    
    formcontrolname_length = "length"
    formcontrolname_width = "width"
    formcontrolname_height = "height"
    
    
    # from_address_text = "Thane"
    # to_address_text = "Pittsburgh"
    
    
    #weight = "15"
    length = "15"
    width = "15"
    height = "15"
    
    print(from_address_text)
    print(to_address_text)
    print(weight)
    
    
    
    select_address_from_autocomplete(driver, from_address_id, from_address_text, dropdown_id)
    time.sleep(2)
    select_address_from_autocomplete(driver, to_address_id, to_address_text, dropdown_id)
    select_weight(driver, weight_id, weight)
    select_dimensions(driver, formcontrolname_length, length, formcontrolname_width, width, formcontrolname_height, height)
    
    show_rates_button = driver.find_element_by_id(button_id)
    show_rates_button.click()
    
    
    fedex_delivery_dates = []
    fedex_delivery_days = []
    fedex_delivery_types = []
    fedex_delivery_prices = []
    
    days_of_week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    
    
    
    
    delivery_date_class = "fdx-c-definitionlist__description fdx-u-font-size--h6 fdx-u-text--light"
    
    """

    delivery_date_class_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//dd[@class='{delivery_date_class}']"))
    )
    
    delivery_date_class_elements = delivery_date_class_element.find_elements(By.XPATH, f"//dd[@class='{delivery_date_class}']")

    for index, li_element in enumerate(delivery_date_class_elements, start=1):
        print(f"Item {index}: {li_element.text}")
        if any(li_element.text.startswith(day) for day in days_of_week):
            fedex_delivery_dates.append(str(li_element.text))
            
            
    today_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            
    for date in fedex_delivery_dates:
        given_date = datetime.strptime(date, '%a, %b %d')

        # Get today's date
        today_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
        # Check if the day and month of the given date are before December 31
        if given_date.month < 12 or (given_date.month == 12 and given_date.day <= 31):
            given_date = given_date.replace(year=today_date.year)
        else:
            given_date = given_date.replace(year=today_date.year + 1)
        
        # Calculate the difference in days
        days_difference = (given_date - today_date).days
        
        fedex_delivery_days.append(days_difference)
    """
    

    
    delivery_type_class = "fdx-c-definitionlist__description--small"

    delivery_type_class_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//dd[@class='{delivery_type_class}']"))
    )
    
    delivery_type_class_elements = delivery_type_class_element.find_elements(By.XPATH, f"//dd[@class='{delivery_type_class}']")

    for index, li_element in enumerate(delivery_type_class_elements, start=1):
        print(f"Item {index}: {li_element.text}")
        fedex_delivery_types.append(str(li_element.text))
        
        grandparent_element = li_element.find_element_by_xpath(f"ancestor::div[@class='fdx-o-grid__row']")

        # Navigate to the child element under the specific grandparent
        another_child_element = grandparent_element.find_element_by_xpath(f".//dd[@class='{delivery_date_class}']")
        
        # Get the text content of the another child element
        another_child_text_content = another_child_element.text
        
        
        given_date = datetime.strptime(str(another_child_text_content), '%a, %b %d')

        # Get today's date
        today_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
        # Check if the day and month of the given date are before December 31
        if given_date.month < 12 or (given_date.month == 12 and given_date.day <= 31):
            given_date = given_date.replace(year=today_date.year)
        else:
            given_date = given_date.replace(year=today_date.year + 1)
        
        # Calculate the difference in days
        days_difference = (given_date - today_date).days
        
        fedex_delivery_days.append(days_difference)
        # ancestor_text_content = li_element.find_element_by_xpath(f"../dd[@class='{delivery_date_class}']").text
        print(f"li_element.text: another_child_text_content -  {li_element.text}: {another_child_text_content}")
        
        
        
    
    delivery_price_class = "magr-c-rates__button fdx-c-button fdx-c-button--primary fdx-u-mb--4 fdx-u-mt--4@small-only fdx-u-flex--column"

    delivery_price_class_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//button[@class='{delivery_price_class}']"))
    )
    
    delivery_price_class_elements = delivery_price_class_element.find_elements(By.XPATH, f"//button[@class='{delivery_price_class}']")

    for index, li_element in enumerate(delivery_price_class_elements, start=1):
        print(f"Item {index}: {li_element.text}")
        fedex_delivery_prices.append(str(li_element.text))
        
    
    
    driver.quit()
    
    print(fedex_delivery_days)
    print(fedex_delivery_prices)
    print(fedex_delivery_types)
    return fedex_delivery_days, fedex_delivery_prices, fedex_delivery_types

"""    
fedex_delivery_days, fedex_delivery_prices, fedex_delivery_types = fedex()

fedex_delivery_prices_numeric = [float(re.sub(r'[^\d.]', '', price)) for price in fedex_delivery_prices]

# Plotting delivery days
plt.figure(figsize=(10, 5))
plt.bar(fedex_delivery_types, fedex_delivery_days, color='skyblue')
plt.title('FedEx Delivery Days')
plt.xlabel('Delivery Type')
plt.ylabel('Delivery Days')
plt.xticks(rotation=45, ha='right')
plt.show()

# Plotting delivery prices
plt.figure(figsize=(10, 5))
plt.bar(fedex_delivery_types, fedex_delivery_prices_numeric, color='lightcoral')
plt.title('FedEx Delivery Prices')
plt.xlabel('Delivery Type')
plt.ylabel('Delivery Price (in ₹)')
plt.xticks(rotation=45, ha='right')
plt.show()


x = np.arange(len(fedex_delivery_types))

# Plotting all fields in a grouped bar chart
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plotting delivery days
ax1.bar(x - 0.2, fedex_delivery_days, width=0.2, color='skyblue', label='Delivery Days')

# Plotting delivery prices on a secondary y-axis
ax2 = ax1.twinx()
ax2.bar(x, fedex_delivery_prices_numeric, width=0.2, color='lightcoral', label='Delivery Prices')

# Labeling the secondary y-axis
ax2.set_ylabel('Delivery Price (in ₹)', color='lightcoral')
ax2.tick_params(axis='y', labelcolor='lightcoral')

# Set x-axis ticks and labels
plt.xticks(x, fedex_delivery_types, rotation=45, ha='right')

# Set common labels and title
ax1.set_xlabel('Delivery Type')
ax1.set_ylabel('Delivery Days')
plt.title('FedEx Delivery Days and Prices')

# Display the legend
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax2.legend(loc='upper left', bbox_to_anchor=(1, 0.85))

plt.tight_layout()
plt.show()


# Plotting a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(fedex_delivery_days, fedex_delivery_prices_numeric, color='purple')
plt.title('Scatter Plot: Delivery Days vs Delivery Prices')
plt.xlabel('Delivery Days')
plt.ylabel('Delivery Price (in ₹)')

# Adding labels for each point
for i, txt in enumerate(fedex_delivery_types):
    plt.annotate(txt, (fedex_delivery_days[i], fedex_delivery_prices_numeric[i]))

plt.show()
"""