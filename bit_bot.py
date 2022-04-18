#! /usr/bin/python

from alpaca_trade_api.rest import REST, TimeFrame
import pandas as pd

BASE_URL = "https://paper-api.alpaca.markets"
KEY_ID = "PK4WYD4BWSKOROFOAON4"
SECRET_KEY = "JVnhLodNhlHV6zVU87Eu62jW33E8TJU6tFXDGidv"

# Instantiate REST API Connection
api = REST(key_id=KEY_ID,secret_key=SECRET_KEY,base_url="https://paper-api.alpaca.markets")

# Fetch 1Minute historical bars of Bitcoin
bars = api.get_crypto_bars("BTCUSD", TimeFrame.Minute).df

bars = bars[bars.exchange == 'CBSE']

# order_buy = api.submit_order('BTCUSD',qty=0.5, side='buy')

positions = api.list_positions()
print(positions)
