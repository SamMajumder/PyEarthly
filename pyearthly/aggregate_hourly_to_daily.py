# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 09:30:42 2024

@author: samba
"""

import os
import glob
import xarray as xr
import logging
from datetime import datetime
import shutil


def aggregate_hourly_to_daily(source_file_path, destination_path, variable, year, month, data_type, aggregation_method='sum', filename_pattern=None, date_pattern_in_filename='%Y_%m_%d', custom_dimension='time', verbose=False, output_filename_pattern="era5-{data_type}-{year}_{month}.nc"):
    """
    Combines hourly netCDF files into a single netCDF file with layers corresponding to each day in the source files for a given month.
    
    Parameters:
    - source_file_path: Path to the source files.
    - destination_path: Path where the combined file will be saved.
    - variable: The variable in the netCDF files to process.
    - year, month: Year and month for the data.
    - data_type: Type of the data (e.g., temperature, precipitation).
    - aggregation_method: Method for aggregating data ('mean', 'sum', 'median', etc.).
    - filename_pattern: Pattern to match the filenames. If None, a default pattern is used.
    - date_pattern_in_filename: Date format in the filename for extracting the date.
    - custom_dimension: The dimension over which to aggregate.
    - verbose: If True, prints additional information.
    - output_filename_pattern: Pattern for the output filename.
    """

    if filename_pattern is None:
        filename_pattern = f"era5-{data_type}-{year}_{month}_*.nc"

    file_pattern = os.path.join(source_file_path, filename_pattern)
    files = sorted(glob.glob(file_pattern))

    combined_data = []
    time_values = []
    for file in files:
        ds = xr.open_dataset(file)
        if variable not in ds.variables:
            logging.warning(f"No variable named '{variable}' in {file}. Skipping.")
            continue

        # Selecting the aggregation method
        if aggregation_method == 'mean':
            processed_data = ds[variable].mean(dim=custom_dimension)
        elif aggregation_method == 'sum':
            processed_data = ds[variable].sum(dim=custom_dimension)
        elif aggregation_method == 'median':
            processed_data = ds[variable].median(dim=custom_dimension)
        elif aggregation_method == 'min':
            processed_data = ds[variable].min(dim=custom_dimension)
        elif aggregation_method == 'max':
            processed_data = ds[variable].max(dim=custom_dimension)
        elif aggregation_method == 'std':
            processed_data = ds[variable].std(dim=custom_dimension)
        elif aggregation_method == 'var':
            processed_data = ds[variable].var(dim=custom_dimension)
        elif aggregation_method == 'count':
            processed_data = ds[variable].count(dim=custom_dimension)
        else:
            logging.warning(f"Aggregation method '{aggregation_method}' not recognized. Skipping.")
            continue

        combined_data.append(processed_data)

        # Extract and parse date from filename
        date_str = os.path.basename(file).split('-')[-1].replace('.nc', '')
        try:
            time_values.append(datetime.strptime(date_str, date_pattern_in_filename))
        except ValueError:
            logging.warning(f"Date format in file name '{file}' does not match '{date_pattern_in_filename}'. Skipping.")
            continue

    combined = xr.concat(combined_data, dim=xr.Variable('time', time_values))

    if 'units' in ds[variable].attrs:
        combined.attrs['units'] = ds[variable].attrs['units']

    output_filename = output_filename_pattern.format(data_type=data_type, year=year, month=month)
    combined.to_netcdf(output_filename)

    shutil.move(output_filename, os.path.join(destination_path, output_filename))

    if verbose:
        print(f"Combined data saved to {os.path.join(destination_path, output_filename)}")

    return os.path.join(destination_path, output_filename)
