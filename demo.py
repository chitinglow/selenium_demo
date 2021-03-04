from selenium.webdriver import Firefox, Chrome, Edge, safari
from selenium.webdriver.common.keys import Keys

url = 'https://finance.yahoo.com/?guccounter=1'
driver_path = 'geckodriver.exe'

browser = Firefox(executable_path=driver_path)
browser.get(url)

#get the element id
search_fields_id = 'yfin-usr-qry'

#navigating element (#dir(Keys) class to navigate)
element_search_field =  browser.find_element_by_id(search_fields_id)
element_search_field.clear()
element_search_field.send_keys('TSLA')
element_search_field.send_keys(Keys.ENTER)

## Close current tab
#browser.close()
## Quit browser
browser.quit()

## 