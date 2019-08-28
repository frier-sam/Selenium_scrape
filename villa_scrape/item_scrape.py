

# import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from time import sleep 
from selenium.webdriver.common.by import By
class scrape:
    links =[]
    
    def getinfo(self,loc,dic):
            for it in loc.find_all('li'):
                value = it.span.text.strip()
                name = it.text.strip().replace(value,'').strip()
                if value == '':
                    if it.span.i:
                        if it.span.i['class'] == ['fas', 'fa-check']:
                            value  = 'Yes'
                        else:
                            value = 'No'
                dic[name]=value
            return dic
 
    def __init__(self,links,sleeptime=7): 
       
        
        data = []
        driver = webdriver.Chrome("./chromedriver") 
        for i in links:
            driver.get(i)
            soup = BeautifulSoup(driver.page_source)
            topinfo = {}
            details = {}
            price = soup.find("div", {"class" : "price"}).text
            topinfo = self.getinfo(soup.find("ul", {"class" : "info-ul"}),topinfo)

            for di in soup.findAll("div", {"class" : "infoDetails"}):
                details = self.getinfo(di,details)
            data.append({"url":i,"price":price,"topinfo":topinfo,"details":details})
        
        self.data = data
        return
        









