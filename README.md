[link](https://github.com/SamMajumder/PyEarthly/blob/main/Images/PyEarthly-DALL-E.png)

**Image Credits: The image(s) used in this project were created with the help of DALL-E, an AI system developed by OpenAI.**


# PyEarthly

PyEarthly is a Python package designed for automated workflows that process and analyze geospatial data. It offers a suite of tools for downloading, aggregating, and managing climate and environmental data from various sources like ERA5 reanalysis and CMIP6 datasets.

## Installation

To install PyEarthly, you can use pip:

```bash

pip install PyEarthly


```


**Make sure you have Python 3.10 or higher installed.**

## Usage

Here are some examples of how you can use PyEarthly:

### Download Global ERA5 Reanalysis Hourly Data

This function downloads ERA5 global daily reanalysis data from the CDS API and saves the data in a user-specified location. It utilizes the cdsapi library to facilitate data download from the CDS API and can move the resulting file to a specified location.

**Parameters**
- **url (str)**: The URL of the CDS API.
- **key (str)**: A unique personal key to access and download data from the CDS API.
- **product_type (str)**: The product type of the data to download (e.g., "reanalysis").
- **format (str)**: The file format of the downloaded file (e.g., "netcdf").
- **variable (str)**: The geophysical parameter for which to download the data (e.g., "total_precipitation").
- **year (str)**: The year for which to download the data.
- **month (str)**: The month for which to download the data.
- **day (str)**: The day for which to download the data.
- **time (list of str)**: The hours of the day for which to download the data, specified in a list (e.g., ['00:00', '03:00', '06:00']). The time values can be zero-padded or not, as long as they are formatted as a string.
- **download_folder_path (str, optional)**: The source folder where the downloaded file should be stored, specified as a string path. If not provided, the file will be stored in the current working directory.
- **final_destination_path (str, optional)**: The destination folder/location where the downloaded file should be stored, specified as a string path. If not provided, the file will be stored in the current working directory.
- **filename (str, optional)**: The name to give to the downloaded file, specified as a string. If not provided, the file will be saved with a default filename of "download.nc".

**Returns**
- **str**: The name of the downloaded file.

**Example Usage**

```python
import pyearthly

pyearthly.download_global_era5_reanalysis_hourly_data(
    url='your_api_url',
    key='your_api_key',
    product_type='reanalysis',
    format='netcdf',
    variable='total_precipitation',
    year='2024',
    month='01',
    day='22',
    time=['00:00', '03:00', '06:00'],
    area=[90, -180, -90, 180],
    download_folder_path='/path/to/download',
    final_destination_path='/path/to/destination',
    filename='precipitation_data.nc'
)
```

### Download Local ERA5 Reanalysis Hourly Data

This function downloads ERA5 hourly reanalysis data from the CDS API, given a Region of Interest (ROI) and saves the data in a user-specified location. It utilizes the `cdsapi` library to facilitate data download from the CDS API and can move the resulting file to a specified location.

**Parameters**
- **url (str)**: The URL of the CDS API.
- **key (str)**: A unique personal key to access and download data from the CDS API.
- **product_type (str)**: The product type of the data to download (e.g., "reanalysis").
- **format (str)**: The file format of the downloaded file (e.g., "netcdf").
- **variable (str)**: The geophysical parameter for which to download the data (e.g., "total_precipitation").
- **year (str)**: The year for which to download the data.
- **month (str)**: The month for which to download the data.
- **day (str)**: The day for which to download the data.
- **time (list of str)**: The hours of the day for which to download the data, specified in a list (e.g., ['00:00', '03:00', '06:00']).
- **area (list of float)**: The geographic bounding box for the area of interest, specified as [North, West, South, East].
- **download_folder_path (str, optional)**: The source folder where the downloaded file should be stored, specified as a string path.
- **final_destination_path (str, optional)**: The destination folder/location where the downloaded file should be stored, specified as a string path.
- **filename (str, optional)**: The name to give to the downloaded file, specified as a string.

**Returns**
- **str**: The name of the downloaded file.

**Example Usage**

```python
url = "https://cds.climate.copernicus.eu/api/v2"
key = "your_personal_key_here"
product_type = "reanalysis"
format = "netcdf"
variable = "total_precipitation"
year = "2020"
month = "06"
day = "15"
time = ['00:00', '06:00', '12:00', '18:00']
area = [55.4318064032368, 24.702107245590803, 12.144718095458737, 87.31267032158668]
download_folder_path = "/path/to/download_folder"
final_destination_path = "/path/to/destination_folder"
filename = "era5_precipitation_20200615.nc"

pyearthly.download_local_era5_reanalysis_hourly_data(
    url, key, product_type, format, variable, year, month, day, time, area,
    download_folder_path, final_destination_path, filename
)

print(f"Downloaded file: {downloaded_file}")

```





### CMIP6 Climate Data Download

The `cmip6_climate_data_download` function is a highly valuable tool in the realm of climate data analysis and research. Its primary utility lies in its ability to streamline the process of accessing and downloading specific subsets of climate data from the CMIP6 (Coupled Model Intercomparison Project Phase 6) dataset.

**Parameters**
- **model**: Climate model name as a string (e.g., 'ACCESS-CM2').
- **timeframe**: Time frame of the data (e.g., 'historical', 'SSP126', 'SSP245').
- **ensemble**: Ensemble member (e.g., 'r1i1p1f1').
- **climate_variable (str)**: Climate variable as a string (e.g., 'pr' for precipitation).
- **start_year (int)**: Start year of the data range.
- **end_year (int)**: End year of the data range.
- **output_folder (str)**: Path to the output folder where files will be saved.

**Description**
This function provides a streamlined interface to download climate data for a specific model, timeframe, ensemble member, and climate variable for a specified range of years. The data is sourced from the extensive CMIP6 dataset, making it easier for researchers to obtain the necessary data for climate analysis and modeling.

**Example Usage**

```python
# Example script to use the function
import pyearthly

# Define parameters for the data download
model = 'ACCESS-CM2'
timeframe = 'historical'
ensemble = 'r1i1p1f1'
climate_variable = 'pr'  # Precipitation
start_year = 2015
end_year = 2020
output_folder = '/path/to/output_folder'

# Call the data download function
pyearthly.cmip6_climate_data_download(
    model=model,
    timeframe=timeframe,
    ensemble=ensemble,
    climate_variable=climate_variable,
    start_year=start_year,
    end_year=end_year,
    output_folder=output_folder
)

```


### Aggregate Hourly Data to Daily


This function combines hourly netCDF files into a single netCDF file with daily layers for a given month, based on a specified variable.

**Parameters**
- **variable (str)**: Crucial Parameter. The variable in the netCDF files to process. Inspect the netCDF files closely to identify the correct variable name. Example: "2m temperature" might be stored as "t2m".
- **source_file_path (str)**: Path to the directory with source netCDF files. Example: "/path/to/hourly/files".
- **destination_path (str)**: Path where the combined daily netCDF file will be saved. Example: "/path/to/save/daily/data".
- **year (str)**: The year for the data. Example: "2021".
- **month (str)**: The month for the data. Example: "06" for June.
- **data_type (str)**: Type of the data. Example: "temperature", "precipitation".
- **aggregation_method (str)**: Method for aggregating data. Options: 'mean', 'sum', 'median', etc. Example: "mean".
- **filename_pattern (str, optional)**: Pattern to match filenames in the source directory. The default pattern is constructed as "era5-{data_type}-{year}_{month}_*.nc". If your files follow a different pattern, specify it here. Example: "era5-2m-temperature-2021_06_*.nc".
- **date_pattern_in_filename (str)**: Date format in the filename. Default: '%Y_%m_%d'. This should match the date format in your file names. Example: "2021_01_01" in the file name "era5-2m-temperature-2021_01_01.nc".
- **custom_dimension (str)**: The dimension for aggregation. Default: 'time'.
- **verbose (bool)**: If True, prints additional information. Default: False.
- **output_filename_pattern (str)**: Pattern for the output filename. Default pattern is "era5-{data_type}-{year}_{month}.nc". Example: "era5-2m-temperature-2021_06.nc".

**Returns**
- **str**: The path to the saved combined netCDF file.

**Description**
The function reads hourly netCDF files, aggregates data per day using the specified method, and combines them into a single file. It is essential to match the variable with the data present in the netCDF files.

The `filename_pattern` is particularly important. The default pattern "era5-{data_type}-{year}_{month}_*.nc" is designed to match files named in a specific format. If your files have a different naming convention, you should specify a custom pattern that matches your files.

**Example Usage**

```python

import pyearthly

pyearthly.aggregate_hourly_to_daily(
    source_file_path='/path/to/hourly/data',
    destination_path='/path/to/daily/data',
    variable='total_precipitation',
    year='2024',
    month='01',
    data_type='precipitation',
    aggregation_method='sum'
)

```

### Aggregate Daily Data to Monthly


This function combines daily netCDF files into a single netCDF file with layers corresponding to each month in the source files for a given year.

**Parameters**
- **variable (str)**: Crucial Parameter. The variable in the netCDF files to process. It is vital to inspect the netCDF files closely to identify the correct variable name as stored in the data. For example, "2m temperature" might be stored as "t2m".
- **source_file_path (str)**: Path to the directory containing source netCDF files. Example: "/path/to/daily/files".
- **destination_path (str)**: Path where the combined monthly netCDF file will be saved. Example: "/path/to/save/monthly/data".
- **year (str)**: The year for which to aggregate the data. Example: "2021".
- **data_type (str)**: Type of the data. Example: "temperature", "precipitation".
- **aggregation_method (str)**: Method for aggregating data. Options include 'mean', 'sum', 'median', etc. Example: "mean".
- **filename_pattern (str, optional)**: Pattern to match filenames in the source directory. The default pattern is constructed as "era5-{data_type}-{year}_*.nc". If your files follow a different pattern, specify it here. Example: "era5-temperature-2021_*.nc".
- **date_pattern_in_filename (str)**: Date format in the filename for extracting the date. Default: '%Y_%m'. This should match the date format in your file names. For example, "2021_01" in "era5-2m-temperature-2021_01.nc".
- **custom_dimension (str)**: The dimension for aggregation. Default: 'time'.
- **verbose (bool)**: If True, prints additional information. Default: False.
- **output_filename_pattern (str)**: Pattern for the output filename. Default pattern is "era5-{data_type}-{year}.nc". Example: "era5-temperature-2021.nc".

**Returns**
- **str**: The path to the saved combined netCDF file.

**Description**
The function reads daily netCDF files, aggregates data per month using the specified method, and combines them into a single file for the specified year. The `filename_pattern` is especially important to ensure accurate data aggregation. The default pattern "era5-{data_type}-{year}_*.nc" matches files named in a specific format. If your files have a different naming convention, you should specify a custom pattern that matches your files.


**Example Usage**

```python
import pyearthly



# Aggregating daily data into monthly averages
output_file = aggregate_daily_to_monthly(
    source_file_path=source_file_path,
    destination_path=destination_path,
    variable=variable,
    year=year,
    data_type=data_type,
    aggregation_method=aggregation_method,
    filename_pattern=filename_pattern,
    date_pattern_in_filename=date_pattern_in_filename,
    custom_dimension="time",  # Assuming aggregation over the 'time' dimension
    verbose=True,
    output_filename_pattern=output_filename_pattern
)

print(f"Output file saved at: {output_file}")


```

### Append NetCDF Files


This function appends multiple NetCDF files found in a specified directory into a single NetCDF file. It temporarily saves the output file to the `/tmp/` directory, then moves it to the specified target directory.

**Parameters**
- **directory (str)**: Path to the directory containing NetCDF files. The function will append all NetCDF files in this directory. Example: "/path/to/source/directory".
- **output_filename (str)**: Name for the output NetCDF file. This is the name of the file that will be created in the `/tmp/` directory and then moved to the target directory. Example: "combined_data.nc".
- **variable_name (str)**: Name of the variable to append across files. It's important to ensure that this variable exists in all the NetCDF files in the specified directory. Inspect the netCDF files closely to identify the correct variable name. Example: "2m temperature" might be stored as "t2m".
- **target_directory (str)**: Path to the target directory where the output file will be moved. Example: "/path/to/target/directory".

**Description**
The function processes each NetCDF file in the specified directory, extracting the specified variable and appending it to a list. It then concatenates these variables along the time dimension to create a single combined dataset. The combined dataset is first saved in the `/tmp/` directory and then moved to the target directory.

**Precautions**
- Ensure all NetCDF files in the directory contain the specified `variable_name`.
- The function temporarily uses disk space in the `/tmp/` directory. Ensure sufficient space is available.
- If a file with the same `output_filename` already exists in the `target_directory`, the function will prompt for confirmation to overwrite it.


**Example Usage**

```python

pyearthly.append_netcdf_files(
    directory='/path/to/netcdf/files',
    output_filename='combined_data.nc',
    variable_name='temperature',
    target_directory='/path/to/combined/data'
)   


```

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

## License
Distributed under the MIT License. See License.txt for more information.

## Contact
Sambadi Majumder - sambadimajumder@gmail.com

Project Link: https://test.pypi.org/project/PyEarthly/0.3.0/
