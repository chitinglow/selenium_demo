from selenium.webdriver import Firefox, Chrome, Edge, safari
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


url = 'https://jenniferdewalt.com/click_challenge.html'
driver_path = 'geckodriver.exe'

browser = Firefox(executable_path=driver_path)
browser.get(url)


action_chains = ActionChains(browser)
browser.find_element_by_id('start').click()

for i in range(300):
    action_chains.double_click().perform()