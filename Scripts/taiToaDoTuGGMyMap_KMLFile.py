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
    name_tag = placemark.find('kml:name', namespaces)
    coord_tag = placemark.find('.//kml:coordinates', namespaces)

    if name_tag is not None and coord_tag is not None:
        name = name_tag.text.strip()
        coords = coord_tag.text.strip()

        # Lấy longitude, latitude (bỏ qua altitude nếu có)
        lon, lat, *_ = coords.split(",")
        data.append([name, float(lon), float(lat)])

# Create DataFrame
df = pd.DataFrame(data, columns=['Store Name', 'Longitude', 'Latitude'])

# Save to Excel
output_file_path = "data/stores_coordinates_case_300.xlsx"
df.to_excel(output_file_path, index=False)

print(f"File Excel đã được lưu tại: {output_file_path}")
