from restaurant_url import crawlRestaurants
from zomato_restaurant import getAllRestaurantsIdAndUrl,getAllRestaurantsLocalityId
from zomato_menu import insertManyDishes,findDistinctRestaurantIds
from zomato_locality import getAllIdsOfLocality

listOfAllRestaurantUrlAndId =  getAllRestaurantsIdAndUrl()
# for i in getAllIdsOfLocality():
# 	print i[0]
listOfMenus = {}

print "listOfAllRestaurantUrlAndId"
print "\n\n"

for resId in listOfAllRestaurantUrlAndId:
	
	print resId[0]
	if resId[1] != '0':
		if (resId[0],) not in findDistinctRestaurantIds():
			for menu in crawlRestaurants(resId[1]):
				insertManyDishes([(menu,resId[0],)])