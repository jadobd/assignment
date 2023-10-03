mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchnage_rate': 107.25
            }

# Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT


# print(mobile_data.keys())
# print(mobile_data.values())
# print(mobile_data["data"][0])

name = mobile_data["data"][0]["name"]
made= mobile_data["data"][0]["made"]
usd_price = int(mobile_data["data"][0]["price"].strip(" USD"))
exchange_rate = int(mobile_data["exchnage_rate"])
bdt_price = usd_price * exchange_rate
print(f'{name} is made in {made}. The price is {usd_price} which is almost equal to {bdt_price} BDT')