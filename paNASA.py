import requests
import pandas as pd
import urllib

class paNASA:
	def __init__(self, token=None, secret=None):
		self.token = token
		self.secret = secret
		self.url_basis = "https://data.nasa.gov/resource/%s?%s"

		if token is not None:
			self.headers = {"X-App-Token": token}
		else:
			self.headers = None

	def meteorites(self, limit=50000, offset=0):
		query = {
		"$limit" : limit,
		"$offset" : offset
		}

		qs = urllib.parse.urlencode(query)
		url = self.url_basis % ("y77d-th95.json", qs)

		req = requests.get(url, headers=self.headers)

		if req.status_code == 200:
			data = pd.DataFrame.from_records(req.json())
		else:
			data = None

		return data