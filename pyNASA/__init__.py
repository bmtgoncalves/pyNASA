import pandas as pd
import json
import pkg_resources
from sodapy import Socrata

class pyNASA:
	def __init__(self, token=None, secret=None):
		self.token = token
		self.secret = secret
		self.client = Socrata("data.nasa.gov", token)

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
		records = self.client.get(resource_name, limit=limit, offset=offset)

		return pd.DataFrame.from_records(records)