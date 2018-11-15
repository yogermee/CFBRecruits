from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import urllib
import re

class Scraper(object):
	def __init__(self, path):
		self.path = path

	def buildPlayerDicts(self, data_fields, team_player_data, index_iterator):
		player_data = []

		for number in range(0, len(team_player_data), index_iterator):
			player_dict = {}
			player = team_player_data[number:number + index_iterator]

			for data_item, player_item in zip(data_fields, player):
				player_dict[data_item] = player_item

			player_data.append(player_dict)

		return player_data

	def calcAvgClassRating(self, final_class_data):
		total_rating = 0

		for item in final_class_data:
			for key, value in item.iteritems():
				if key == "Rating":
					total_rating += float(value)

		average_rating = total_rating / len(final_class_data)

		return round(average_rating, 2)

class Scrape247(Scraper):
	def __init__(self, path):
		self.path = path

	def getClassURL(self, team, year):
		url_prefix = "https://247sports.com/college/"
		url_suffix = "-Football/Commits/"
		year = "/Season/" + str(year)
		url = url_prefix + team + year + url_suffix

		return url

	def getClassData(self, url):
		browser = webdriver.Chrome(self.path)

		try:
			browser.get(url)

		except TimeoutException as e:
			browser.execute_script("window.stop();")
			print "Selenum browser driver has timed out. Please try re-running your script."

		team_player_count = int(re.findall(r'\d+', browser.find_element_by_xpath('//*[@id="page-content"]/div[1]/section[2]/section/div/ul').text.splitlines()[0])[0])
		team_player_data = str(browser.find_element_by_xpath('//*[@id="page-content"]/div[1]/section[2]/section/div/ul').text).splitlines()[5:]

		data_fields = ["Name", "Location", "Ht/Wt", "Rating", "Nat/Pos/St Rank", "Status", "Position"]
		index_iterator = len(team_player_data) / team_player_count

		return (data_fields, team_player_data, index_iterator)

	def buildClassData(self, data):
		return self.buildPlayerDicts(data[0], data[1], data[2])

	def avgClassRating(self, final_class_data):
		return self.calcAvgClassRating(final_class_data)

	def teamRankings(self, year):
		browser = webdriver.Chrome(self.path)

		url_prefix = "https://247sports.com/Season/"
		url_suffix = "-Football/CompositeTeamRankings/"
		year = str(year)
		url = url_prefix + year + url_suffix

		browser.get(url)

		all_team_data = str(browser.find_element_by_xpath('//*[@id="page-content"]/div/section/section/div/ul').text).splitlines()[8:-1]
		data_fields = ["Current Rank", "Previous Rank", "Team", "Total Commits",
		"Average Rating", "5-Stars","4-Stars","3-Stars", "Total Points"]

		index_iterator = len(all_team_data) / 50

		team_data = []

		for number in range(0, len(all_team_data), index_iterator):
			team_dict = {}
			team = all_team_data[number:number + index_iterator]

			for data_item, team_item in zip(data_fields, team):
				team_dict[data_item] = team_item

			team_data.append(team_dict)

		return team_data

class ScrapeRivals(Scraper):
	def __init__(self, path):
		self.path = path

	def getClassURL(self, team, year):
		url = "https://" + team + ".rivals.com/commitments/football/" + str(year)

		return url

	def getClassData(self, url):
		browser = webdriver.Chrome(self.path)
		browser.get(url)

		data_fields = ["Name", "Position", "Location", "Height", "Weight", "Rating", "Commit Date", "Status"]
		team_player_data = browser.find_element_by_xpath('//*[@id="articles"]/rv-commitments').text.splitlines()[1:]
		team_player_count = len(team_player_data) / len(data_fields)
		
		index_iterator =  len(team_player_data) / team_player_count

		return (data_fields, team_player_data, index_iterator)

	def buildClassData(self, data):
		return self.buildPlayerDicts(data[0], data[1], data[2])

	def avgClassRating(self, final_class_data):
		return self.calcAvgClassRating(final_class_data)

	def teamRankings(self, year):
		browser = webdriver.Chrome(self.path)

		url_prefix = "https://n.rivals.com/team_rankings/"
		url_suffix = "/all-teams/football"
		year = str(2012)
		url = url_prefix + year + url_suffix

		browser.get(url)

		all_team_data = str(browser.find_element_by_xpath('//*[@id="articles"]/rv-team-rankings/rv-sortable-table/div/div[2]').text).splitlines()[1:]
		data_fields = ["Current Rank", "Team", "Total Commits", "5-Stars","4-Stars","3-Stars",
		"Average Rating", "Total Points"]

		index_iterator = len(all_team_data) / 100
		team_data = []

		for number in range(0, len(all_team_data), index_iterator):
			team_dict = {}
			team = all_team_data[number:number + index_iterator]

			for data_item, team_item in zip(data_fields, team):
				team_dict[data_item] = team_item

			team_data.append(team_dict)

		return team_data
