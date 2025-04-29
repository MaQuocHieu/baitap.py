
import requests
import pandas as pd
from datetime import datetime

# 1. Gọi API để lấy dữ liệu
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "past_days": 10,
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "timezone": "auto"  # tự động chọn múi giờ địa phương
}

response = requests.get(url, params=params)
data = response.json()

# 2. Tạo DataFrame từ dữ liệu nhận được
df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature_2m": data["hourly"]["temperature_2m"],
    "relative_humidity_2m": data["hourly"]["relative_humidity_2m"],
    "wind_speed_10m": data["hourly"]["wind_speed_10m"]
})

# Thêm latitude và longitude vào từng dòng
df["latitude"] = data["latitude"]
df["longitude"] = data["longitude"]

# Chuyển cột time sang kiểu datetime
df["time"] = pd.to_datetime(df["time"])

# 3. Lưu vào file CSV
df.to_csv("weather_data.csv", index=False)
print("✅ Đã lưu dữ liệu vào file 'weather_data.csv'")

# 4. Tính tổng các giá trị đến ngày 29-04
end_date = datetime(2025, 4, 29)
df_filtered = df[df["time"] < end_date]

# Tính tổng
sum_temp = df_filtered["temperature_2m"].sum()
sum_humidity = df_filtered["relative_humidity_2m"].sum()
sum_wind = df_filtered["wind_speed_10m"].sum()

# In kết quả
print("🌡️ Tổng nhiet do:", sum_temp)
print("💧 Tổng do am:", sum_humidity)
print("🍃 Tổng toc do gio:", sum_wind)