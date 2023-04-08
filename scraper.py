from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def GetSteamGames(ToScrape = 10):

    ChromeDriver = 'chromedriver.exe'
    driver = webdriver.Chrome(executable_path = ChromeDriver)
    
    GamesName = list()
    
    driver.get('https://store.steampowered.com/search/?ignore_preferences=1&filter=topsellers')
    
    time.sleep(3)
    
    GamesBanner = driver.find_elements(By.CLASS_NAME,"search_result_row.ds_collapse_flag.app_impression_tracked")
    
    for item in GamesBanner:
        
        try:
            GameDriver = webdriver.Chrome(executable_path = ChromeDriver)
            GameDriver.get(f"{item.get_attribute('href')}")
            time.sleep(1)
            GamesName.append(GameDriver.find_element(By.CLASS_NAME, "apphub_AppName"))
        
        except:
            
            AgeRestriction = webdriver.Chrome(executable_path = ChromeDriver)
            AgeRestriction.get(f"{item.get_attribute('href')}")
            
            Select(AgeRestriction.find_element(By.NAME, "ageYear")).select_by_value('2000')
            SubmitButtom = AgeRestriction.find_element(By.CLASS_NAME, "btnv6_blue_hoverfade.btn_medium")
            SubmitButtom.click()
            
            # Fix Age Restriction
            
            #AgeRestriction.append(AgeRestriction.find_element(By.CLASS_NAME, "apphub_AppName"))
            
    return GamesName
        
print(GetSteamGames())