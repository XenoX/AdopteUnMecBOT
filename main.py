#!/usr/bin/python3

import time
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class AdopteUnMec:
    #######################################################
    ##################### CHANGE THIS #####################
    #######################################################
    email = 'CHANGEME'
    password = 'CHANGEME'
    searchs = [
        'métalleuse de Paris de moins de 50ans',
        'jongleuse de Versailles de moins de 30ans',
        'rentière de Neuilly de plus de 80ans',
    ]
    #######################################################

    def __init__(self):
        self.email = AdopteUnMec.email
        self.password = AdopteUnMec.password
        self.searchs = AdopteUnMec.searchs
        self.base_domain = "https://www.adopteunmec.com"
        self.s = Service('./chromedriver')
        self.driver = webdriver.Chrome(service = self.s)
        self.profile_links = []

        self.run()

    def run(self):
        self.login()

        for search in self.searchs:
            self.goToPage("/gogole?q=" + search.replace(" ", "+"))
            self.scrollDown(10)
            self.getProfilesLinks()
        
        self.visitProfiles()

        print(str(len(self.profile_links)) + " visited profiles")

        self.close()

    def login(self):
        self.driver.get(self.base_domain)

        self.driver.find_element(By.XPATH, '//*[@id="btn-display-login"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="mail"]').send_keys(self.email)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.password)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/section/form/div[2]/button').click()

        print("Connected")

    def goToPage(self, uri):
        print("Go to page " + self.base_domain + uri)
        self.driver.get(self.base_domain + uri)

    def scrollDown(self, quantity):
        # Scroll down for discover all results
        for i in range(quantity):
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)

    def getProfilesLinks(self):
        selector = Selector(self.driver.page_source)
        for item in selector.xpath('//*[@id="grid-container"]//a[contains(@href, "/profile/")]/@href').getall():
            if not item.startswith(self.base_domain):
                item = self.base_domain + item
            self.profile_links.append(item)

    def visitProfiles(self):
        for link in list(set(self.profile_links)):
            print("Visit : " + link)
            self.driver.get(link)
            time.sleep(0.5)

    def close(self):
        self.driver.close()

AdopteUnMec()