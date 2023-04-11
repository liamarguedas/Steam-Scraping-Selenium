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
    Metacritic = list()
    GameType = list()
    LastUpdate = list()
    GamesLanguages = list()
    GamesFeatures = list()
    
    
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
            GamePrice.append(GameDriver.find_element(By.XPATH, "//div[@class='game_purchase_action_bg']/div[@class='game_purchase_price price']").text)   

        except:
            GamePrice.append(GameDriver.find_element(By.XPATH, "//div[@class='discount_prices']/div[@class='discount_original_price']").text)

        # Discounted price
        try:
            if GamePrice[-1] in ['Gratuito para jogar', 'Gratuito p/ Jogar']:
                
                raise ValueError('Except to execute')
            else: 
                DiscountedPrice.append(GameDriver.find_element(By.XPATH, "//div[@class='discount_block game_purchase_discount']//div[@class='discount_final_price']").text)   
        except:
            DiscountedPrice.append('R$ 0,00') 
            
        # Game Rating (PEGI)
        try: 
            PEGIRating.append(GameDriver.find_element(By.XPATH, "//div[@class='game_rating_icon']/img").get_attribute("src"))  
        except:
            PEGIRating.append(np.nan) 
            
        # MetacriticScore
        try: 
            Metacritic.append(GameDriver.find_element(By.CLASS_NAME, "score").text)  
        except:
            Metacritic.append(np.nan) 
            
        # Genero
        try: 
            GameType.append(GameDriver.find_element(By.XPATH, "//div[@id='genresAndManufacturer']//span").text)  
        except:
            GameType.append(np.nan)  
        
        # Last update
        try: 
            LastUpdate.append(GameDriver.find_element(By.CLASS_NAME, "partnereventwebrowembed_LatestUpdateButton_3F6YM.Focusable").text)  
        except:
            LastUpdate.append(np.nan) 
        
        # Game Available Languages
        try: 
            GamesLanguages.append(GameDriver.find_element(By.CLASS_NAME, "all_languages").text)  
        except:
            GamesLanguages.append(np.nan) 
            
        # In-app purchases
        try: 
            GamesFeatures.append(GameDriver.find_elements(By.XPATH, "//div[@class='game_area_features_list_ctn']//div[@class='label']").text)  
        except:
            GamesFeatures.append(np.nan) 
            
        print(GamesFeatures)
        break
        # Valvi anti-cheat
        
        # Valve workshop
        
        
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
    'PEGI': PEGIRating,
    'MetacriticScore': Metacritic,
    'Type':GameType,
    'LastUpdate': LastUpdate}).to_csv('games.csv')
        
GetSteamGames()