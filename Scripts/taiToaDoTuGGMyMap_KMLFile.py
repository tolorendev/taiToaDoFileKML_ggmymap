import pandas as pd
from xml.etree import ElementTree as ET

# Load the KML file
kml_file_path = "data/VLXD OPSE PAPER 2.kml"
tree = ET.parse(kml_file_path)
root = tree.getroot()

# Define namespaces
namespaces = {
    'kml': 'http://www.opengis.net/kml/2.2',
    'gx': 'http://www.google.com/kml/ext/2.2',
    'atom': 'http://www.w3.org/2005/Atom'
}

# Extract data
data = []
for placemark in root.findall('.//kml:Placemark', namespaces):
    name = placemark.find('kml:name', namespaces).text
    coordinates = placemark.find('.//kml:coordinates', namespaces).text
    data.append([name, coordinates.strip()])

# Create DataFrame
df = pd.DataFrame(data, columns=['Store Name', 'Coordinates'])

# Save to Excel
output_file_path = 'data/stores_coordinates_case_300.xlsx'
df.to_excel(output_file_path, index=False)

# import ace_tools as tools; tools.display_dataframe_to_user(name="Stores and Coordinates", dataframe=df)

output_file_path
