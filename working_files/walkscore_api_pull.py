'''{
"status": 1 
, "walkscore": 98
, "description": "Walker's Paradise"
, "updated": "2016-11-17 04:40:31.218250" 
, "logo_url": "https://cdn.walk.sc/images/api-logo.png"
, "more_info_icon": "https://cdn.walk.sc/images/api-more-info.gif"
, "more_info_link": "https://www.walkscore.com/how-it-works/"
, "ws_link":
"https://www.walkscore.com/score/1119-8th-Avenue-Seattle-WA-98101/lat=47.6085/lng=-122.3295/?utm_source=walkscore.com&utm_medium=ws_api&utm_campaign=ws_api"
, "help_link": "https://www.walkscore.com/how-it-works/"
, "snapped_lat": 47.6085
, "snapped_lon": -122.3295 
, "transit" : {"score": 100, "description": "Rider's Paradise", "summary": "115 nearby routes: 103 bus, 6 rail, 6 other"} 
, "bike" : {"score": 68, "description": "Bikeable"} 
}'''

# Dependencies
import json
import requests as req
import pandas as pd

#import VA lat long file
df = pd.read_csv('Random VA lat longs.csv')
df_test = df.head()
#print(df.head())
# Save config information.
# example_string = 'http://api.walkscore.com/score?format=json& \
# address=1119%8th%20Avenue%20Seattle%20WA%2098101&lat=47.6085& \
# lon=-122.3295&transit=1&bike=1&wsapikey=4e9a14b4cda5f4c809d23bf0f13235d4'

# Define API call parameters
walkscore_url = 'http://api.walkscore.com/score'
formatter = 'json'
api_key = 'c58332edc3aafbea28ad89d47614ff8c'
param_dict = {
	'wsapikey': api_key,
	'format': formatter,
	'transit': 1,
	'bike': 1,
	}

# Get walk, bike, and transit score data
for index, row in df_test.iterrows():

	# Put API pull in a try/except block to handle
	# Key Errors when no data are available for a
	# given lat/lon combination.
	try:
		x = row['lat'],
		y = row['lon'],
		param_dict['lat'] = x
		param_dict['lon'] = y
		ws_response = req.get(walkscore_url, params=param_dict).json()
		
		'''
		df.set_value(index,'walk score',ws_response["walkscore"])
		df.set_value(index,'transit score',ws_response["transit"]['score'])
		df.set_value(index,'bike score',ws_response["bike"]['score'])
		print(row)
		'''
		print('Result #' + str(index) + ':\nWalkscore: ' +
			str(ws_response['walkscore']) +
			'; Transit Score: ' +
			str(ws_response['transit']['score']) +
			'; Bike Score: ' +
			str(ws_response['bike']['score']))
		

	except KeyError:
		continue