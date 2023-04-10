from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import numpy as np

def PassAgeRestriction(Driver):
    
    # Select year 2000
    Select(Driver.find_element(By.NAME, "ageYear")).select_by_value('2000')
            
    # Click submit
    Driver.find_element(By.CLASS_NAME, "btnv6_blue_hoverfade.btn_medium").click()
    
def GetSteamGames(ToScrape = 10, ToWait = 2):
    
    GameName = list()
    AgeRestriction = list()
    GameDescription = list()
    GameReviews = list()
    ReviewSentiment = list()
    ReleaseDate = list()
    GameDeveloper = list()
    GamePrice = list()
    DiscountedPrice = list()
    PEGIRating = list()
    
    
    ChromeDriver = 'chromedriver.exe'
    driver = webdriver.Chrome(executable_path = ChromeDriver)
    
    driver.get('https://store.steampowered.com/search/?ignore_preferences=1&filter=topsellers')
    
    time.sleep(ToWait)
    
    # Find all listed games
    GamesBanner = driver.find_elements(By.CLASS_NAME,"search_result_row.ds_collapse_flag.app_impression_tracked")
    
    # For game in (Find all listed games)
    for item in GamesBanner:
        
        time.sleep(ToWait)
        
        # Get game URL to scrape
        GameDriver = webdriver.Chrome(executable_path = ChromeDriver)
        GameDriver.get(f"{item.get_attribute('href')}")
        time.sleep(ToWait)
        
        # Pass AgeRestriction if needed
        try: 
            PassAgeRestriction(Driver = GameDriver)
            AgeRestriction.append('Yes')
        except:
            AgeRestriction.append('No')
          
          
        time.sleep(ToWait)
        
        # Game name
        try: 
            GameName.append(GameDriver.find_element(By.CLASS_NAME, "apphub_AppName").text)   
        except: # In case of an error, introduced an NaN value.
            GameName.append(np.nan)
            
        # Game description
        try: 
            GameDescription.append(GameDriver.find_element(By.CLASS_NAME, "game_description_snippet").text)   
        except:
            GameDescription.append(np.nan)
            
        # Total reviews
        try: 
            GameReviews.append(GameDriver.find_element(By.CLASS_NAME, "user_reviews_summary_bar").text)   
        except:
            GameReviews.append(np.nan)
            
        # Reviews sentiment
        try: 
            ReviewSentiment.append(GameDriver.find_element(By.CLASS_NAME, "game_review_summary").text)   
        except:
            ReviewSentiment.append(np.nan)
             
        # Release date
        try: 
            ReleaseDate.append(GameDriver.find_element(By.CLASS_NAME, "date").text)   
        except:
            ReleaseDate.append(np.nan)
            
        # Game Developer
        try: 
            GameDeveloper.append(GameDriver.find_element(By.ID, "developers_list").text)   
        except:
            GameDeveloper.append(np.nan)
        
        # Original Price
        try:
            GamePrice.append(GameDriver.find_element(By.CLASS_NAME, "game_purchase_price.price").text)   
        except:
            GamePrice.append(GameDriver.find_element(By.CLASS_NAME, "discount_original_price").text)   
            

        # Discounted price
        try: 
            DiscountedPrice.append(GameDriver.find_element(By.CLASS_NAME, "discount_final_price").text)   
        except:
            DiscountedPrice.append('R$ 0,00') 
            
        # Game Rating (PEGI)
        try: 
            PEGIRating.append(GameDriver.find_element(By.CLASS_NAME, "game_rating_icon").get_attribute('src'))   
        except:
            PEGIRating.append(np.nan) 
            
        # FIX PEGI RATING
            
        # Genero
        
        # Close opened window
        GameDriver.quit()
        
    return pd.DataFrame({'Game' : GameName,
    'AgeRestriction': AgeRestriction,
    'GameDescription':GameDescription,
    'Reviews':GameReviews,
    'ReviewSentiment':ReviewSentiment,
    'ReleaseDate':ReleaseDate,
    'Developer':GameDeveloper,
    'FullPrice':GamePrice,
    'DiscountedPrice':DiscountedPrice,
    'PEGI': PEGIRating}).to_csv('games.csv')
        
GetSteamGames()