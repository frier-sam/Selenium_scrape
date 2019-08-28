

# import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from time import sleep 
from selenium.webdriver.common.by import By
class scrape:
    links =[]
    
    def getlinks(self,driver):
        
        soup = BeautifulSoup(driver.page_source)
        linkdivs = soup.findAll("i", {"class": "fas fa-home"})
        for i in linkdivs:
            self.links.append(self.base_domain+i.parent['href'])
        return
 
    def __init__(self,url,pages=10,sleeptime=7,base_domain = "https://www.kompas-villas.com"): 
        self.base_domain = base_domain
        driver = webdriver.Chrome("./chromedriver") 
        driver.get(url)
        sleep(sleeptime)

        self.getlinks(driver)
        # i=2
        # driver.find_element(By.XPATH,'//div[contains(@class, "aspPager")]/span/a[contains(text(),'+str(i)+')]').click()
        print("scraping the links from following pages")
        i = 2
        while i < pages:
            try:
                driver.find_element(By.XPATH,'//div[contains(@class, "aspPager")]/span/a[contains(text(),'+str(i)+')]').click()
                print(i)
                self.getlinks(driver)

            except:
                print('trying to clicking next')
                try:
                    driver.find_element(By.XPATH,'//div[contains(@class, "aspPager")]/span/a[contains(text(),"Next")]').click()
                    self.getlinks(driver)
                except:
                    print('unable to load any more pages')
                    pass
                pass
            i = i+1
            sleep(sleeptime)
        return
        




