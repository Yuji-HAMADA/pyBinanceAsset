from binance.spot import Spot
import json
import settings
 
"""
api key/secret are required for user data endpoints
Should be set in setting.py of the same folder like below
API_KEY='apikeyapikey'
SECRET_KEY='secretkeysecretkey'
"""
client = Spot(key=settings.API_KEY, secret=settings.SECRET_KEY)

spot = client.account_snapshot('SPOT')
f = open('./spot.json', mode="w")
json.dump(spot, f)
f.close()

staking = client.staking_product_position('STAKING')
f = open('./staking.json', mode="w")
json.dump(staking, f)
f.close()

saving = client.savings_flexible_product_position()
f = open('./saving.json', mode="w")
json.dump(saving, f)
f.close()
