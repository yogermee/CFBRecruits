from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import urllib
import re

class Scraper(object):
	def __init__(self):
		pass

	def buildPlayerDicts(self, data_fields, team_player_data, index_iterator):
		player_data = []

		for number in range(0, len(team_player_data), index_iterator):
			player_dict = {}
			player = team_player_data[number:number + index_iterator]

			for data_item, player_item in zip(data_fields, player):
				player_dict[data_item] = player_item

			player_data.append(player_dict)

		return player_data

class Scrape247(Scraper):
	def __init__(self):
		super(Scraper, self).__init__()

	def getURL(self, team, year):
		url_prefix = "https://247sports.com/college/"
		url_suffix = "-Football/Commits/"
		year = "/Season/" + str(year)
		url = url_prefix + team + year + url_suffix

		return url

	def getClassData(self, url):
		browser = webdriver.Chrome(<INSERT YOUR WEB DRIVER'S LOCAL FILE PATH HERE>)

		try:
			browser.get(url)

		except TimeoutException as e:
			browser.execute_script("window.stop();")
			print "Selenum browser driver has timed out. Please try re-running your script."

		browser.implicitly_wait(30)

		team_player_count = int(re.findall(r'\d+', browser.find_element_by_xpath('//*[@id="page-content"]/div[1]/section[2]/section/div/ul').text.splitlines()[0])[0])
		team_player_data = str(browser.find_element_by_xpath('//*[@id="page-content"]/div[1]/section[2]/section/div/ul').text).splitlines()[5:]

		data_fields = ["Name", "Location", "Ht/Wt", "Rating", "Nat/Pos/St Rank", "Status", "Position"]
		index_iterator = len(team_player_data) / team_player_count

		return (data_fields, team_player_data, index_iterator)

	def buildClassData(self, data):

		return self.buildPlayerDicts(data[0], data[1], data[2])

	def avgClassRating(self, player_data):
		total_rating = 0

		for item in player_data:
			for key, value in item.iteritems():
				if key == "Rating":
					total_rating += float(value)

		average_rating = total_rating / len(player_data)

		return round(average_rating, 2)

	def teamRankings(self, year):
		browser = webdriver.Chrome("/Users/yogermee/Documents/Coding/SeleniumDrivers/chromedriver")

		url_prefix = "https://247sports.com/Season/"
		url_suffix = "-Football/CompositeTeamRankings/"
		year = str(year)
		url = url_prefix + year + url_suffix

		browser.get(url)
		browser.implicitly_wait(30)

		all_team_data = str(browser.find_element_by_xpath('//*[@id="page-content"]/div/section/section/div/ul').text).splitlines()
		data_fields = ["Current Rank", "Previous Rank", "Team", "Total Commits",
		"Average Rating", "5-Stars","4-Stars","3-Stars", "Total Points"]

		team_data_list = all_team_data[8:-1]
		index_iterator = len(team_data_list) / 50
		team_data = []

		for number in range(0, len(team_data_list), index_iterator):
			team_dict = {}
			team = team_data_list[number:number + index_iterator]

			for data_item, team_item in zip(data_fields, team):
				team_dict[data_item] = team_item

			team_data.append(team_dict)

		return team_data

class ScrapeRivals(Scraper):
	def __init__(self):
		super(Scraper, self).__init__()

	def getURL(self, team, year):
		url = "https://" + team + ".rivals.com/commitments/football/" + str(year)

		return url

	def getClassData(self, url):
		browser = webdriver.Chrome("/Users/yogermee/Documents/Coding/SeleniumDrivers/chromedriver")
		browser.get(url)
		browser.implicitly_wait(30)

		data_fields = ["Name", "Position", "Location", "Height", "Weight", "Rating", "Commit Date", "Status"]
		team_player_data = browser.find_element_by_xpath('//*[@id="articles"]/rv-commitments').text.splitlines()[1:]
		team_player_count = len(team_player_data) / len(data_fields)
		
		index_iterator =  len(team_player_data) / team_player_count

		return (data_fields, team_player_data, index_iterator)

	def buildClassData(self, data):

		return self.buildPlayerDicts(data[0], data[1], data[2])
