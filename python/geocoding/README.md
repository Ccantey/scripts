# Batch Geocode CSVs

=====================================

This Python program depends on a geopy python wrapper and a Google API key. It will read and geocode a csv file. Through the Google geocoding API, you can geocode up to 2,500 address per day. The Geopy wrapper has methods for several geocoding services though, so one could try/except through many more addresses.

[pip](http://www.pip-installer.org/en/latest/) is required to install python modules. Make sure the Python environmental variable is set.

First install [GeoPy API](https://github.com/geopy/geopy) using [pip](http://www.pip-installer.org/en/latest/) with:

    pip install geopy

Install [xlswriter](https://xlsxwriter.readthedocs.io/index.html) for to write Excel files:

    pip install xlswriter


