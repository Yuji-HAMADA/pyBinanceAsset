from binance.spot import Spot
import json
import settings

# api key/secret are required for user data endpoints
client = Spot(key=settings.API_KEY, secret=settings.SECRET_KEY)

# Get account and balance information
account = client.account()
#print(account)

# Define spot_n_savings dict
spot_n_savings = {}

# Set spot_n_savings dict for non-empty crypt
for balance in account['balances']:
    amount = float((balance['free']))
    if amount > 0:
        spot_n_savings[balance['asset']] = amount

print(spot_n_savings)
path1 = './test1.json'
json_file1 = open(path1, mode="w")
json.dump(spot_n_savings, json_file1)
json_file1.close()

staking = client.staking_product_position('STAKING')
#print(staking)
path2 = './test_staking.json'
json_file2 = open(path2, mode="w")
json.dump(staking, json_file2)
json_file2.close()

saving = client.savings_flexible_product_position()
print(saving)
path3 = './test_saving.json'
json_file3 = open(path3, mode="w")
json.dump(saving, json_file3)
json_file3.close()

#snaptshot = client.account_snapshot('SPOT')
#print(snaptshot)

#account_status = client.account_status()
#print(account_status)