import requests
import pandas as pd
import urllib
import json

class paNASA:
	def __init__(self, token=None, secret=None):
		self.token = token
		self.secret = secret
		self.url_basis = "https://data.nasa.gov/resource/%s?%s"

		if token is not None:
			self.headers = {"X-App-Token": token}
		else:
			self.headers = None

		resources = json.load(open("resources.json"))

		for key, value in resources.items():
			def rec(self, limit=50000, offset=0):
				return self.resource(value, limit, offset)
			rec.__name__ = key

			setattr(paNASA, key, rec)

	def resource(self, resource_name, limit=50000, offset=0):
		query = {
		"$limit" : limit,
		"$offset" : offset
		}

		qs = urllib.parse.urlencode(query)
		url = self.url_basis % (resource_name, qs)

		req = requests.get(url, headers=self.headers)

		if req.status_code == 200:
			data = pd.DataFrame.from_records(req.json())
		else:
			data = None

		return data

if __name__ == "__main__":

	from NASA_accounts import apps
	app = apps["paNASA"]

	nasa = paNASA(**app)
	data = nasa.outgassing()

	print(data.shape)