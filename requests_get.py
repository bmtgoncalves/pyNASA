import requests
import urllib
from NASA_accounts import apps

app = apps["pyNASA"]

dataset = "y77d-th95"
url_basis = "https://data.nasa.gov/resource/%s.json?%s"
headers = {"X-App-Token": app["token"]}

query = {
"$limit" : 1000,
"$offset" : 0
}

qs = urllib.parse.urlencode(query)
url = url_basis % (dataset, qs)

req = requests.get(url, headers=headers)
print(len(req.json()))