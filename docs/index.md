# Simple Python interface to NASA datasets

pyNASA provides a simple interface to obtain seveal NASA datasets and return them as a pandas dataframe ready to use. It currently retrieves the data every time it is requested. A local caching mechanism will be added soon!

## Available datasets and corresponding methods
- [Meteorite Landings](https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh) **meteorite()**
- [Near-Earth Comets - Orbital Elements](https://data.nasa.gov/Space-Science/Near-Earth-Comets-Orbital-Elements/b67r-rgxc) **comets()**
- [Global Landslide Catalog Export](https://data.nasa.gov/dataset/Global-Landslide-Catalog-Export/dd9e-wu2v) **landslides()**
- [NASA Facilities](https://data.nasa.gov/Management-Operations/NASA-Facilities/gvk9-iz74) **facilities()**
- [Fireball And Bolide Reports](https://data.nasa.gov/Space-Science/Fireball-And-Bolide-Reports/mc52-syum) **bolide()**
- [WISE NEA/COMET DISCOVERY STATISTICS](https://data.nasa.gov/Space-Science/WISE-NEA-COMET-DISCOVERY-STATISTICS/7qz6-zrqt) **comet_discovery()**
- [Outgassing Db](https://data.nasa.gov/Applied-Science/Outgassing-Db/r588-f7pr) **outgassing()**
- [Open Source And General Resource Software](https://data.nasa.gov/Software/Open-Source-And-General-Resource-Software/fk38-4khf) **open_source()**
- [NASA Patents](https://data.nasa.gov/Raw-Data/NASA-Patents/gquh-watm) **patents()**
- [Extra-vehicular Activity (EVA) - US and Russia](https://data.nasa.gov/Raw-Data/Extra-vehicular-Activity-EVA-US-and-Russia/9kcy-zwvn) **eva()**
- [Candida albicans response to spaceflight (NASA STS-115) --- GSM1231690_Slide_43](https://data.nasa.gov/dataset/Candida-albicans-response-to-spaceflight-NASA-STS-/59ui-jv2j) **candida_albicans()**
- [SxSW 2016 Leads](https://data.nasa.gov/Management-Operations/SxSW-2016-Leads/yvxp-ccvk) **sxsw_2016()**
- [A E- GEOD-50881 Gene Chip Assay --- Candida albicans response to spaceflight (NASA STS-115)](https://data.nasa.gov/dataset/A-E-GEOD-50881-Gene-Chip-Assay-Candida-albicans-re/c5py-4h4g) **gene_chip_assay()**
- [BeXRB Monitor Data](https://data.nasa.gov/dataset/BeXRB-Monitor-Data/jdkf-j3pt) **bexrb_monitor()**
- [S E- GEOD-50881 Study Samples --- Candida albicans response to spaceflight (NASA STS-115)](https://data.nasa.gov/dataset/S-E-GEOD-50881-Study-Samples-Candida-albicans-resp/8e7s-kdza) **geod_50881()**

## Installation

```bash
pip install pyNASA
```

## Usage

Simplest example:

```python
from pyNASA import pyNASA

nasa = pyNASA()
data = nasa.outgassing() # Retrieve the "Outgassing Db" dataset as a pandas data frame

print(data.shape)
```