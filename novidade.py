import requests
import json

cotaçoes =requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotaçoes = json
print(cotaçoes)