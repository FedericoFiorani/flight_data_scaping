#!/usr/bin/env python
# coding: utf-8

# ## Flight Data Web Scraping

# ### Project aimed at collecting information about flights' cancellations from FlightAware.com

# Installing all the packages required for the analysis

# In[3]:


pip install --upgrade pip


# In[5]:


pip install msgpack


# In[6]:


pip install selenium


# Importing the required modules

# In[33]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import date, timedelta


# Creating the link between Chrome, Cromedriver and Selenium

# In[34]:


options = Options()
options.binary_location = "C:\Application Data\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:\chromedriver\chromedriver.exe')
driver.get('http://google.com/')
print("Chrome Browser Invoked")


# Directing the Chromedriver towards the webpage of interest: FlightAware - Cancelled flights

# In[35]:


url = 'https://uk.flightaware.com/live/cancelled/yesterday'
driver.get(url)
#setting a sleeping time to add delay in the execution of the program
time.sleep(3)


# Clicking accept on the cookies' widgets

# In[36]:


driver.find_element_by_css_selector('button.sc-ifAKCX.ljEJIv').click()
time.sleep(3)

driver.find_element_by_css_selector('span#cookieDisclaimerButtonText').click()
time.sleep(3)


# Creating a list of all the airlines present in the main page of FlightAware.com

# In[14]:


#locating the table
tables1 = driver.find_elements_by_id("airline-cancel-table")

for table in tables1:
    print('ok')

#finding the right classes in the html script and inserting them into an empty list
all_rows1 = table.find_elements_by_class_name("smallrow1")
all_rows2 = table.find_elements_by_class_name("smallrow2")

all_rows = all_rows1+all_rows2

airlines = []
for table in tables1:
    for row in all_rows:
        for air in row.find_elements_by_tag_name('a'):
            airlines.append(air.text)


# The airline analized will be (all the ones in the website):

# In[15]:


print(airlines)


# Counting the number of airlines present in the website in the chosen day: 

# In[16]:


len(airlines)


# Defining the function to create the initial column of the historical cancelled flights' dataset

# In[26]:


#the function takes as the only argument the date of today
def initiate_file(date_today):

#the data is retreived from the day before the scraping happens
    date_yesterday = date_today - timedelta(days=1) 

#opening a new csv file in writing mode, naming it and using a standard encoding
#using the comma instead of the tab to facilitate work on the csv file in R
    f = open('Flights.csv', 'w', encoding = 'utf-8')
    f.write(f'{date_yesterday}\nAirline_origin,\tAirport_origin_for_each_airline\n')

#going through each airline from the list previously created
    for air in airlines:
        driver.find_element_by_link_text(air)
        origin_airline = driver.find_element_by_link_text(air).text
        driver.find_element_by_link_text(air).click()

        for start_plane in driver.find_elements_by_class_name("hint")[::2]:
                f.write(f"{origin_airline},{start_plane.text}\n") 
                
#since some airlines have multiple pages of flight cancellations, this function runs through every page until there is no more "Next 20" button to push        
        try: 
            while True:
                driver.find_element_by_link_text('Next 20').click()

#considering every other element because we are only considering the origin
                for start_plane in driver.find_elements_by_class_name("hint")[::2]:
                    f.write(f"{origin_airline},{start_plane.text}\n")
                time.sleep(3)

#when the pages of a certain ailine finish, the driver goes back to the main page
        except:
            driver.get(url)
            time.sleep(3)     
       
        
        time.sleep(3)

#after all the data from every airline is printed into the csv file, the code closes the document
    f.close()   


# Function to be called only one time (at the beginning of the dataset)

# In[21]:


initiate_file(date.today())


# Defining the function to append the same kind of data as before, but everyday

# In[39]:


#the function takes as the only argument the date of today
def get_data(date_today):

#the data is retreived from the day before the scraping happens
    date_yesterday = date_today - timedelta(days=1) 

#opening a new csv file in append mode, directing to the right file, same e
    f = open('Flights.csv', 'a', encoding = 'utf-8')

#going through each airline from the list previously created
    for air in airlines:
        driver.find_element_by_link_text(air)
        origin_airline = driver.find_element_by_link_text(air).text
        driver.find_element_by_link_text(air).click()

        for start_plane in driver.find_elements_by_class_name("hint")[::2]:
                f.write(f"{origin_airline},{start_plane.text}\n") 
                
#since some airlines have multiple pages of flight cancellations, this function runs through every page until there is no more "Next 20" button to push        
        try: 
            while True:
                driver.find_element_by_link_text('Next 20').click()

#considering every other element because we are only considering the origin
                for start_plane in driver.find_elements_by_class_name("hint")[::2]:
                    f.write(f"{origin_airline},{start_plane.text}\n")
                time.sleep(3)

#when the pages of a certain ailine finish, the driver goes back to the main page
        except:
            driver.get(url)
            time.sleep(3)     
       
        
        time.sleep(3)

#after all the data from every airline is printed into the csv file, the code closes the document
    f.close()


# Function to be called everyday at anytime e.g. 12:00 a.m. because the data is from yesterday

# In[ ]:


get_data(date.today())

