from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("/data/data/com.termux/files/usr/bin/geckodriver")

options = webdriver.FirefoxOptions()
options.add_argument("--headless")    # no GUI mode

driver = webdriver.Firefox(service=service, options=options)
driver.get("https://www.python.org")

print("Page Title:", driver.title)

elem = driver.find_element(By.CSS_SELECTOR, ".introduction")
print("Intro text:", elem.text[:100], "...")

time.sleep(2)
driver.quit()
