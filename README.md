# CFBRecruits (Python 2.7)

*Making NCAA football recruiting data as easily accessible as possible*

## Table of Contents

1. Introduction
2. Installation
   - Install Selenium
   - Install Selenium Google Chrome WebDriver
   - Install CFBRecruits
3. Using CFBRecruits
   - Classes
   - Methods
4. Appendix

### 1. Introduction

The CFBRecruits module was created to gain access to NCAA football recruit data without having to pay for 3rd party API access (which is often sparse, inconsistent, or simply non-existant). Currently, the two largest websites tracking college football recruits are 247sports.com and Rivals.com. Each website ranks both overall university recruiting classes and individual recruits on a state- and nation-wide basis. The CFBRecruits module utilizes Selenium 2.0 to effecitively navigate ever-shifting DOM elements to deliver the webpage's data to your machine in a readable and easily iterable fashion.

**Currently, the CFBRecruits module will return the following data from both websites:**

1. Complete university recruiting class data by year
2. Average university recruit rating by year
3. The Top 50 recruiting classes by university, by year

### 2. Installation

The CFBRecruit module relies heavily on Selenium 2.0, and specifically Selenium's Google Chrome WebDriver. Later in these instructions we'll touch on all aspects of WebDrivers, but for now, you'll want to start by simply installing Selenium on your machine. (***NOTE:*** *While I'll cover the high-level details below, please be sure to brush-up on [Selenium's documentation--especially if you're a Windows user for proper instructions!](https://selenium-python.readthedocs.io/installation.html)*)

#### First - Install Selenium

1. Open your Mac's terminal
2. Copy and paste: `pip install selenium`
3. Press enter/return

#### Second - Install Selenium Google Chrome WebDriver

1. [Click Here](https://sites.google.com/a/chromium.org/chromedriver/downloads) to navigate to the WebDriver download page
2. Click to download the "Latest Release" of the Selenium Google Chrome WebDriver
3. Click "chromedriver_mac64.zip"
4. Locate the downloaded .zip file
5. Open the .zip file
6. Move the "chromedriver" file to your desired folder/location--you'll need this exact file path later.

#### Third - Install CFBRecruits

### 3. Using CFBRecruits

#### Classes

There are currently two classes in CFBRecruits--one for 247Sports.com and one for Rivals.com--named `Scrape247()` and `ScrapeRivals()`, respectively. They are both children of the `Scraper()` parent class.

##### Creating a Class instance

In order to access all of the methods within each class, you'll first need to create an instance of the class for the website in question. For instance:

`site = ScrapeRivals()` or `site = Scrape247()`

Once you've created your class instance, you're now ready to begin utilizing the methods within each class.

#### Utilizing CFBRecruit's methods

Currently, each website's class has the following methods:

1. `getClassURL(team, year)` - Including the proper team name string (referenced in the appendix) and the desired year, this function will enable you to generate the proper URL to scrape without have to locate it on the website, copy it, and then paste it into any other methods.

Example:

`site = ScrapeRivals()
 page = site.getClassURL('tamu', 2012)`

2. `getClassData(url)` - 
3. `buildClassData(data)`
4. `avgClassRating(player_data)`
5. `teamRankings(year)`
