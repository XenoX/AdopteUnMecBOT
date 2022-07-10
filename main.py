import time
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#######################################################
##################### CHANGE THIS #####################
#######################################################
email = 'CHANGEME'
password = 'CHANGEME'
search = 'métalleuse de Paris de moins de 50ans'
#######################################################

s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)

base_domain = "https://www.adopteunmec.com"

# Connect and go to search page
driver.get(base_domain)

driver.find_element(By.XPATH, '//*[@id="btn-display-login"]').click()
driver.find_element(By.XPATH, '//*[@id="mail"]').send_keys(email)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/section/form/div[2]/button').click()

driver.get(base_domain+"/gogole?q=" + search.replace(" ", "+"))

# Scroll down for discover all results
for i in range(6):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)

# Get profiles links
sel = Selector(text=driver.page_source)
profile_links = []
for item in sel.xpath('//*[@id="grid-container"]//a[contains(@href, "/profile/")]/@href').getall():
    if not item.startswith(base_domain):
        item = base_domain + item
    profile_links.append(item)

# Visit all profiles
profile_links = list(set(profile_links))
for link in profile_links:
    print("Visit : " + link)
    driver.get(link)
    time.sleep(0.5)

print(str(len(profile_links)) + " visited profiles")

driver.close()