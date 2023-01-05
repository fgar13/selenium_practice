from selenium import webdriver as wd
import time

driver = wd.Chrome() #or Firefox()

driver.get('https://www.indeed.com/')
time.sleep(5000)
