from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import re

# Đọc tệp CSV
file_path = 'water agency.csv'
df = pd.read_csv(file_path)

# Khởi tạo WebDriver cho Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Hàm để trích xuất kinh độ và vĩ độ từ URL của Google Maps
def extract_coordinates_from_url(url):
    driver.get(url)
    time.sleep(5)  # Đợi trang tải hoàn toàn
    current_url = driver.current_url
    match = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', current_url)
    if match:
        return float(match.group(1)), float(match.group(2))
    return None, None

# Trích xuất tọa độ từ cột 'URL'
coordinates = [extract_coordinates_from_url(url) for url in df['URL']]
df['Latitude'], df['Longitude'] = zip(*coordinates)

# Thêm cột số thứ tự
df['STT'] = range(1, len(df) + 1)

# Sắp xếp lại các cột theo thứ tự mong muốn
df = df[['STT', 'Tiêu đề', 'Latitude', 'Longitude']]

# Lưu kết quả vào tệp Excel
output_file = 'locations_with_coordinates.xlsx'
df.to_excel(output_file, index=False, engine='openpyxl')

# Đóng trình duyệt
driver.quit()

print(f"Kết quả đã được lưu vào tệp {output_file}")
