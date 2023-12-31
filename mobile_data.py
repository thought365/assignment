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

for phone in mobile_data['data']:

    price_usd = phone['price'].split(' ')[0]
    # print("price is ", price_usd)
    exchange_rate = mobile_data['exchnage_rate']
    # print("Exchange rate is ", exchange_rate)
    total_price = float(price_usd) * exchange_rate

    print(f"{phone['name']} is made in {phone['made']}. The price is {phone['price']} which is almost Equal to {total_price} ")

