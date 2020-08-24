import configparser
import googlemaps

config = configparser.ConfigParser()
config.read('config.ini')

gmaps = googlemaps.Client(key = config['GOOGLEMAP']['API_KEY'])

places = gmaps.places_nearby(
	location=(22.6229005, 120.3089579),
	keyword='拉麵店',
	radius=2500,
	language='zh-TW'
	)

for place in sorted(places['results'],key=lambda x: x['rating'],reverse=True):
    # print(place['name'],place['rating'])
    # place_id = place['place_id']
    # info = gmaps.place(place_id)['result']
    # for review in gmaps.place(place_id)['result']['reviews']:
    #     print(review['text'])
    #     print('------------')
    # print('\n')
    lat = place['geometry']['location']['lat']
    lon = place['geometry']['location']['lng']
    


