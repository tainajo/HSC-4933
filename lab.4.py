import requests
YEAR = 2020
DATASET = "dec/dhc"

URL = f"https://api.census.gov/data/{YEAR}/{DATASET}"
API_KEY = "ba387dd3093f1deccf93db1cc6567bbce97d3ab1"

param = {
"get" : "NAME,H10_004N",
"for" : "state:*",
"key" : API_KEY,
}

response = requests.get(URL, params=param)

if response.status_code != 200:
    print(f"Request failed ({response.status_code})")
    print(response.text)
    raise SystemExit (1)

response.raise_for_status()

data = response.json()

print(f"Got {len(data) -1} rows back.")

for i in data:
    print(i)
