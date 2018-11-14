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

1. `getClassURL(team, year)` - Including the proper team name string (please reference the appendix for all proper team name strings) and the desired year, this function will enable you to generate the proper URL string to pass into methods to then be scraped without having to manually locate it on the website, copy it, and then paste it into any other methods (which, will also work, if you so desire).

*Example:*

```
site = ScrapeRivals()
url = site.getClassURL('tamu', 2012)

print url
...
https://tamu.rivals.com/commitments/football/2012
```

2. `getClassData(url)` - This method does all of the heavy lifting to scrape the URL in question and returns the initial data sets in a tuple (`(data_fields, team_player_data, index_iterator)`) that will later be massaged into more readable and iterable data objects.

*Example:*

```
site = ScrapeRivals()
url = site.getClassURL('tamu', 2012)
class_data = site.getClassData(url)

print class_data
...
(['Name', 'Position', 'Location', 'Height', 'Weight', 'Rating', 'Commit Date', 'Status'], [u'Thomas Johnson', u'WR', u'Dallas, TX', u'6\'0"', u'180', u'6', u'2/2/12', u'SIGNED', u'Edmund Ray', u'DT', u'St. Louis, MO', u'6\'5"', u'290', u'5.6', u'2/1/12', u'SIGNED', u'Polo Manukainiu', u'DE', u'Euless, TX', u'6\'6"', u'256', u'5.7', u'1/30/12', u'SIGNED', u'Edward Pope', u'ATH', u'Carthage, TX', u'6\'3"', u'170', u'5.8', u'1/28/12', u'SIGNED', u'Sabian Holmes', u'WR', u'Southlake, TX', u'5\'11"', u'175', u'5.5', u'1/9/12', u'SIGNED', u'Derel Walker', u'WR', u'Athens, TX', u'6\'2"', u'175', u'5.7', u'12/23/11', u'SIGNED', u'Otis Jacobs', u'DB', u'Perkinston, MS', u'6\'1"', u'180', u'5.7', u'12/22/11', u'SIGNED', u'Germain Ifedi', u'OL', u'Houston, TX', u'6\'5"', u'304', u'5.7', u'10/26/11', u'SIGNED', u'Julien Obioha', u'DE', u'New Orleans, LA', u'6\'4"', u'255', u'5.6', u'7/29/11', u'SIGNED', u'Kenneth Marshall', u'DB', u'South Houston, TX', u'6\'0"', u'191', u'5.6', u'6/14/11', u'SIGNED', u'Trey Williams', u'RB', u'Spring, TX', u'5\'8"', u'175', u'6.1', u'4/17/11', u'SIGNED', u'Matt Davis', u'QB', u'Houston, TX', u'6\'2"', u'202', u'5.8', u'4/17/11', u'SIGNED', u'Mike Matthews', u'OL', u'Missouri City, TX', u'6\'3"', u'260', u'5.8', u'2/24/11', u'SIGNED', u'Alonzo Williams', u'DE', u'Long Beach, CA', u'6\'4"', u'248', u'5.6', u'2/24/11', u'SIGNED', u'Kimo Tipoti', u'OL', u'Hurst, TX', u'6\'3"', u'330', u'5.7', u'2/21/11', u'SIGNED', u'Jordan Richmond', u'LB', u'Denton, TX', u'6\'1"', u'220', u'5.8', u'2/21/11', u'SIGNED', u'Michael Richardson', u'DE', u'DeSoto, TX', u'6\'2"', u'228', u'5.7', u'2/19/11', u'SIGNED', u'Tyrone Taylor', u'DE', u'Galena Park, TX', u'6\'3"', u'210', u'5.6', u'12/19/10', u'SIGNED', u'DeVante Harris', u'DB', u'Mesquite, TX', u'5\'11"', u'160', u'5.9', u'(No Date)', u'SIGNED'], 8)
```

3. `buildClassData(data)`

*Example:*

```
site = ScrapeRivals()
url = site.getClassURL('tamu', 2012)
class_data = site.getClassData(url)
final_class_data = site.buildClassData(class_data)

print final_class_data
...
[{'Status': u'SIGNED', 'Rating': u'6', 'Name': u'Thomas Johnson', 'Weight': u'180', 'Height': u'6\'0"', 'Location': u'Dallas, TX', 'Position': u'WR', 'Commit Date': u'2/2/12'}, {'Status': u'SIGNED', 'Rating': u'5.6', 'Name': u'Edmund Ray', 'Weight': u'290', 'Height': u'6\'5"', 'Location': u'St. Louis, MO', 'Position': u'DT', 'Commit Date': u'2/1/12'}, {'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Polo Manukainiu', 'Weight': u'256', 'Height': u'6\'6"', 'Location': u'Euless, TX', 'Position': u'DE', 'Commit Date': u'1/30/12'}, {'Status': u'SIGNED', 'Rating': u'5.8', 'Name': u'Edward Pope', 'Weight': u'170', 'Height': u'6\'3"', 'Location': u'Carthage, TX', 'Position': u'ATH', 'Commit Date': u'1/28/12'}, {'Status': u'SIGNED', 'Rating': u'5.5', 'Name': u'Sabian Holmes', 'Weight': u'175', 'Height': u'5\'11"', 'Location': u'Southlake, TX', 'Position': u'WR', 'Commit Date': u'1/9/12'}, {'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Derel Walker', 'Weight': u'175', 'Height': u'6\'2"', 'Location': u'Athens, TX', 'Position': u'WR', 'Commit Date': u'12/23/11'}, {'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Otis Jacobs', 'Weight': u'180', 'Height': u'6\'1"', 'Location': u'Perkinston, MS', 'Position': u'DB', 'Commit Date': u'12/22/11'}, {'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Germain Ifedi', 'Weight': u'304', 'Height': u'6\'5"', 'Location': u'Houston, TX', 'Position': u'OL', 'Commit Date': u'10/26/11'}, {'Status': u'SIGNED', 'Rating': u'5.6', 'Name': u'Julien Obioha', 'Weight': u'255', 'Height': u'6\'4"', 'Location': u'New Orleans, LA', 'Position': u'DE', 'Commit Date': u'7/29/11'}, {'Status': u'SIGNED', 'Rating': u'5.6', 'Name': u'Kenneth Marshall', 'Weight': u'191', 'Height': u'6\'0"', 'Location': u'South Houston, TX', 'Position': u'DB', 'Commit Date': u'6/14/11'}, {'Status': u'SIGNED', 'Rating': u'6.1', 'Name': u'Trey Williams', 'Weight': u'175', 'Height': u'5\'8"', 'Location': u'Spring, TX', 'Position': u'RB', 'Commit Date': u'4/17/11'}, {'Status': u'SIGNED', 'Rating': u'5.8', 'Name': u'Matt Davis', 'Weight': u'202', 'Height': u'6\'2"', 'Location': u'Houston, TX', 'Position': u'QB', 'Commit Date': u'4/17/11'}, {'Status': u'SIGNED', 'Rating': u'5.8', 'Name': u'Mike Matthews', 'Weight': u'260', 'Height': u'6\'3"', 'Location': u'Missouri City, TX', 'Position': u'OL', 'Commit Date': u'2/24/11'}, {'Status': u'SIGNED', 'Rating': u'5.6', 'Name': u'Alonzo Williams', 'Weight': u'248', 'Height': u'6\'4"', 'Location': u'Long Beach, CA', 'Position': u'DE', 'Commit Date': u'2/24/11'}, {'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Kimo Tipoti', 'Weight': u'330', 'Height': u'6\'3"', 'Location': u'Hurst, TX', 'Position': u'OL', 'Commit Date': u'2/21/11'}, {'Status': u'SIGNED', 'Rating': u'5.8', 'Name': u'Jordan Richmond', 'Weight': u'220', 'Height': u'6\'1"', 'Location': u'Denton, TX', 'Position': u'LB', 'Commit Date': u'2/21/11'}, {'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Michael Richardson', 'Weight': u'228', 'Height': u'6\'2"', 'Location': u'DeSoto, TX', 'Position': u'DE', 'Commit Date': u'2/19/11'}, {'Status': u'SIGNED', 'Rating': u'5.6', 'Name': u'Tyrone Taylor', 'Weight': u'210', 'Height': u'6\'3"', 'Location': u'Galena Park, TX', 'Position': u'DE', 'Commit Date': u'12/19/10'}, {'Status': u'SIGNED', 'Rating': u'5.9', 'Name': u'DeVante Harris', 'Weight': u'160', 'Height': u'5\'11"', 'Location': u'Mesquite, TX', 'Position': u'DB', 'Commit Date': u'(No Date)'}]
```

4. `avgClassRating(player_data)`
5. `teamRankings(year)`
