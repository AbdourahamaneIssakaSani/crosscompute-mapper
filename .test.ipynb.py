#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from os import getenv
from pathlib import Path

input_folder = Path(getenv(
    'CROSSCOMPUTE_INPUT_FOLDER', 'batches/standard/input'))
output_folder = Path(getenv(
    'CROSSCOMPUTE_OUTPUT_FOLDER', 'batches/standard/output'))

output_folder.mkdir(parents=True, exist_ok=True)


# In[ ]:


import csv

def extract_data(csv_path, series_code, value_column):
    """
    Extracts data from a CSV file.

    Args:
        csv_path (str): Path to the CSV file.
        series_code (str): The series code to extract.
        value_column (str): The column to extract.

    Returns:
        dict: A dictionary with the country code as the key and the value as the value.
    """

    data = {}

    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            country_code = row['Country Code']
            current_series_code = row['Series Code']
            value = str(row[value_column])

            try:
                value = float(value)
            except ValueError:
                value = None

            if current_series_code == series_code:
                data[country_code] = value

    return data


# In[ ]:


import json

var_path = input_folder / 'variables.dictionary'

data = {}

with var_path.open('rt') as f:
    data = json.load(f)

csv_path = input_folder / 'data.csv'
series_code = data['serie_code']
value_column = data['value_column']
fig_title = data.get('fig_title')
legend_text = data.get('legend_text')


# In[ ]:


import geopandas as gpd
import matplotlib.pyplot as plt

mock_data = extract_data(csv_path, series_code, value_column)


# In[ ]:


from hashlib import blake2b

def get_hash(text):
    "Return the hash of the given text."
    h = blake2b()
    h.update(text.encode())
    return h.hexdigest()

geojson_folder = Path('geojson')
geojson_folder.mkdir(exist_ok=True)

geojson_url = 'https://github.com/datasets/geo-countries/raw/master/data/countries.geojson'

geojson_path = geojson_folder / f'{get_hash(geojson_url)}.geojson'

world_gdf = None

if not geojson_path.exists():
    world_gdf = gpd.read_file(geojson_url)
    world_gdf.to_file(geojson_path, driver='GeoJSON')
else:
    world_gdf = gpd.read_file(geojson_path)


merged_gdf = world_gdf.merge(
    gpd.GeoDataFrame({'ISO_A3': list(mock_data.keys()), 'value': list(mock_data.values())}),
    on='ISO_A3'
)


# In[ ]:


from mpl_toolkits.axes_grid1 import make_axes_locatable

# Plot the map with color based on the 'value' column
fig, ax = plt.subplots(1, 1, figsize=(9, 9))
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)

merged_gdf.to_crs(epsg=3857, inplace=True)

merged_gdf.plot(column='value', cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, cax=cax, legend_kwds={'label': legend_text}, missing_kwds={'color': 'grey', "hatch": "///", 'label': 'Missing values'})

# Add a title
plt.title(fig_title, fontsize=15, fontweight='bold', color='black', loc='center')

# Save the plot as an image
output_image_path = output_folder /'colored_map.png'
plt.savefig(output_image_path, dpi=300, bbox_inches='tight')

print(f"Colored map saved as '{output_image_path}'.")

