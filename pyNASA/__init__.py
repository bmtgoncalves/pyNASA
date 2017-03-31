import requests
import pandas as pd
import urllib
import json
import pkg_resources
import sys

class pyNASA:
	def __init__(self, token=None, secret=None):
		self.token = token
		self.secret = secret
		self.url_basis = "https://data.nasa.gov/resource/%s.json?%s"

		if token is not None:
			self.headers = {"X-App-Token": token}
		else:
			self.headers = None

		data = pkg_resources.resource_string(__name__, "resources.json")
		resources = json.loads(data.decode())

		for dataset in resources:
			pyNASA._add_resource_(**dataset)

	def _add_resource_(id, name, description):
		def rec(self, limit=50000, offset=0):
			return self.resource(id, limit, offset)
		
		rec.__name__ = name
		rec.__doc__ = description
		rec.__id__ = id

		setattr(pyNASA, name, rec)

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