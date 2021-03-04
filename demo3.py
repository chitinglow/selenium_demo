import os
import time
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException


'''
1) find_element_by_id
1) find_element_by_name
2)find_element_by_xpath
3)find_element_by_link_text
3)find_element_by_partial_link_text
4)find_element_by_tag_name
5)find_element_by_class_name
6)find_element_by_css_selector



'''

# eg 1
driver_path = 'geckodriver.exe'
url = "https://www.facebook.com"
url = "https://sg.finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
browser = webdriver.Firefox(executable_path=driver_path)
browser.get(url)

element_username = browser.find_element_by_id('email')
element_password = browser.find_element_by_name('pass')

element_username.clear()
element_username.send_keys('HelloABC')
element_password.clear()
element_password.send_keys('ABCD123')

browser.find_element_by_id('u_0_d_36').click()
browser.back()

# eg2 

class_name = "Lh(44px)"
element_class = browser.find_element_by_class_name(class_name)

print(element_class)
print(len(element_class))

# eg 3

element1 = browser.find_element_by_link_text('Historical Data')

element2 = browser.find_element_by_partial_link_text('p=AAPL')

element2.click()
browser.back()

page_source_1 = element1.get_attribute('innerHTML')
browser.back()


# eg 4
browser.get('https://facebook.com')
tag1 = browser.find_element_by_tag_name('head')
tag2 = browser.find_elements_by_tag_name('head')

len(tag1)


# eg 5
browser.get('https://www.tripadvisor.com.sg/')

css1 = browser.find_element_by_css_selector('span._28xPSrb')
css1.get_attribute('innerHTML')

# eg 6 XPATH
element_xpath = browser.find_element_by_xpath('//div[text()="Avalon, CA"]')
element_xpath.click()

# eg 7 Find_Element method

e = browser.find_element(By.XPATH, '//span[@class="HLvj7Lh5 _9RPF_Kg6')
e.text