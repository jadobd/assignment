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

i = 0
while i < len(mobile_data["data"]):
    model = mobile_data["data"][i]["name"]
    country = mobile_data["data"][i]["made"]
    usd_price = float(mobile_data["data"][i]["price"].strip(" USD"))
    exchange_rate = float(mobile_data["exchnage_rate"])
    bdt_price = usd_price * exchange_rate
    print(f'{model} is made in {country}. The price is {usd_price} USD which is almost equal to {bdt_price} BDT')
    i += 1
