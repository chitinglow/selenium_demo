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

driver_path = 'geckodriver.exe'

url = "https://www.tripadvisor.com.sg/"
browser = webdriver.Firefox(executable_path=driver_path)
browser.get(url)

# Check browser tabs
browser.window_handles

# Create new tab
browser.execute_script('window.open()')
browser.execute_script('window.open("https://facebook.com")')

#show current tabs
print(browser.current_window_handle)


## Switch to different tabs
browser.current_window_handle
browser.switch_to_window(browser.window_handles[1])

# Close tabs
browser.execute_script('window.close("")')


## Scroll pages based on x and y value
browser.execute_script('window.scrollTo(0, 300)')

element = browser.find_element_by_xpath('//h3[text()="Destinations travelers love"')
element.rect
element.location
element.size
browser.execute_script('window.scrollBy(0, {0})'.format(element.rect['y'] - element.rect['height'] - 50))
