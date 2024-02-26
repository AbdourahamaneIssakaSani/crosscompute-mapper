# Welcome to Our Data Visualization Tool

Transform your data into vibrant maps effortlessly with our user-friendly Data Visualization Tool.

To get started, follow these simple steps:

- Visit <https://databank.worldbank.org>.
- Select a database of your choice.
- Click on **Download options** and choose **CSV** format to download the dataset.

Now you're ready to test the tool with your own dataset!

{ series_code }

{ value_column }

{ fig_title }

{ legend_text }

{ min_color }

{ max_color }

{ csv_file }

{ BUTTON_PANEL }

## Quick Help

1. **Series Code**: Specify a unique code for the data you want to visualize, such as population, GDP, or surface area.
2. **Value Column**: Choose the column containing data values corresponding to the series code (e.g., "2000 [YR2000]").
3. **Figure Title**: Add a title to provide context for your map.
4. **Legend Text**: Describe the legend to help viewers understand the color scale.
5. **Min and Max Colors**: Select colors representing minimum and maximum values on your map.
6. **CSV File**: Your data source, following a format similar to the World Bank Data spreadsheet.

## Data Format

The tool adapts to various spreadsheet formats. Here's an example in a World Bank Data format:

```plaintext
Country Name    Country Code    Series Name                              Series Code       2000 [YR2000]   2001 [YR2001]
United States    USA             Population, total                         SP.POP.TOTL       282162411       284968955
United States    USA             Population growth (annual %)              SP.POP.GROW       1.112768997     0.989741382
United States    USA             CO2 emissions (metric tons per capita)    EN.ATM.CO2E.PC    20.46979674     20.17153693

```

Adjust series codes and value columns based on your data structure.
