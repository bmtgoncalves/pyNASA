#!/usr/bin/env python

from pyNASA import pyNASA

if __name__ == "__main__":
	from NASA_accounts import apps
	app = apps["pyNASA"]

	nasa = pyNASA(**app)
	data = nasa.outgassing()

	print(data.shape)
