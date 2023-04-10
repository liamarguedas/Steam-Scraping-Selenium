from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import numpy as np



def PassAgeRestriction(Driver):
    
    # Select year 2000
    Select(Driver.find_element(By.NAME, "ageYear")).select_by_value('2000')
            
    # Click submit
    Driver.find_element(By.CLASS_NAME, "btnv6_blue_hoverfade.btn_medium").click()
    
    

def GetSteamGames(ToScrape = 10, ToWait = 3):
    
    GamesName = list()
    AgeRestriction = list()

    ChromeDriver = 'chromedriver.exe'
    driver = webdriver.Chrome(executable_path = ChromeDriver)
    
    driver.get('https://store.steampowered.com/search/?ignore_preferences=1&filter=topsellers')
    
    time.sleep(ToWait)
    
    # Find all listed games
    GamesBanner = driver.find_elements(By.CLASS_NAME,"search_result_row.ds_collapse_flag.app_impression_tracked")
    
    # For game in (Find all listed games)
    for item in GamesBanner:
        
        # Get game URL to scrape
        GameDriver = webdriver.Chrome(executable_path = ChromeDriver)
        GameDriver.get(f"{item.get_attribute('href')}")
        time.sleep(ToWait)
        
        try: # Pass AgeRestriction if needed
            PassAgeRestriction(Driver = GameDriver)
            AgeRestriction.append(1)
        except:
            AgeRestriction.append(0)
          
        time.sleep(ToWait)
        
        try: # Save game name
            GamesName.append(GameDriver.find_element(By.CLASS_NAME, "apphub_AppName").text)   
        except: # In case of an error, introduced an NaN value.
            GamesName.append(np.nan)
     
    return GamesName
        
print(GetSteamGames())