import requests

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum,dogecoin",
    "vs_currencies": "usd"
}

try:
    response = requests.get(url, params=params)
    data = response.json()

    print("--- LIVE CRYPTOCURRENCY PRICES ---")

    print("Bitcoin:", data["bitcoin"]["usd"], "USD")
    print("Ethereum:", data["ethereum"]["usd"], "USD")
    print("Dogecoin:", data["dogecoin"]["usd"], "USD")

except Exception as e:
    print("Error:", e)