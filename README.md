# 🎮 Steam Scraping Selenium 
Welcome to my open Steam Scraping open source Python project! 

As a PC Gamer and Data Geek this project is a labor of love that I have been working on for some time, and I am excited to share it with the world. As an open source project, anyone can access and contribute to the code, making it a collaborative effort with the potential to reach a wide audience. 

Through the use of Python programming language and Selenium, I have created a scraper that collects information about specific games and outputs it in a csv file for data uses. This project is designed to be user-friendly, efficient, and scalable, allowing for easy implementation and customization for a variety of use cases.

Whether you're a seasoned analyst or just starting out, I believe this project will be a valuable tool in your toolkit. I encourage you to explore the code, contribute your own ideas and improvements, and help make this project the best it can be. 

Thank you for your interest and support!

## 📖 Prerequisites
In order to run the scraper you will need `Python >= 3.9.0`, `Selenium >= 4.8.3`, `pandas >= 1.5.0` and `numpy >= 1.10.0` installed in your enviroment. You can install `requirements.txt` with:

```shell
pip install -r requirements.txt
```

You will also need a ChromeDriver in order to scrape with Selenium, you can get the current Browser Driver [here](https://chromedriver.chromium.org/downloads) and set it as your webdriver path.

An easy alternative is by installing `webdriver-manager >= 3.8.5`, method used in the scraper:

```shell
pip install webdriver-manager
```

Source code: [github](https://github.com/SergeyPirogov/webdriver_manager)

## 📃 Instructions

In order to import the scraper to your project use (Source code needs to be in the same folder):

```shell
from scraper import GetSteamGames
```

GetSteamGames() has 4 attributes:
```shell
GetSteamGames(ToScrape = 10, ToWait = 0.5, verbose = True, Scroll = 5)
```

**ToScrape :** ***int, default = 10***<br />
Number of games to scrape by the scraper

**ToWait :** ***float, default = 0.5***<br />
Time to wait for each scrape to finish, need to be equal or higher than 0.5

**verbose :** ***bool, default = True***<br />
Prints progress and information about the scraping

**Scroll :** ***int, default = 5***<br />
Times to scroll in the steam games website. Each scroll gets you about 20 games, from there you can select how many to scrape with `ToScrape`, example:

If you want a dataset with about 1000 samples, set `Scroll = 50` and `ToScrape = 1000`

## 🗳️ Output

The scraper outputs a `games.csv` file in the same folder containing the following data:

| Column        | Description   |
| ------------- |:-------------:|
| **GameName**      | The name of the game |
| **AgeRestriction**      | Whether or not the data has age restriction      |
| **GameDescription** | Steam Description about the game      |
| **Reviews** | Total reviews of the game      |
| **ReleaseDate** | Indicates the release day/month/year of the game       |
| **Developer** | Developer of the game      |
| **FullPrice** | Indicates the full price of the game without any discounts      |
| **DiscountedPrice** | Indicates the discounted price if there was a sale at the time of the scrape, if not value would be 0.      |
| **PEGI** | URL of an image with the PEGI rank, image url finish with */DEJUS/{rank}.png*     |
| **MetacriticScore** | Metacritic Score of the game if available     |
| **Type** | Indicates de tagged category of the game      |
| **LastUpdate** | Last time it was updated      |
| **GamesLanguages** | Number of languages available      |
| **GameFeatures** | A list containing Steam Features present in the game      |
| **DRM Notice** | Whether the user needs to sign a DRM or not      |
| **GameAchievements** | Number of Achievements the game has      |
| **CuratorReviews** | Number of Curator Reviews the game has      |

## ⚖️ License
MIT © [Steam-Scraping-Selenium](LICENSE)
