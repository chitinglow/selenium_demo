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


"""
Refresh, Go Back, Go Forward
"""
#browser.refresh()
#browser.back()
#browser.forward()

"""
Minimize window, Maximize window, restore window
"""
## Get browser window size
w, h = browser.get_window_size().values()

browser.maximize_window()
browser.minimize_window()
browser.set_window_size(w,h)


"""
Action Chains class (perform complex actions)
"""
from selenium.webdriver import ActionChains

action_chains = ActionChains(browser)
action_chains.key_down(Keys.CONTROL).send_keys("V").key_up(Keys.CONTROL).perform()

xpath_string = '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div/section/div/ul/li[2]/a/span'
element = browser.find_element_by_xpath(xpath_string)
action_chains.move_to_element(element).click().perform()

