
# PyEarthly

## Overview

PyEarthly is a comprehensive Python module tailored for environmental scientists, geospatial analysts, and remote sensing professionals. It provides a streamlined interface to Google Earth Engine, enabling users to extract and process satellite imagery and various remote sensing data. The module facilitates the transformation of complex Earth Engine data collections into structured Pandas dataframes, making data analysis and visualization more accessible and efficient.

## Features

- **Data Extraction**: Utilize the `extract_data` function to fetch remote sensing data from a specified Earth Engine data collection within a user-defined temporal and spatial scope.

- **Data Processing**: Convert the extracted data into a Pandas dataframe with the `process_data_to_dataframe` function, which includes options for temporal resolution and specific band selection for analysis.

- **Customizability**: Define custom regions of interest, temporal resolutions, and spectral bands (e.g., NDVI) to tailor the data extraction to your specific research needs.

- **Error Handling**: Built-in logging to capture and report errors during the data extraction and processing stages, ensuring a robust and user-friendly experience.

## Getting Started

To begin using PyEarthly, install the module and set up your environment with Google Earth Engine and Pandas. Ensure you have the necessary credentials for Earth Engine access and familiarize yourself with the Earth Engine Python API for optimal use of PyEarthly.

## Usage

```python
import PyEarthly

# Define your parameters
start_date = 'YYYY-MM-DD'
end_date = 'YYYY-MM-DD'
band = 'NDVI'
region = None  # Default is set to Sundarbans
scale = 1000

# Extract data
collection = PyEarthly.extract_data(start_date, end_date, band=band, region=region, scale=scale)

# Process data into a dataframe
df = PyEarthly.process_data_to_dataframe(collection, start_date, end_date, band=band, region=region, scale=scale)

