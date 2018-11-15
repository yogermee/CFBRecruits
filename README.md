# CFBRecruits *Beta* (written in Python 2.7)

*Making NCAA football recruiting data as easily accessible as possible.*

# Table of Contents

1. Introduction
2. Installation
   - Install Selenium
   - Install Selenium Google Chrome WebDriver
   - Install CFBRecruits
3. Using CFBRecruits
   - Classes
     - Creating a Class instance
   - Utilizing CFBRecruit's Methods
     - `getClassURL(team, year)`
     - `getClassData(url)`
     - `buildClassData(data)`
     - `avgClassRating(player_data)`
     - `teamRankings(year)`
     
4. Appendix

## 1. Introduction

The CFBRecruits module was created to gain access to NCAA football recruit data without having to pay for 3rd party API access (which is often sparse, inconsistent, or simply non-existant). Currently, the two largest websites tracking college football recruits are 247sports.com and Rivals.com. Each website ranks both overall university recruiting classes and individual recruits on a state- and nation-wide basis. The CFBRecruits module utilizes Selenium 2.0 to effecitively navigate ever-shifting DOM elements to deliver the webpage's data to your machine in a readable and easily iterable fashion.

**Currently, the CFBRecruits module will return the following data from both websites:**

1. Complete university recruiting class data by year
2. Average university recruit rating by year
3. The Top 50 recruiting classes by university, by year

## 2. Installation

The CFBRecruit module relies heavily on Selenium 2.0, and specifically Selenium's Google Chrome WebDriver. Later in these instructions we'll touch on all aspects of WebDrivers, but for now, you'll want to start by simply installing Selenium on your machine. (***NOTE:*** *While I'll cover the high-level details below, please be sure to brush-up on [Selenium's documentation--especially if you're a Windows user for proper instructions!](https://selenium-python.readthedocs.io/installation.html)*)

### First - Install Selenium

1. Open your Mac's terminal
2. Copy and paste: `pip install selenium`
3. Press enter/return

### Second - Install Selenium Google Chrome WebDriver

1. [Click Here](https://sites.google.com/a/chromium.org/chromedriver/downloads) to navigate to the WebDriver download page
2. Click to download the "Latest Release" of the Selenium Google Chrome WebDriver
3. Click "chromedriver_mac64.zip"
4. Locate the downloaded .zip file
5. Open the .zip file
6. Move the "chromedriver" file to your desired folder/location--you'll need this exact file path later.

### Third - Install CFBRecruits

#### A brief moment on WebDrivers:

If you're familiar with Selenium, you may already know that you can use WebDrivers for basically any browser (Firefox, Chrome, Opera, etc.), and perhaps, Google Chrome isn't your browser of choice (which is what the CFBRecruits module utilizes). What you can do is [visit Selenium's WebDriver download page](https://selenium-python.readthedocs.io/installation.html#drivers), download the WebDriver of your choice, and then follow steps 3-6 from "Second - Install Selenium Google Chrome WebDriver" but for the WebDriver of your choice.

Once you've done this--and this goes for any WebDriver--be sure to capture the exact file path of your WebDriver as you'll need it for Step 7 below:

1. Download "CFBRecruits.py" from the CFBRecruits repository

*Note: If you choose to use a different browser WebDriver, you'll need to chose the proper WebDriver object. For instance, if you'd prefer to use Firefox, instead of "`webdriver.Chrome()`" you'll want to change each reference to a specific WebDriver in "CFBRecruits.py" to "`webdriver.Firefox()`".

## 3. Using CFBRecruits

### Classes

There are currently two classes in CFBRecruits--one for 247Sports.com and one for Rivals.com--named `Scrape247(path)` and `ScrapeRivals(path)`, respectively. They are both children of the `Scraper(path)` parent class.

#### Creating a Class instance
'Step zero', if you will, is establishing your Google Chrome WebDriver local file path as a variable to pass into either module.

*Example:*

```
path = "INSERT YOUR WEB DRIVER'S LOCAL FILE PATH HERE"
```

In order to access all of the methods within each class, you'll first need to create an instance of the class for the website in question. For instance:

```
path = "INSERT YOUR WEB DRIVER'S LOCAL FILE PATH HERE"
site = ScrapeRivals(path)` # or `site = Scrape247(path)
```
Once you've created your path variable and class instance, you're now ready to begin utilizing the methods within each class.

### Utilizing CFBRecruit's methods

Currently, each website's class has the following methods:

1. `getClassURL(team, year)` - Including the proper team name string (please reference the appendix for all proper team name strings) and the desired year, this function will enable you to generate the proper URL string to pass into methods to then be scraped without having to manually locate it on the website, copy it, and then paste it into any other methods (which would also work in the `getClassData(url)` method, if you so desire).

*Example:*

```
path = "INSERT YOUR WEB DRIVER'S LOCAL FILE PATH HERE"
site = ScrapeRivals(path)
url = site.getClassURL('tamu', 2012)

print url
...
https://tamu.rivals.com/commitments/football/2012
```

2. `getClassData(url)` - This method does all of the heavy lifting to scrape the URL in question and returns the initial data sets in a tuple (`(data_fields, team_player_data, index_iterator)`) that will later be massaged into more readable and iterable data objects.

*Example:*

```
path = "INSERT YOUR WEB DRIVER'S LOCAL FILE PATH HERE"
site = ScrapeRivals(path)
url = site.getClassURL('tamu', 2012)
class_data = site.getClassData(url)

print class_data
...
(['Name', 'Position', 'Location', 'Height', 'Weight', 'Rating', 'Commit Date', 'Status'], [u'Thomas Johnson', u'WR', u'Dallas, TX', u'6\'0"', u'180', u'6', u'2/2/12', u'SIGNED', u'Edmund Ray', u'DT', u'St. Louis, MO', u'6\'5"', u'290', u'5.6', u'2/1/12', u'SIGNED', u'Polo Manukainiu', u'DE', u'Euless, TX', u'6\'6"', u'256', u'5.7', u'1/30/12', u'SIGNED', u'Edward Pope', u'ATH', u'Carthage, TX', u'6\'3"', u'170', u'5.8', u'1/28/12', u'SIGNED', u'Sabian Holmes', u'WR', u'Southlake, TX', u'5\'11"', u'175', u'5.5', u'1/9/12', u'SIGNED', u'Derel Walker', u'WR', u'Athens, TX', u'6\'2"', u'175', u'5.7', u'12/23/11', u'SIGNED', u'Otis Jacobs', u'DB', u'Perkinston, MS', u'6\'1"', u'180', u'5.7', u'12/22/11', u'SIGNED', u'Germain Ifedi', u'OL', u'Houston, TX', u'6\'5"', u'304', u'5.7', u'10/26/11', u'SIGNED', u'Julien Obioha', u'DE', u'New Orleans, LA', u'6\'4"', u'255', u'5.6', u'7/29/11', u'SIGNED', u'Kenneth Marshall', u'DB', u'South Houston, TX', u'6\'0"', u'191', u'5.6', u'6/14/11', u'SIGNED', u'Trey Williams', u'RB', u'Spring, TX', u'5\'8"', u'175', u'6.1', u'4/17/11', u'SIGNED', u'Matt Davis', u'QB', u'Houston, TX', u'6\'2"', u'202', u'5.8', u'4/17/11', u'SIGNED', u'Mike Matthews', u'OL', u'Missouri City, TX', u'6\'3"', u'260', u'5.8', u'2/24/11', u'SIGNED', u'Alonzo Williams', u'DE', u'Long Beach, CA', u'6\'4"', u'248', u'5.6', u'2/24/11', u'SIGNED', u'Kimo Tipoti', u'OL', u'Hurst, TX', u'6\'3"', u'330', u'5.7', u'2/21/11', u'SIGNED', u'Jordan Richmond', u'LB', u'Denton, TX', u'6\'1"', u'220', u'5.8', u'2/21/11', u'SIGNED', u'Michael Richardson', u'DE', u'DeSoto, TX', u'6\'2"', u'228', u'5.7', u'2/19/11', u'SIGNED', u'Tyrone Taylor', u'DE', u'Galena Park, TX', u'6\'3"', u'210', u'5.6', u'12/19/10', u'SIGNED', u'DeVante Harris', u'DB', u'Mesquite, TX', u'5\'11"', u'160', u'5.9', u'(No Date)', u'SIGNED'], 8)
```

3. `buildClassData(data)` - This method will take the previously generated `class_data` and turn each player's data into a dictionary where the key is a data type and the value is the actual data value.

*Example:*

```
path = "INSERT YOUR WEB DRIVER'S LOCAL FILE PATH HERE"
site = ScrapeRivals(path)
url = site.getClassURL('tamu', 2012)
class_data = site.getClassData(url)
final_class_data = site.buildClassData(class_data)

print final_class_data
...
[{'Status': u'SIGNED', 'Rating': u'6', 'Name': u'Thomas Johnson', 'Weight': u'180', 'Height': u'6\'0"', 'Location': u'Dallas, TX', 'Position': u'WR', 'Commit Date': u'2/2/12'}, {'Status': u'SIGNED', 'Rating': u'5.6', 'Name': u'Edmund Ray', 'Weight': u'290', 'Height': u'6\'5"', 'Location': u'St. Louis, MO', 'Position': u'DT', 'Commit Date': u'2/1/12'}, {'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Polo Manukainiu', 'Weight': u'256', 'Height': u'6\'6"', 'Location': u'Euless, TX', 'Position': u'DE', 'Commit Date': u'1/30/12'}, {'Status': u'SIGNED', 'Rating': u'5.8', 'Name': u'Edward Pope', 'Weight': u'170', 'Height': u'6\'3"', 'Location': u'Carthage, TX', 'Position': u'ATH', 'Commit Date': u'1/28/12'}, {'Status': u'SIGNED', 'Rating': u'5.5', 'Name': u'Sabian Holmes', 'Weight': u'175', 'Height': u'5\'11"', 'Location': u'Southlake, TX', 'Position': u'WR', 'Commit Date': u'1/9/12'}, {'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Derel Walker', 'Weight': u'175', 'Height': u'6\'2"', 'Location': u'Athens, TX', 'Position': u'WR', 'Commit Date': u'12/23/11'}, {'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Otis Jacobs', 'Weight': u'180', 'Height': u'6\'1"', 'Location': u'Perkinston, MS', 'Position': u'DB', 'Commit Date': u'12/22/11'}, {'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Germain Ifedi', 'Weight': u'304', 'Height': u'6\'5"', 'Location': u'Houston, TX', 'Position': u'OL', 'Commit Date': u'10/26/11'}, {'Status': u'SIGNED', 'Rating': u'5.6', 'Name': u'Julien Obioha', 'Weight': u'255', 'Height': u'6\'4"', 'Location': u'New Orleans, LA', 'Position': u'DE', 'Commit Date': u'7/29/11'}, {'Status': u'SIGNED', 'Rating': u'5.6', 'Name': u'Kenneth Marshall', 'Weight': u'191', 'Height': u'6\'0"', 'Location': u'South Houston, TX', 'Position': u'DB', 'Commit Date': u'6/14/11'}, {'Status': u'SIGNED', 'Rating': u'6.1', 'Name': u'Trey Williams', 'Weight': u'175', 'Height': u'5\'8"', 'Location': u'Spring, TX', 'Position': u'RB', 'Commit Date': u'4/17/11'}, {'Status': u'SIGNED', 'Rating': u'5.8', 'Name': u'Matt Davis', 'Weight': u'202', 'Height': u'6\'2"', 'Location': u'Houston, TX', 'Position': u'QB', 'Commit Date': u'4/17/11'}, {'Status': u'SIGNED', 'Rating': u'5.8', 'Name': u'Mike Matthews', 'Weight': u'260', 'Height': u'6\'3"', 'Location': u'Missouri City, TX', 'Position': u'OL', 'Commit Date': u'2/24/11'}, {'Status': u'SIGNED', 'Rating': u'5.6', 'Name': u'Alonzo Williams', 'Weight': u'248', 'Height': u'6\'4"', 'Location': u'Long Beach, CA', 'Position': u'DE', 'Commit Date': u'2/24/11'}, {'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Kimo Tipoti', 'Weight': u'330', 'Height': u'6\'3"', 'Location': u'Hurst, TX', 'Position': u'OL', 'Commit Date': u'2/21/11'}, {'Status': u'SIGNED', 'Rating': u'5.8', 'Name': u'Jordan Richmond', 'Weight': u'220', 'Height': u'6\'1"', 'Location': u'Denton, TX', 'Position': u'LB', 'Commit Date': u'2/21/11'}, {'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Michael Richardson', 'Weight': u'228', 'Height': u'6\'2"', 'Location': u'DeSoto, TX', 'Position': u'DE', 'Commit Date': u'2/19/11'}, {'Status': u'SIGNED', 'Rating': u'5.6', 'Name': u'Tyrone Taylor', 'Weight': u'210', 'Height': u'6\'3"', 'Location': u'Galena Park, TX', 'Position': u'DE', 'Commit Date': u'12/19/10'}, {'Status': u'SIGNED', 'Rating': u'5.9', 'Name': u'DeVante Harris', 'Weight': u'160', 'Height': u'5\'11"', 'Location': u'Mesquite, TX', 'Position': u'DB', 'Commit Date': u'(No Date)'}]
```
The value returned is a list of dictionaries that can be easily iterated through. For example:

```
site = ScrapeRivals()
url = site.getClassURL('tamu', 2012)
class_data = site.getClassData(url)
final_class_data = site.buildClassData(class_data)

for player in final_class_data:
	print player
...
{'Status': u'SIGNED', 'Rating': u'6', 'Name': u'Thomas Johnson', 'Weight': u'180', 'Height': u'6\'0"', 'Location': u'Dallas, TX', 'Position': u'WR', 'Commit Date': u'2/2/12'}
{'Status': u'SIGNED', 'Rating': u'5.6', 'Name': u'Edmund Ray', 'Weight': u'290', 'Height': u'6\'5"', 'Location': u'St. Louis, MO', 'Position': u'DT', 'Commit Date': u'2/1/12'}
{'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Polo Manukainiu', 'Weight': u'256', 'Height': u'6\'6"', 'Location': u'Euless, TX', 'Position': u'DE', 'Commit Date': u'1/30/12'}
{'Status': u'SIGNED', 'Rating': u'5.8', 'Name': u'Edward Pope', 'Weight': u'170', 'Height': u'6\'3"', 'Location': u'Carthage, TX', 'Position': u'ATH', 'Commit Date': u'1/28/12'}
{'Status': u'SIGNED', 'Rating': u'5.5', 'Name': u'Sabian Holmes', 'Weight': u'175', 'Height': u'5\'11"', 'Location': u'Southlake, TX', 'Position': u'WR', 'Commit Date': u'1/9/12'}
{'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Derel Walker', 'Weight': u'175', 'Height': u'6\'2"', 'Location': u'Athens, TX', 'Position': u'WR', 'Commit Date': u'12/23/11'}
{'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Otis Jacobs', 'Weight': u'180', 'Height': u'6\'1"', 'Location': u'Perkinston, MS', 'Position': u'DB', 'Commit Date': u'12/22/11'}
{'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Germain Ifedi', 'Weight': u'304', 'Height': u'6\'5"', 'Location': u'Houston, TX', 'Position': u'OL', 'Commit Date': u'10/26/11'}
{'Status': u'SIGNED', 'Rating': u'5.6', 'Name': u'Julien Obioha', 'Weight': u'255', 'Height': u'6\'4"', 'Location': u'New Orleans, LA', 'Position': u'DE', 'Commit Date': u'7/29/11'}
{'Status': u'SIGNED', 'Rating': u'5.6', 'Name': u'Kenneth Marshall', 'Weight': u'191', 'Height': u'6\'0"', 'Location': u'South Houston, TX', 'Position': u'DB', 'Commit Date': u'6/14/11'}
{'Status': u'SIGNED', 'Rating': u'6.1', 'Name': u'Trey Williams', 'Weight': u'175', 'Height': u'5\'8"', 'Location': u'Spring, TX', 'Position': u'RB', 'Commit Date': u'4/17/11'}
{'Status': u'SIGNED', 'Rating': u'5.8', 'Name': u'Matt Davis', 'Weight': u'202', 'Height': u'6\'2"', 'Location': u'Houston, TX', 'Position': u'QB', 'Commit Date': u'4/17/11'}
{'Status': u'SIGNED', 'Rating': u'5.8', 'Name': u'Mike Matthews', 'Weight': u'260', 'Height': u'6\'3"', 'Location': u'Missouri City, TX', 'Position': u'OL', 'Commit Date': u'2/24/11'}
{'Status': u'SIGNED', 'Rating': u'5.6', 'Name': u'Alonzo Williams', 'Weight': u'248', 'Height': u'6\'4"', 'Location': u'Long Beach, CA', 'Position': u'DE', 'Commit Date': u'2/24/11'}
{'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Kimo Tipoti', 'Weight': u'330', 'Height': u'6\'3"', 'Location': u'Hurst, TX', 'Position': u'OL', 'Commit Date': u'2/21/11'}
{'Status': u'SIGNED', 'Rating': u'5.8', 'Name': u'Jordan Richmond', 'Weight': u'220', 'Height': u'6\'1"', 'Location': u'Denton, TX', 'Position': u'LB', 'Commit Date': u'2/21/11'}
{'Status': u'SIGNED', 'Rating': u'5.7', 'Name': u'Michael Richardson', 'Weight': u'228', 'Height': u'6\'2"', 'Location': u'DeSoto, TX', 'Position': u'DE', 'Commit Date': u'2/19/11'}
{'Status': u'SIGNED', 'Rating': u'5.6', 'Name': u'Tyrone Taylor', 'Weight': u'210', 'Height': u'6\'3"', 'Location': u'Galena Park, TX', 'Position': u'DE', 'Commit Date': u'12/19/10'}
{'Status': u'SIGNED', 'Rating': u'5.9', 'Name': u'DeVante Harris', 'Weight': u'160', 'Height': u'5\'11"', 'Location': u'Mesquite, TX', 'Position': u'DB', 'Commit Date': u'(No Date)'}
```
And, by iterating the .iteritems() function, you can iterate through the actual dictionary and extract the data value you'd like based on the key. For instance:

```
for item in final_class_data:
	for key, value in item.iteritems():
		if key == "Name":
			print value
		else:
			pass
...
Thomas Johnson
Edmund Ray
Polo Manukainiu
Edward Pope
Sabian Holmes
Derel Walker
Otis Jacobs
Germain Ifedi
Julien Obioha
Kenneth Marshall
Trey Williams
Matt Davis
Mike Matthews
Alonzo Williams
Kimo Tipoti
Jordan Richmond
Michael Richardson
Tyrone Taylor
DeVante Harris
```

4. `avgClassRating(player_data)` - This allows you to extract the average rating for the class at the URL you're querying, returning a simple float value denoting that average

*Example:*

```
path = "INSERT YOUR WEB DRIVER'S LOCAL FILE PATH HERE"
site = ScrapeRivals(path)
url = site.getClassURL('tamu', 2012)
class_data = site.getClassData(url)
final_class_data = site.buildClassData(class_data)

print site.avgClassRating(final_class_data)
...
5.73
```

5. `teamRankings(year)` - For 247Sports.com or Rivals.com, you can easily retrieve the overall recruiting class rankings by univeristy (*Note:* 247Sports.com returns the top 50 recruiting classes, while Rivals.com returns the top 100 recruiting classes). Similar to individual university recruiting class data, this method returns a list of dictionaries for easy readability.

*Example:*

```
path = "INSERT YOUR WEB DRIVER'S LOCAL FILE PATH HERE"
site = ScrapeRivals(path)

print site.teamRankings(2012)
...
[{'Current Rank': '1', 'Total Commits': '26', 'Total Points': '2621', '3-Stars': '9', '5-Stars': '3', 'Team': 'Alabama', '4-Stars': '14', 'Average Rating': '3.77'}, {'Current Rank': '2', 'Total Commits': '28', 'Total Points': '2481', '3-Stars': '10', '5-Stars': '2', 'Team': 'Texas', '4-Stars': '15', 'Average Rating': '3.64'}, {'Current Rank': '3', 'Total Commits': '22', 'Total Points': '2421', '3-Stars': '8', '5-Stars': '3', 'Team': 'Florida', '4-Stars': '10', 'Average Rating': '3.68'}, {'Current Rank': '4', 'Total Commits': '25', 'Total Points': '2382', '3-Stars': '9', '5-Stars': '2', 'Team': 'Ohio State', '4-Stars': '14', 'Average Rating': '3.72'}, {'Current Rank': '5', 'Total Commits': '22', 'Total Points': '2297', '3-Stars': '9', '5-Stars': '3', 'Team': 'Stanford', '4-Stars': '10', 'Average Rating': '3.73'}, {'Current Rank': '6', 'Total Commits': '19', 'Total Points': '2263', '3-Stars': '5', '5-Stars': '3', 'Team': 'Florida State', '4-Stars': '10', 'Average Rating': '3.79'}, {'Current Rank': '7', 'Total Commits': '25', 'Total Points': '2132', '3-Stars': '13', '5-Stars': '2', 'Team': 'Michigan', '4-Stars': '10', 'Average Rating': '3.56'}, {'Current Rank': '8', 'Total Commits': '16', 'Total Points': '2040', '3-Stars': '2', '5-Stars': '3', 'Team': 'USC', '4-Stars': '10', 'Average Rating': '3.81'}, {'Current Rank': '9', 'Total Commits': '33', 'Total Points': '1975', '3-Stars': '23', '5-Stars': '2', 'Team': 'Miami (FL)', '4-Stars': '8', 'Average Rating': '3.36'}, {'Current Rank': '10', 'Total Commits': '21', 'Total Points': '1951', '3-Stars': '8', '5-Stars': '0', 'Team': 'Auburn', '4-Stars': '13', 'Average Rating': '3.62'}, {'Current Rank': '11', 'Total Commits': '25', 'Total Points': '1937', '3-Stars': '14', '5-Stars': '1', 'Team': 'Oklahoma', '4-Stars': '10', 'Average Rating': '3.48'}, {'Current Rank': '12', 'Total Commits': '19', 'Total Points': '1775', '3-Stars': '10', '5-Stars': '2', 'Team': 'Georgia', '4-Stars': '6', 'Average Rating': '3.47'}, {'Current Rank': '13', 'Total Commits': '26', 'Total Points': '1731', '3-Stars': '14', '5-Stars': '1', 'Team': 'UCLA', '4-Stars': '8', 'Average Rating': '3.27'}, {'Current Rank': '14', 'Total Commits': '20', 'Total Points': '1680', '3-Stars': '11', '5-Stars': '0', 'Team': 'Clemson', '4-Stars': '9', 'Average Rating': '3.45'}, {'Current Rank': '15', 'Total Commits': '19', 'Total Points': '1647', '3-Stars': '12', '5-Stars': '1', 'Team': 'Texas A&M', '4-Stars': '6', 'Average Rating': '3.42'}, {'Current Rank': '16', 'Total Commits': '21', 'Total Points': '1641', '3-Stars': '9', '5-Stars': '0', 'Team': 'Oregon', '4-Stars': '10', 'Average Rating': '3.38'}, {'Current Rank': '17', 'Total Commits': '22', 'Total Points': '1595', '3-Stars': '9', '5-Stars': '0', 'Team': 'Tennessee', '4-Stars': '11', 'Average Rating': '3.41'}, {'Current Rank': '18', 'Total Commits': '23', 'Total Points': '1567', '3-Stars': '12', '5-Stars': '0', 'Team': 'LSU', '4-Stars': '9', 'Average Rating': '3.22'}, {'Current Rank': '19', 'Total Commits': '25', 'Total Points': '1534', '3-Stars': '15', '5-Stars': '0', 'Team': 'South Carolina', '4-Stars': '8', 'Average Rating': '3.24'}, {'Current Rank': '20', 'Total Commits': '17', 'Total Points': '1521', '3-Stars': '7', '5-Stars': '1', 'Team': 'Notre Dame', '4-Stars': '8', 'Average Rating': '3.53'}, {'Current Rank': '21', 'Total Commits': '25', 'Total Points': '1452', '3-Stars': '14', '5-Stars': '1', 'Team': 'Washington', '4-Stars': '5', 'Average Rating': '3.08'}, {'Current Rank': '22', 'Total Commits': '28', 'Total Points': '1429', '3-Stars': '19', '5-Stars': '0', 'Team': 'Virginia Tech', '4-Stars': '7', 'Average Rating': '3.18'}, {'Current Rank': '23', 'Total Commits': '19', 'Total Points': '1316', '3-Stars': '9', '5-Stars': '0', 'Team': 'California', '4-Stars': '7', 'Average Rating': '3.11'}, {'Current Rank': '24', 'Total Commits': '19', 'Total Points': '1296', '3-Stars': '13', '5-Stars': '1', 'Team': 'Rutgers', '4-Stars': '4', 'Average Rating': '3.26'}, {'Current Rank': '25', 'Total Commits': '17', 'Total Points': '1257', '3-Stars': '11', '5-Stars': '0', 'Team': 'Nebraska', '4-Stars': '6', 'Average Rating': '3.35'}, {'Current Rank': '26', 'Total Commits': '27', 'Total Points': '1139', '3-Stars': '21', '5-Stars': '0', 'Team': 'Texas Tech', '4-Stars': '3', 'Average Rating': '2.93'}, {'Current Rank': '27', 'Total Commits': '27', 'Total Points': '1126', '3-Stars': '16', '5-Stars': '0', 'Team': 'Virginia', '4-Stars': '4', 'Average Rating': '2.81'}, {'Current Rank': '28', 'Total Commits': '29', 'Total Points': '1088', '3-Stars': '19', '5-Stars': '0', 'Team': 'Utah', '4-Stars': '5', 'Average Rating': '2.93'}, {'Current Rank': '29', 'Total Commits': '22', 'Total Points': '1069', '3-Stars': '19', '5-Stars': '0', 'Team': 'Vanderbilt', '4-Stars': '3', 'Average Rating': '3.14'}, {'Current Rank': '30', 'Total Commits': '28', 'Total Points': '1056', '3-Stars': '21', '5-Stars': '0', 'Team': 'Mississippi State', '4-Stars': '4', 'Average Rating': '3.04'}, {'Current Rank': '31', 'Total Commits': '19', 'Total Points': '1037', '3-Stars': '16', '5-Stars': '1', 'Team': 'Missouri', '4-Stars': '1', 'Average Rating': '3.11'}, {'Current Rank': '32', 'Total Commits': '24', 'Total Points': '1015', '3-Stars': '17', '5-Stars': '0', 'Team': 'Oklahoma State', '4-Stars': '3', 'Average Rating': '2.96'}, {'Current Rank': '33', 'Total Commits': '26', 'Total Points': '1005', '3-Stars': '22', '5-Stars': '0', 'Team': 'Purdue', '4-Stars': '2', 'Average Rating': '3'}, {'Current Rank': '34', 'Total Commits': '24', 'Total Points': '1001', '3-Stars': '21', '5-Stars': '0', 'Team': 'Arkansas', '4-Stars': '2', 'Average Rating': '3.04'}, {'Current Rank': '35', 'Total Commits': '25', 'Total Points': '975', '3-Stars': '15', '5-Stars': '1', 'Team': 'Maryland', '4-Stars': '2', 'Average Rating': '2.8'}, {'Current Rank': '36', 'Total Commits': '28', 'Total Points': '965', '3-Stars': '20', '5-Stars': '0', 'Team': 'Colorado', '4-Stars': '2', 'Average Rating': '2.79'}, {'Current Rank': '37', 'Total Commits': '22', 'Total Points': '952', '3-Stars': '17', '5-Stars': '0', 'Team': 'TCU', '4-Stars': '3', 'Average Rating': '3.05'}, {'Current Rank': '38', 'Total Commits': '24', 'Total Points': '944', '3-Stars': '15', '5-Stars': '0', 'Team': 'Arizona State', '4-Stars': '3', 'Average Rating': '2.79'}, {'Current Rank': '39', 'Total Commits': '23', 'Total Points': '917', '3-Stars': '16', '5-Stars': '0', 'Team': 'Oregon State', '4-Stars': '2', 'Average Rating': '2.87'}, {'Current Rank': '40', 'Total Commits': '19', 'Total Points': '907', '3-Stars': '14', '5-Stars': '0', 'Team': 'Mississippi', '4-Stars': '2', 'Average Rating': '2.95'}, {'Current Rank': '41', 'Total Commits': '20', 'Total Points': '876', '3-Stars': '14', '5-Stars': '0', 'Team': 'Michigan State', '4-Stars': '3', 'Average Rating': '2.8'}, {'Current Rank': '42', 'Total Commits': '22', 'Total Points': '873', '3-Stars': '16', '5-Stars': '0', 'Team': 'Louisville', '4-Stars': '3', 'Average Rating': '3'}, {'Current Rank': '43', 'Total Commits': '24', 'Total Points': '853', '3-Stars': '15', '5-Stars': '0', 'Team': 'Iowa', '4-Stars': '4', 'Average Rating': '2.96'}, {'Current Rank': '44', 'Total Commits': '23', 'Total Points': '813', '3-Stars': '18', '5-Stars': '0', 'Team': 'North Carolina', '4-Stars': '3', 'Average Rating': '3.04'}, {'Current Rank': '45', 'Total Commits': '23', 'Total Points': '810', '3-Stars': '17', '5-Stars': '0', 'Team': 'Baylor', '4-Stars': '3', 'Average Rating': '3'}, {'Current Rank': '46', 'Total Commits': '24', 'Total Points': '808', '3-Stars': '17', '5-Stars': '0', 'Team': 'Arizona', '4-Stars': '2', 'Average Rating': '2.88'}, {'Current Rank': '47', 'Total Commits': '16', 'Total Points': '795', '3-Stars': '10', '5-Stars': '0', 'Team': 'Pittsburgh', '4-Stars': '4', 'Average Rating': '3.13'}, {'Current Rank': '48', 'Total Commits': '29', 'Total Points': '787', '3-Stars': '24', '5-Stars': '0', 'Team': 'West Virginia', '4-Stars': '1', 'Average Rating': '2.9'}, {'Current Rank': '49', 'Total Commits': '19', 'Total Points': '780', '3-Stars': '15', '5-Stars': '0', 'Team': 'South Florida', '4-Stars': '2', 'Average Rating': '3'}, {'Current Rank': '50', 'Total Commits': '28', 'Total Points': '756', '3-Stars': '24', '5-Stars': '0', 'Team': 'Cincinnati', '4-Stars': '0', 'Average Rating': '2.86'}, {'Current Rank': '51', 'Total Commits': '25', 'Total Points': '750', '3-Stars': '5', '5-Stars': '0', 'Team': 'UTEP', '4-Stars': '0', 'Average Rating': '1.96'}, {'Current Rank': '52', 'Total Commits': '19', 'Total Points': '708', '3-Stars': '11', '5-Stars': '0', 'Team': 'Penn State', '4-Stars': '1', 'Average Rating': '2.58'}, {'Current Rank': '53', 'Total Commits': '20', 'Total Points': '621', '3-Stars': '10', '5-Stars': '0', 'Team': 'Duke', '4-Stars': '1', 'Average Rating': '2.6'}, {'Current Rank': '54', 'Total Commits': '22', 'Total Points': '618', '3-Stars': '17', '5-Stars': '0', 'Team': 'North Carolina State', '4-Stars': '0', 'Average Rating': '2.77'}, {'Current Rank': '55', 'Total Commits': '25', 'Total Points': '605', '3-Stars': '13', '5-Stars': '0', 'Team': 'Boise State', '4-Stars': '0', 'Average Rating': '2.36'}, {'Current Rank': '56', 'Total Commits': '26', 'Total Points': '602', '3-Stars': '14', '5-Stars': '0', 'Team': 'Washington State', '4-Stars': '2', 'Average Rating': '2.69'}, {'Current Rank': '57', 'Total Commits': '17', 'Total Points': '587', '3-Stars': '13', '5-Stars': '0', 'Team': 'Georgia Tech', '4-Stars': '2', 'Average Rating': '3'}, {'Current Rank': '57', 'Total Commits': '12', 'Total Points': '587', '3-Stars': '7', '5-Stars': '0', 'Team': 'Wisconsin', '4-Stars': '3', 'Average Rating': '3.08'}, {'Current Rank': '59', 'Total Commits': '21', 'Total Points': '580', '3-Stars': '14', '5-Stars': '0', 'Team': 'Kansas State', '4-Stars': '1', 'Average Rating': '2.76'}, {'Current Rank': '60', 'Total Commits': '25', 'Total Points': '531', '3-Stars': '16', '5-Stars': '0', 'Team': 'Houston', '4-Stars': '1', 'Average Rating': '2.72'}, {'Current Rank': '61', 'Total Commits': '21', 'Total Points': '525', '3-Stars': '12', '5-Stars': '0', 'Team': 'Northwestern', '4-Stars': '2', 'Average Rating': '2.76'}, {'Current Rank': '62', 'Total Commits': '15', 'Total Points': '514', '3-Stars': '9', '5-Stars': '0', 'Team': 'Brigham Young', '4-Stars': '2', 'Average Rating': '2.87'}, {'Current Rank': '63', 'Total Commits': '26', 'Total Points': '504', '3-Stars': '21', '5-Stars': '0', 'Team': 'Kentucky', '4-Stars': '1', 'Average Rating': '2.88'}, {'Current Rank': '64', 'Total Commits': '17', 'Total Points': '468', '3-Stars': '8', '5-Stars': '0', 'Team': 'Boston College', '4-Stars': '2', 'Average Rating': '2.71'}, {'Current Rank': '65', 'Total Commits': '19', 'Total Points': '459', '3-Stars': '14', '5-Stars': '0', 'Team': 'Illinois', '4-Stars': '0', 'Average Rating': '2.74'}, {'Current Rank': '66', 'Total Commits': '21', 'Total Points': '437', '3-Stars': '13', '5-Stars': '0', 'Team': 'Syracuse', '4-Stars': '0', 'Average Rating': '2.62'}, {'Current Rank': '67', 'Total Commits': '25', 'Total Points': '436', '3-Stars': '17', '5-Stars': '0', 'Team': 'Indiana', '4-Stars': '0', 'Average Rating': '2.6'}, {'Current Rank': '68', 'Total Commits': '20', 'Total Points': '427', '3-Stars': '10', '5-Stars': '0', 'Team': 'Marshall', '4-Stars': '1', 'Average Rating': '2.6'}, {'Current Rank': '69', 'Total Commits': '28', 'Total Points': '420', '3-Stars': '16', '5-Stars': '0', 'Team': 'Arkansas State', '4-Stars': '0', 'Average Rating': '2.57'}, {'Current Rank': '70', 'Total Commits': '19', 'Total Points': '409', '3-Stars': '16', '5-Stars': '0', 'Team': 'Wake Forest', '4-Stars': '0', 'Average Rating': '2.84'}, {'Current Rank': '71', 'Total Commits': '26', 'Total Points': '407', '3-Stars': '12', '5-Stars': '0', 'Team': 'Southern Miss', '4-Stars': '1', 'Average Rating': '2.54'}, {'Current Rank': '72', 'Total Commits': '28', 'Total Points': '341', '3-Stars': '11', '5-Stars': '0', 'Team': 'Memphis', '4-Stars': '0', 'Average Rating': '2.25'}, {'Current Rank': '73', 'Total Commits': '27', 'Total Points': '333', '3-Stars': '19', '5-Stars': '0', 'Team': 'Minnesota', '4-Stars': '0', 'Average Rating': '2.7'}, {'Current Rank': '74', 'Total Commits': '20', 'Total Points': '324', '3-Stars': '11', '5-Stars': '0', 'Team': 'East Carolina', '4-Stars': '0', 'Average Rating': '2.45'}, {'Current Rank': '75', 'Total Commits': '21', 'Total Points': '285', '3-Stars': '15', '5-Stars': '0', 'Team': 'Kansas', '4-Stars': '0', 'Average Rating': '2.62'}, {'Current Rank': '76', 'Total Commits': '13', 'Total Points': '259', '3-Stars': '7', '5-Stars': '0', 'Team': 'Western Kentucky', '4-Stars': '0', 'Average Rating': '2.54'}, {'Current Rank': '77', 'Total Commits': '29', 'Total Points': '228', '3-Stars': '5', '5-Stars': '0', 'Team': 'Temple', '4-Stars': '0', 'Average Rating': '2.17'}, {'Current Rank': '78', 'Total Commits': '23', 'Total Points': '214', '3-Stars': '9', '5-Stars': '0', 'Team': 'Connecticut', '4-Stars': '0', 'Average Rating': '2.39'}, {'Current Rank': '78', 'Total Commits': '27', 'Total Points': '214', '3-Stars': '9', '5-Stars': '0', 'Team': 'Toledo', '4-Stars': '0', 'Average Rating': '2.33'}, {'Current Rank': '80', 'Total Commits': '20', 'Total Points': '197', '3-Stars': '8', '5-Stars': '0', 'Team': 'Ohio', '4-Stars': '0', 'Average Rating': '2.3'}, {'Current Rank': '81', 'Total Commits': '18', 'Total Points': '181', '3-Stars': '6', '5-Stars': '0', 'Team': 'Tulane', '4-Stars': '1', 'Average Rating': '2.22'}, {'Current Rank': '82', 'Total Commits': '25', 'Total Points': '178', '3-Stars': '5', '5-Stars': '0', 'Team': 'Miami (OH)', '4-Stars': '0', 'Average Rating': '2.2'}, {'Current Rank': '83', 'Total Commits': '23', 'Total Points': '169', '3-Stars': '7', '5-Stars': '0', 'Team': 'Nevada', '4-Stars': '0', 'Average Rating': '2.22'}, {'Current Rank': '84', 'Total Commits': '26', 'Total Points': '166', '3-Stars': '5', '5-Stars': '0', 'Team': 'New Mexico', '4-Stars': '0', 'Average Rating': '2.04'}, {'Current Rank': '85', 'Total Commits': '29', 'Total Points': '155', '3-Stars': '19', '5-Stars': '0', 'Team': 'Florida International', '4-Stars': '0', 'Average Rating': '2.66'}, {'Current Rank': '86', 'Total Commits': '20', 'Total Points': '149', '3-Stars': '6', '5-Stars': '0', 'Team': 'Hawaii', '4-Stars': '0', 'Average Rating': '2'}, {'Current Rank': '87', 'Total Commits': '27', 'Total Points': '144', '3-Stars': '4', '5-Stars': '0', 'Team': 'Navy', '4-Stars': '0', 'Average Rating': '1.48'}, {'Current Rank': '88', 'Total Commits': '21', 'Total Points': '140', '3-Stars': '16', '5-Stars': '0', 'Team': 'Iowa State', '4-Stars': '0', 'Average Rating': '2.76'}, {'Current Rank': '89', 'Total Commits': '22', 'Total Points': '130', '3-Stars': '14', '5-Stars': '0', 'Team': 'Tulsa', '4-Stars': '0', 'Average Rating': '2.45'}, {'Current Rank': '90', 'Total Commits': '21', 'Total Points': '125', '3-Stars': '12', '5-Stars': '0', 'Team': 'Southern Methodist', '4-Stars': '0', 'Average Rating': '2.57'}, {'Current Rank': '91', 'Total Commits': '18', 'Total Points': '116', '3-Stars': '13', '5-Stars': '0', 'Team': 'UCF', '4-Stars': '0', 'Average Rating': '2.61'}, {'Current Rank': '92', 'Total Commits': '25', 'Total Points': '115', '3-Stars': '11', '5-Stars': '0', 'Team': 'Rice', '4-Stars': '0', 'Average Rating': '2.36'}, {'Current Rank': '92', 'Total Commits': '24', 'Total Points': '115', '3-Stars': '11', '5-Stars': '0', 'Team': 'Texas State', '4-Stars': '0', 'Average Rating': '2.38'}, {'Current Rank': '94', 'Total Commits': '28', 'Total Points': '110', '3-Stars': '11', '5-Stars': '0', 'Team': 'Florida Atlantic', '4-Stars': '0', 'Average Rating': '2.32'}, {'Current Rank': '95', 'Total Commits': '30', 'Total Points': '100', '3-Stars': '8', '5-Stars': '0', 'Team': 'Northern Illinois', '4-Stars': '0', 'Average Rating': '2.27'}, {'Current Rank': '96', 'Total Commits': '24', 'Total Points': '95', '3-Stars': '7', '5-Stars': '0', 'Team': 'Louisiana-Lafayette', '4-Stars': '0', 'Average Rating': '2.29'}, {'Current Rank': '97', 'Total Commits': '19', 'Total Points': '91', '3-Stars': '8', '5-Stars': '0', 'Team': 'Louisiana Tech', '4-Stars': '0', 'Average Rating': '2.21'}, {'Current Rank': '98', 'Total Commits': '22', 'Total Points': '90', '3-Stars': '6', '5-Stars': '0', 'Team': 'San Diego State', '4-Stars': '0', 'Average Rating': '2.09'}, {'Current Rank': '99', 'Total Commits': '20', 'Total Points': '86', '3-Stars': '7', '5-Stars': '0', 'Team': 'New Mexico State', '4-Stars': '0', 'Average Rating': '2.05'}, {'Current Rank': '100', 'Total Commits': '21', 'Total Points': '85', '3-Stars': '5', '5-Stars': '0', 'Team': 'North Texas', '4-Stars': '0', 'Average Rating': '2.24'}]
```

## 4. Appendix

*Coming Soon*
