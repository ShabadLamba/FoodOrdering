def findRestaurant(dictOfValues):
	# dictOfParams = {"restaurant_id":None,"name":None,"url":None,"address":None,"locality_id":None,"latitude":None,"longitude":None,"rating":None,"country_id":None,"phone":None,"timings":None,\
	# 		"average_cost_for_two":None,"is_pure_veg":None,"sports_bar_flag":None,"has_bar":None,"has_ac":None,"has_dine_in":None,"has_delivery":None,"takeaway_flag":None,"accepts_credit_cards":None,\
	# 		"accepts_debit_cards":None,"sheesha_flag":None,"halal_flag":None,"has_wifi":None,"has_live_music":None,"nightlife_flag":None,"stag_entry_flag":None,"entry_fee":None,\
	# 		"has_online_delivery":None,"min_order":None,"average_delivery_time":None,"delivery_charge":None,"accepts_online_payment":None}
	# for key in dictOfValues:
	# 	dictOfParamsp[key] = dictOfValues[key]
	sqlQuery = "SELECT * FROM restaurants WHERE "
	length = len(dictOfValues)	
	for key in dictOfValues:
		if length>1:
			if type(dictOfValues[key]) == str:
				sqlQuery += "( " + key + "=" + "'" + str(dictOfValues[key]) + "'" + " )" + " AND "
			elif type(dictOfValues[key]) == dict:
				for key2 in dictOfValues[key]:
					if type(dictOfValues[key][key2]) == dict:
						sqlQuery += "( " + key + " BETWEEN " + str(dictOfValues[key][key2]["min"]) + " AND " + str(dictOfValues[key][key2]["max"]) + " )"+ " AND "
					elif dictOfValues[key][key2] != None:
						sqlQuery += "( " + key + "=" + str(dictOfValues[key][key2]) +  " )" + " AND "
			else:
				sqlQuery += "( " + key + "=" + str(dictOfValues[key]) + " )" + " AND "
			length -= 1
		else:
			if type(dictOfValues[key]) == str:
				sqlQuery += "( " + key + "=" + "'" + str(dictOfValues[key]) + "'" + " )"
				break
			elif type(dictOfValues[key]) == dict:
				for key2 in dictOfValues[key]:
					if type(dictOfValues[key][key2]) == dict:
						sqlQuery += "( " + key + " BETWEEN " + str(dictOfValues[key][key2]["min"]) + " AND " + str(dictOfValues[key][key2]["max"]) + " )"
					elif dictOfValues[key][key2] != None:
						sqlQuery += "( " + key + "=" + str(dictOfValues[key][key2]) +  " )"
				break
			else:
				sqlQuery += "( " + key + "=" + str(dictOfValues[key]) + " )"
				break
	print sqlQuery


dictOfParams = {"prize":{"exact": None,"range":{"min":45,"max":567}},"name":"Papu Pizza","url":"PPizza.com","address":"Govind Nagar","locality_id":345,"latitude":1.73,"longitude":79.412,"rating":.0002,"country_id":42,"phone":9090909090,"timings":"0400am",}
			# "average_cost_for_two":None,"is_pure_veg":None,"sports_bar_flag":None,"has_bar":None,"has_ac":None,"has_dine_in":None,"has_delivery":None,"takeaway_flag":None,"accepts_credit_cards":None,\
			# "accepts_debit_cards":None,"sheesha_flag":None,"halal_flag":None,"has_wifi":None,"has_live_music":None,"nightlife_flag":None,"stag_entry_flag":None,"entry_fee":None,\
			# "has_online_delivery":None,"min_order":None,"average_delivery_time":None,"delivery_charge":None,"accepts_online_payment":None}
findRestaurant(dictOfParams)