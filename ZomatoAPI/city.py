from zomato_city import insertManyCities,findAllCities,findCityByName,findLastInsertedCityId,findCityIdByName
from zomato_locality import insertManyLocalities,findIdOfLocality
import subprocess
import os
import ast
from pprint import pprint

LocalitiesDetails = []
CitiesDetails = []
zoneDict = {}

for cityId in range(1,40):
	curlCall = "curl --header 'X-Zomato-API-Key:7749b19667964b87a3efc739e254ada2' 'https://api.zomato.com/v2/subzones.json?city_id=%s'" % (str(cityId))
	locationData = subprocess.check_output(curlCall,shell=True) 
	dictLocationData = ast.literal_eval(locationData)
	# for i in y["results"]:
	# 	print i
	try:
		for subzones in dictLocationData["subzones"]:
			# print ast.literal_eval(subzones["subzone"])
				
			cityTuple = (subzones['subzone']['city_id'],subzones['subzone']['city_name'],)	
			
			if(findCityByName(cityTuple[1]) == []):
				insertManyCities((cityTuple,))
				print cityTuple

			LocaTuple = (subzones['subzone']['id'] ,subzones['subzone']['name'], findCityIdByName(subzones['subzone']['city_name']), subzones['subzone']['latitude'], subzones['subzone']['longitude'],)

			if findIdOfLocality(LocaTuple[0]) == []:
				print LocaTuple
				insertManyLocalities((LocaTuple,))
		
	except:
		print "Error! :p"
		print "\n"
		print dictLocationData



