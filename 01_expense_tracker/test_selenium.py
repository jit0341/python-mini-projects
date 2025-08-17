from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# path to chromedriver (Termux usually keeps it in /data/data/com.termux/files/usr/bin/)
service = Service("/data/data/com.termux/files/usr/bin/chromedriver")

# Chrome options (headless = no GUI)
options = webdriver.ChromeOptions()
options.add_argument("--headless")         # run in background
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Launch browser
driver = webdriver.Chrome(service=service, options=options)

# Open a website
driver.get("https://www.python.org")

print("Page Title:", driver.title)

# Find the first element with CSS selector
elem = driver.find_element(By.CSS_SELECTOR, ".introduction")
print("Intro text:", elem.text[:100], "...")

time.sleep(2)
driver.quit()
