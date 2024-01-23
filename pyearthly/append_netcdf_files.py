# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:40:29 2024

@author: samba
"""

import os
import xarray as xr
from tqdm import tqdm
import shutil
import sys

def append_netcdf_files(directory, output_filename, variable_name, target_directory):
    """
    Appends NetCDF files found in the specified directory into a single NetCDF file.
    Saves the output file to the /tmp/ directory, then moves the output file
    to the specified target directory using shutil.

    :param directory: Path to the directory containing NetCDF files.
    :param output_filename: Name for the output NetCDF file.
    :param variable_name: Name of the variable to append across files.
    :param target_directory: Path to the target directory for the output file.
    """
    data_arrays = []

    # Sorting files ensures that they are appended in order
    netcdf_files = sorted([f for f in os.listdir(directory) if f.endswith('.nc')])
    for filename in tqdm(netcdf_files, desc="Processing files"):
        filepath = os.path.join(directory, filename)
        with xr.open_dataset(filepath) as ds:
            data = ds[variable_name]
            data_arrays.append(data)

    # Concatenate data arrays along the time dimension
    combined_data = xr.concat(data_arrays, dim='time')

    # Define the complete file path for the output file in the /tmp/ directory
    output_file_path = os.path.join('/tmp/', output_filename)

    # Save the combined data to the specified file path
    combined_data.to_netcdf(output_file_path)

    print(f"Combined NetCDF file saved at {output_file_path}")

    # Define the complete file path for the output file in the target directory
    target_file_path = os.path.join(target_directory, output_filename)

    # Check if the target file exists, and ask for user confirmation if it does
    if os.path.exists(target_file_path):
        print(f"Destination file {target_file_path} already exists.")
        response = input("Do you want to overwrite it? (yes/no)")
        while response.lower() not in ['yes', 'no']:
            response = input("Please enter 'yes' or 'no'")
        if response.lower() == 'no':
            print("File not moved")
            exit()

    # Move the file to the target path
    shutil.move(output_file_path, target_file_path)

    print(f"File moved from {output_file_path} to {target_file_path}")