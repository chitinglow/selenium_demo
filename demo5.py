## Wait method

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

# Implicit wait
url = "https://www.tripadvisor.com.sg/Tourism-g29121-Avalon_Catalina_Island_California-Vacations.html"
browser = webdriver.Firefox(executable_path=driver_path)
browser.implicitly_wait(10)
browser.get(url)

# Explicit wait
duration = 10

try:
    element = WebDriverWait(browser, duration).until(EC.presence_of_element_located(
    (By.CLASS_NAME, '_2ftMalEe')))
except TimeoutException as e:
    print('Loading Exceed Delay Time')
else:
    print(element.get_attribute('innerHTML'))