from binance.spot import Spot
import json
import settings


"""
api key/secret are required for user data endpoints
They are expected to be set in setting.py of the same folder like below
API_KEY='apikeyapikey'
SECRET_KEY='secretkeysecretkey'
"""
client = Spot(key=settings.API_KEY, secret=settings.SECRET_KEY)

spot = client.account_snapshot('SPOT')
path4 = './spot.json'
json_file4 = open(path4, mode="w")
json.dump(spot, json_file4)
json_file4.close()
print(spot)

staking = client.staking_product_position('STAKING')
#print(staking)
path2 = './test_staking.json'
json_file2 = open(path2, mode="w")
json.dump(staking, json_file2)
json_file2.close()

saving = client.savings_flexible_product_position()
#print(saving)
path3 = './test_saving.json'
json_file3 = open(path3, mode="w")
json.dump(saving, json_file3)
json_file3.close()
