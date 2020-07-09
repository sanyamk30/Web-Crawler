#!/usr/bin/env python
# coding: utf-8

# In[87]:


from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs


# In[88]:


driver = wd.Chrome(executable_path = '/home/sanyam/Downloads/chromedriver')
driver.maximize_window()


# In[89]:


driver.get("https://www.booking.com/index.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaGyIAQGYAQm4ARnIAQzYAQPoAQGIAgGoAgO4ArbC3fYFwAIB0gIkY2FmMzUwZGEtOTgxNi00NTQ4LWI0N2MtNWE1OGJjMGUxYTQ12AIE4AIB;sid=6726270c9da0b8d57b12856fbe9971d0;keep_landing=1&sb_price_type=total&")


# Sign In Part

# In[90]:


sign_in = driver.find_element_by_link_text('Sign in')
sign_in.click()


# In[91]:


email = driver.find_element_by_id('username')
email.send_keys("") ## put in your username


# In[92]:


next_button = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[1]/div[2]/div/div/div/form/div[3]/button")
next_button.click()


# In[93]:


password = driver.find_element_by_id('password')
password.send_keys("") ## put in your password
sign_in = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[1]/div[2]/div/div/div/form/button")
sign_in.click()


# Searching

# In[94]:


search = driver.find_element_by_id('ss')
search.clear()
search.send_keys("United States")
click = driver.find_element_by_xpath("//*[@id='frm']/div[1]/div[2]/div[1]/div[2]/div/div/div/div/span")
click.click()
dateWidget = driver.find_element_by_xpath("//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table")
columns = dateWidget.find_elements_by_tag_name('td')
from datetime import date
today = date.today()
for i in columns:
    if(str(i.get_attribute("data-date")) == str(today)):
        i.click()
import datetime
tomorrow = today + datetime.timedelta(days=1)
for i in columns:
    if(str(i.get_attribute("data-date")) == str(tomorrow)):
        i.click()
submit = driver.find_element_by_xpath("//*[@id='frm']/div[1]/div[4]/div[2]/button")
submit.click()


# In[95]:


currency_selector= driver.find_element_by_xpath("//*[@id='b_tt_holder_1']")
currency_selector.click() 


# In[96]:


USD = driver.find_element_by_xpath("//*[@id='currency_dropdown_top']/ul[2]/li[1]/a")
USD.click()


# Pagination

# In[97]:


cities = driver.find_element_by_xpath("//*[@id='filter_uf']/div[2]")


# In[98]:


no_of_cities = cities.find_elements_by_tag_name('a')


# In[99]:


x = len(no_of_cities)
x


# In[140]:


def find_latlng(x):
    ##print(x)
    splits = x.split("=")
    ##print(splits)
    lat = splits[1].split(';')[0]
    lng = splits[2].split(';')[0]
    return lat,lng


# In[113]:


hotel_names = []
hotel_address = []
hotel_prices = []

for i in range(19,x):
    cities = driver.find_element_by_xpath("//*[@id='filter_uf']/div[2]")
    no_of_cities = cities.find_elements_by_tag_name('a')
    no_of_cities[i].click()
    driver.refresh()
    li = driver.find_elements_by_xpath("//*[@id='search_results_table']/div[4]/nav/ul/li[3]/a")
    while len(li)!=0:
        li = driver.find_elements_by_xpath("//*[@id='search_results_table']/div[4]/nav/ul/li[3]/a")
        names = driver.find_elements_by_class_name('sr-hotel__name')
        address = driver.find_elements_by_class_name('sr_card_address_line')
        prices = driver.find_elements_by_css_selector('div.bui-price-display__value')
        #links = driver.find_elements_by_partial_link_text('Show on map')
        ##print(len(links),len(names),len(prices))
        for j in range(len(names)):
            ##links = driver.find_elements_by_partial_link_text('Show on Map')
            #links[j].click()
            #window_after = driver.window_handles[1]
            #driver.switch_to_window(window_after)
            #driver.refresh()
            #script = driver.find_element_by_xpath("//*[@id='b2hotelPage']/script[24]")
            #lat,lng = find_latlng(script.get_attribute('innerHTML'))
            #latitude.append(lat)
            #longitude.append(lng)
            #addr = driver.find_element_by_xpath("//*[@id='b_map_container']/div[2]/div[1]/div/div[1]/div[4]")
            #hotel_address.append(addr.text)
            #driver.close()
            #driver.switch_to.window(driver.window_handles[0])
            hotel_names.append(names[j].text)
            hotel_address.append(address[j].text)
            hotel_prices.append(prices[j].text)
            
        if(len(li)!=0):
            button = driver.find_element_by_xpath("//*[@id='search_results_table']/div[4]/nav/ul/li[3]/a")
            button.click()
            driver.refresh() 
#     cities = driver.find_element_by_xpath("//*[@id='filter_uf']/div[2]")
#     no_of_cities = cities.find_elements_by_tag_name('a')
#     no_of_cities[i].click()
#     driver.refresh()
    button = driver.find_element_by_xpath("//*[@id='filter_uf']/div[2]/a")
    button.click()
    driver.refresh()
    


# In[54]:


data = [hotel_names,hotel_address,hotel_prices]
import pandas as pd
df = pd.DataFrame(data)
df = df.T


# In[55]:


df


# In[56]:


df.to_csv('United_States_9June_SA.csv')


# In[114]:


data = [hotel_names,hotel_address,hotel_prices]
import pandas as pd
df1 = pd.DataFrame(data)
df1 = df1.T
df1


# In[115]:


df = pd.concat([df,df1])


# In[116]:


df


# In[ ]:


df.to_csv('United_States_9June_full.csv')


# In[ ]:




