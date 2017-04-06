from sodapy import Socrata
from NASA_accounts import apps

app = apps["pyNASA"]

client = Socrata("data.nasa.gov", app["token"])

metadata = client.get_metadata("b67r-rgxc")
data = client.get("b67r-rgxc")