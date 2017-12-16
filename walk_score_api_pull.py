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

# Save config information.
example_string = 'http://api.walkscore.com/score?format=json& \
address=1119%8th%20Avenue%20Seattle%20WA%2098101&lat=47.6085& \
lon=-122.3295&transit=1&bike=1&wsapikey=4e9a14b4cda5f4c809d23bf0f13235d4'
walkscore_url = 'http://api.walkscore.com/score?'
formatter = 'json'
api_key = '4e9a14b4cda5f4c809d23bf0f13235d4'
address = '22031'
lat = 38.860865
lon = -77.280209

param_dict = {
	'wsapikey': api_key,
	'address': address,
	'format': formatter,
	'transit': 1,
	'bike': 1,
	'lat': lat,
	'lon': lon
}

# Get weather data
ws_response = req.get(walkscore_url, params=param_dict)
ws_json = ws_response.json()
print(ws_json)