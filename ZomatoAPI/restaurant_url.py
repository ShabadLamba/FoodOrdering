from bs4 import BeautifulSoup
from urllib2 import Request, urlopen, URLError
import re
from errorhandler import typec
from re import search
from re import sub
import json

def crawlRestaurants(restaurant_url):
	try:
		menu_url = []
		restaurant_menu_url_with_unicode = restaurant_url + "/menu#food"
		restaurant_menu_url_with_unicode = restaurant_menu_url_with_unicode.replace(unichr(233),'e')
		restaurant_menu_url = sub(r"[^\x00-\x7F]+","",restaurant_menu_url_with_unicode)
		try:
			response = urlopen(restaurant_menu_url)
			html = response.read()
			# print html
			rest_soup = BeautifulSoup(html)
			for javascript_code in rest_soup.find_all("script",{"type":"text/javascript"}):
				text = javascript_code.text
				pat = "zomato.menuPages"
				index = text.find(pat)
				if index >= 0:
					menu_items = search("zomato.menuPages = (.+?);",text).group(1)
					menu_dict = json.loads(menu_items)
					
					for urls in menu_dict:
						menu_url.append(str(urls['url']))
			return menu_url
		except URLError as error:
			print restaurant_menu_url
		return restaurantsDB
	except URLError as error:
		print error 

# print crawlRestaurants("https://www.zomato.com/bangalore/restaurants/south/koramangala/truffles-51040")
'''
city_id,city_name = 1,"ncr"
locality_id,locality_name = 8,"Anand Lok"
'''