# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:56:27 2024

@author: samba
"""


import os
import requests
import xml.etree.ElementTree as ET
import time



def download_cmip6_climate_data_download(model, timeframe, ensemble, climate_variable, start_year, end_year, output_folder):

    """
    Download climate data files from the CMIP6 dataset.

    This function downloads data for a specified climate model, timeframe,
    ensemble member, and climate variable for a range of years. The files
    are saved in a specified output folder.

    Parameters:
    model (str): Climate model name (e.g., 'ACCESS-CM2').
    timeframe (str): Time frame of the data (e.g., 'historical', 'SSP126', 'SSP245').
    ensemble (str): Ensemble member (e.g., 'r1i1p1f1').
    climate_variable (str): Climate variable (e.g., 'pr' for precipitation).
    start_year (int): Start year of the data range.
    end_year (int): End year of the data range.
    output_folder (str): Path to the output folder where files will be saved.

    Usage:
    cmip6_climate_data("ACCESS-CM2", "historical", "r1i1p1f1", "pr", 1950, 1952, "./output_folder")
    """


    # Ensure the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Construct the catalog URL
    catalog_url = f"https://ds.nccs.nasa.gov/thredds/catalog/AMES/NEX/GDDP-CMIP6/{model}/{timeframe}/{ensemble}/{climate_variable}/catalog.xml"

    # Retrieve the XML catalog
    response = requests.get(catalog_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the catalog. Status code: {response.status_code}")
        return

    # Parse the XML
    root = ET.fromstring(response.content)
    ns = {'thredds': 'http://www.unidata.ucar.edu/namespaces/thredds/InvCatalog/v1.0'}

    # Base URL for file downloads
    base_url = "https://ds.nccs.nasa.gov/thredds/fileServer/"

    # Extract file URLs and filter by year range
    file_urls = []
    for dataset in root.findall(".//thredds:dataset", ns):
        url_path = dataset.attrib.get('urlPath')
        if url_path:
            year = int(url_path.split('_')[-1].split('.')[0])
            if start_year <= year <= end_year:
                file_urls.append(base_url + url_path)

    # Download each file
    for file_url in file_urls:
        file_name = os.path.join(output_folder, file_url.split('/')[-1])
        response = requests.get(file_url)
        if response.status_code == 200:
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {file_name}")
        else:
            print(f"Failed to download {file_name}")

        # Optional: Throttle requests
        # time.sleep(1)