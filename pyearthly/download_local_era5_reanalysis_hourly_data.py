# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:54:57 2024

@author: samba
"""

import cdsapi
import shutil
import os


def download_local_era5_reanalysis_hourly_data(url, key, product_type, format, variable, year, month, day, time, 
                                                area,download_folder_path=None, final_destination_path=None, 
                                                filename=None): 
    


    """
    Downloads ERA5 global daily reanalysis data from the CDS API and saves the data in a user-specified location. The function 
    uses the cdsapi library to download data from the CDS API and moves the resulting file to a user-specified location 
    (if specified).

    Parameters
    ----------
    url : str
        The url of the CDS API.
    key : str
        A unique personal key to access and download data from the CDS API.
    product_type : str
        The product type of the data to download (e.g. reanalysis).
    format : str
        The file format of the downloaded file (e.g. netcdf).
    variable : str
        The geophysical parameter for which to download the data (e.g. "total_precipitation").
    year : str
        The year for which to download the data.
    month : str
        The month for which to download the data.
    day : str
        The day for which to download the data.
    time : list of str
        The hours of the day for which to download the data, specified in a list (e.g. ['00:00', '03:00', '06:00']).
        The time values can be zero-padded or not, as long as they are formatted as a string.
    area : list of float
        The geographic bounding box for the area of interest, specified as [North, West, South, East].
    download_folder_path : str
        Optional. The source folder where the downloaded file should be stored, specified as a string path.
        If not provided, the file will be stored in the current working directory.
    final_destination_path : str
        Optional. The destination folder/location where the downloaded file should be stored, specified as a string path.
        If not provided, the file will be stored in the current working directory.
    filename : str
        Optional. The name to give to the downloaded file, specified as a string.
        If not provided, the file will be saved with a default filename of 'download.nc'.

    Returns
    -------
    str
        The name of the downloaded file.
    """
    

    # Initialize the api client 
    c = cdsapi.Client(url=url, key=key) 

    # Set filename to default if not set by the user
    if filename is None:
        filename = 'download.nc'

    # Retrieve the data
    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': product_type,
            'format': format,
            'variable': variable,
            'year': year,
            'month': month,
            'day': day,
            'time': time,
            'area': area
        },
        filename
    )

    # Check if optional parameters are provided before moving the file
    if download_folder_path is not None and final_destination_path is not None:
        # Define paths for source and destination folders
        src_path = download_folder_path + '/' + filename
        dst_path = final_destination_path + '/' + filename

        # Move file from source to destination
        shutil.move(src_path, dst_path)
        
    return filename