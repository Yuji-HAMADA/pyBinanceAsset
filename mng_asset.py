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
spotFile = open('./spot.json', mode="w")
json.dump(spot, spotFile)
spotFile.close()

staking = client.staking_product_position('STAKING')
fileStaking = open('./staking.json', mode="w")
json.dump(staking, fileStaking)
fileStaking.close()

saving = client.savings_flexible_product_position()
fileFlexible = open('./saving.json', mode="w")
json.dump(saving, fileFlexible)
fileFlexible.close()
