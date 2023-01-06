from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = wd.Chrome() #or Firefox()
driver.get('https://www.indeed.com/')

input_what = driver.find_element(By.ID, "text-input-what")
input_what.click()
input_what.send_keys('Software')
input_what.send_keys(Keys.ENTER)

time.sleep(5)
#NOTES:
#driver.find_element_by_css_selector() - is also an option, when looking for a css class
#in the case of Indeed.com's what and where, I could've looked for
#class = "icl-TextInput-control icl-TextInput-control--withIconRight"

#driver.find_element_by_xpath()