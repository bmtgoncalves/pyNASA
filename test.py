from paNASA import paNASA

if __name__ == "__main__":

	from NASA_accounts import apps
	app = apps["paNASA"]

	nasa = paNASA(**app)
	data = nasa.outgassing()

	print(data.shape)
